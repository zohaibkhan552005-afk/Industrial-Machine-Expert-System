# ============================================================
# INDUSTRIAL MACHINE FAULT DIAGNOSIS EXPERT SYSTEM
# INFERENCE ENGINE - EVIDENCE-BASED RULE EVALUATION (v2)
#
# Ranking policy:
# 1. More distinct observed facts supporting a diagnosis.
# 2. More distinct rules supporting that diagnosis.
# 3. Severity is used only as a final tie-breaker / safety label.
#
# IMPORTANT:
# This engine does not calculate medical/statistical probability.
# A rule match is evidence according to the authored knowledge base,
# not proof that a machine fault is confirmed.
# ============================================================

from collections import defaultdict

from knowledge_base.rules import RULES
from knowledge_base.assertions import ASSERTIONS


SEVERITY_RANK = {
    "low": 1,
    "medium": 2,
    "high": 3,
    "critical": 4
}

ASSERTION_BY_NAME = {
    assertion["name"]: assertion
    for assertion in ASSERTIONS
}

VALID_ASSERTIONS = set(ASSERTION_BY_NAME)
VALID_CATEGORIES = {
    assertion["category"] for assertion in ASSERTIONS
}
VALID_RULE_IDS = {rule["id"] for rule in RULES}


def _as_fact_set(values, parameter_name):
    """Convert an iterable of fact names into a validated string set."""
    if values is None:
        return set()

    if isinstance(values, str):
        values = [values]

    try:
        result = set(values)
    except TypeError as exc:
        raise TypeError(
            f"{parameter_name} must be an iterable of assertion names."
        ) from exc

    if not all(isinstance(item, str) for item in result):
        raise TypeError(
            f"Every item in {parameter_name} must be a string."
        )

    return result


def _severity_value(severity):
    """Return a safe numeric severity rank for sorting."""
    return SEVERITY_RANK.get(str(severity).lower(), 0)


def diagnose_machine(facts, category=None, negated_facts=None):
    """
    Evaluate expert rules against observed facts and rank diagnoses
    using distinct supporting evidence.

    Parameters:
        facts:
            Explicitly recognized positive symptoms/causes.
        category:
            Optional machine category, e.g. "electric_motors".
        negated_facts:
            Optional facts explicitly reported as absent.

    Returns:
        A dictionary compatible with the previous engine's main
        result fields, with additional evidence and conflict details.

    Notes:
        - A diagnosis is only a possible diagnosis supported by rules.
        - No probability/confidence percentage is invented.
        - A fact reported both positively and negatively is excluded.
        - Severity is not treated as diagnostic likelihood.
    """

    positive_input = _as_fact_set(facts, "facts")
    negative_input = _as_fact_set(negated_facts, "negated_facts")

    if category is not None and category not in VALID_CATEGORIES:
        raise ValueError(
            f"Unknown category '{category}'. "
            f"Valid categories: {sorted(VALID_CATEGORIES)}"
        )

    # Separate unknown assertions from valid knowledge-base assertions.
    unrecognized_facts = positive_input - VALID_ASSERTIONS
    unrecognized_negated_facts = negative_input - VALID_ASSERTIONS

    valid_positive = positive_input & VALID_ASSERTIONS
    valid_negative = negative_input & VALID_ASSERTIONS

    # A fact cannot safely be treated as positive when the input also
    # explicitly states that it is absent.
    conflicting_facts = valid_positive & valid_negative
    working_memory = valid_positive - valid_negative

    # Only symptom/cause assertions are valid observations for rule
    # conditions. Diagnoses must not be accepted as user observations.
    non_observation_facts = {
        fact for fact in working_memory
        if ASSERTION_BY_NAME[fact]["type"] not in {"symptom", "cause"}
    }
    working_memory -= non_observation_facts

    # Aggregate rule evidence by diagnosis.
    diagnosis_results = {}
    fired_rules = set()
    inference_trace = []
    incomplete_rules = []

    
    for rule in RULES:
        rule_id = rule["id"]

        if category is not None and rule["category"] != category:
            continue

        conditions = set(rule["conditions"])

        # Determine which rule conditions are already satisfied.
        matched_conditions = conditions & working_memory
        missing_conditions = conditions - working_memory

        # Handle rules that are not yet fully satisfied.
        if missing_conditions:

            # Suggest completion only when at least one condition
            # is present and none of the required conditions is negated.
            if matched_conditions and not (conditions & valid_negative):

                missing_details = []

                for fact in sorted(missing_conditions):
                    assertion = ASSERTION_BY_NAME.get(fact)

                    if assertion:
                        missing_details.append({
                            "name": fact,
                            "description": assertion["description"]
                        })

                incomplete_rules.append({
                    "rule_id": rule_id,
                    "category": rule["category"],
                    "diagnosis": rule["diagnosis"],
                    "matched_conditions": sorted(matched_conditions),
                    "missing_conditions": sorted(missing_conditions),
                    "missing_details": missing_details,
                    "severity": rule["severity"],
                    "solution": rule["solution"],
                    "explanation": rule["explanation"]
                })

            # An incomplete rule must never fire.
            continue

        # All conditions are present: the rule can fire.
        fired_rules.add(rule_id)
        diagnosis = rule["diagnosis"]

        if diagnosis not in diagnosis_results:
            diagnosis_results[diagnosis] = {
                "diagnosis": diagnosis,
                "category": rule["category"],
                "severity": rule["severity"],
                "solution": rule["solution"],
                "explanation": rule["explanation"],
                "rule_ids": [],
                "matched_conditions": [],
                "supporting_evidence": [],
                "solutions": [],
                "explanations": [],
                "supporting_rule_count": 0,
                "diagnostic_evidence_count": 0,
                "evidence_status": (
                    "Possible diagnosis supported by matching rule(s); "
                    "not a confirmed fault."
                )
            }

        result = diagnosis_results[diagnosis]

        if rule_id not in result["rule_ids"]:
            result["rule_ids"].append(rule_id)

        for condition in rule["conditions"]:
            if condition not in result["matched_conditions"]:
                result["matched_conditions"].append(condition)

            assertion = ASSERTION_BY_NAME.get(condition)

            if assertion:
                evidence_item = {
                    "name": condition,
                    "description": assertion["description"],
                    "type": assertion["type"]
                }

                if evidence_item not in result["supporting_evidence"]:
                    result["supporting_evidence"].append(evidence_item)

        if rule["solution"] not in result["solutions"]:
            result["solutions"].append(rule["solution"])

        if rule["explanation"] not in result["explanations"]:
            result["explanations"].append(rule["explanation"])

        if _severity_value(rule["severity"]) > _severity_value(
            result["severity"]
        ):
            result["severity"] = rule["severity"]

        inference_trace.append({
            "rule_id": rule_id,
            "category": rule["category"],
            "conditions": list(rule["conditions"]),
            "matched_conditions": sorted(matched_conditions),
            "diagnosis": diagnosis,
            "severity": rule["severity"],
            "status": "fired"
        })


    # Finalize evidence counts and retain backward-compatible primary
    # solution/explanation fields while exposing all alternatives.
    for result in diagnosis_results.values():
        result["supporting_rule_count"] = len(result["rule_ids"])
        result["diagnostic_evidence_count"] = len(
            result["matched_conditions"]
        )
        # Backward-compatible field for the current Streamlit interface.
        result["rule_id"] = (
            result["rule_ids"][0] if result["rule_ids"] else None
        )

        if result["solutions"]:
            result["solution"] = result["solutions"][0]

        if result["explanations"]:
            result["explanation"] = result["explanations"][0]

    # Rank by distinct evidence first. Rule count is a secondary
    # knowledge-base support signal. Severity is only a final tie-breaker.
    sorted_results = sorted(
        diagnosis_results.values(),
        key=lambda item: (
            item["diagnostic_evidence_count"],
            item["supporting_rule_count"],
            _severity_value(item["severity"])
        ),
        reverse=True
    )

    return {
        "input_facts": sorted(working_memory),
        "negated_facts": sorted(valid_negative),
        "conflicting_facts": sorted(conflicting_facts),
        "unrecognized_facts": sorted(unrecognized_facts),
        "unrecognized_negated_facts": sorted(unrecognized_negated_facts),
        "ignored_non_observation_facts": sorted(non_observation_facts),
        "working_memory": sorted(working_memory),
        "diagnoses": sorted_results,
        "total_diagnoses": len(sorted_results),
        "total_rules_fired": len(fired_rules),
        "inference_trace": inference_trace,
        "incomplete_rules": incomplete_rules
    }


def _run_self_tests():
    """Basic deterministic checks for engine behavior."""
    assert len(VALID_RULE_IDS) == len(RULES), "Duplicate rule IDs found."

    # No facts must never produce a diagnosis.
    empty_result = diagnose_machine([])
    assert empty_result["total_diagnoses"] == 0
    assert empty_result["total_rules_fired"] == 0

    # Every rule should fire when all of its own conditions are supplied
    # within its category. Other rules may also fire.
    for rule in RULES:
        result = diagnose_machine(
            facts=rule["conditions"],
            category=rule["category"]
        )
        assert rule["diagnosis"] in {
            item["diagnosis"] for item in result["diagnoses"]
        }, f"Rule {rule['id']} did not produce its expected diagnosis."

    # Unknown facts must not create diagnoses.
    unknown_result = diagnose_machine(["made_up_fault_symptom"])
    assert unknown_result["total_diagnoses"] == 0
    assert "made_up_fault_symptom" in unknown_result["unrecognized_facts"]

    # Explicitly negated facts must not satisfy a rule.
    sample_rule = RULES[0]
    first_condition = sample_rule["conditions"][0]
    second_condition = sample_rule["conditions"][1]
    negation_result = diagnose_machine(
        facts=[first_condition, second_condition],
        negated_facts=[first_condition],
        category=sample_rule["category"]
    )
    assert first_condition not in negation_result["working_memory"]
    assert sample_rule["diagnosis"] not in {
        item["diagnosis"] for item in negation_result["diagnoses"]
    }

    # A diagnosis assertion supplied as an observation must be ignored.
    diagnosis_assertions = [
        a["name"] for a in ASSERTIONS if a["type"] == "diagnosis"
    ]
    if diagnosis_assertions:
        result = diagnose_machine([diagnosis_assertions[0]])
        assert diagnosis_assertions[0] in result[
            "ignored_non_observation_facts"
        ]

    print("INFERENCE ENGINE SELF-TESTS: PASSED")
    print(f"Rules checked: {len(RULES)}")
    print("Checks: empty input, all rule triggers, unknown facts,")
    print("        negated facts, and diagnosis-as-input rejection.")


if __name__ == "__main__":
    print("=" * 55)
    print("INDUSTRIAL MACHINE EXPERT SYSTEM")
    print("EVIDENCE-BASED INFERENCE ENGINE TEST")
    print("=" * 55)
    _run_self_tests()

    # Demonstrate a sample rule with its own required conditions.
    sample_rule = RULES[0]
    sample_result = diagnose_machine(
        facts=sample_rule["conditions"],
        category=sample_rule["category"]
    )

    print("\nSample category:", sample_rule["category"])
    print("Sample input facts:", sample_rule["conditions"])
    print("\nRanked possible diagnoses:")

    for index, result in enumerate(sample_result["diagnoses"], 1):
        print(f"\n{index}. {result['diagnosis']}")
        print("   Severity:", result["severity"])
        print("   Distinct evidence:", result["diagnostic_evidence_count"])
        print("   Supporting rules:", result["supporting_rule_count"])
        print("   Rule IDs:", result["rule_ids"])
        print("   Matched conditions:", result["matched_conditions"])

    print("\nTotal rules fired:", sample_result["total_rules_fired"])
    print("Total diagnoses:", sample_result["total_diagnoses"])
