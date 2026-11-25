# ============================================================
# INDUSTRIAL MACHINE FAULT DIAGNOSIS EXPERT SYSTEM
# NLP PROCESSOR - EXPANDED SYNONYM COVERAGE (v5)
#
# Scope of this update:
# - Expand explicit phrase recognition for existing assertions.
# - Preserve the v4 extraction, negation, contradiction and inference logic.
# - Do not change Problem B (uncertainty/negation behavior).
# ============================================================

import re
from knowledge_base.assertions import ASSERTIONS
from inference_engine.engine import diagnose_machine
from nlp.nlp_concepts import build_concept_clauses, concept_match

CONNECTOR_WORDS = {
    "a", "an", "the", "is", "are", "was", "were", "has", "have",
    "been", "being", "to", "of", "with", "in", "on", "at", "from",
    "very", "too", "not", "no", "never", "without"
}

NEGATION_WORDS = {
    "not", "no", "never", "without", "neither", "nor",
    "isnt", "arent", "wasnt", "werent", "hasnt", "havent",
    "doesnt", "dont", "didnt", "cannot", "cant", "couldnt",
    "wont", "wouldnt"
}

# Explicit natural-language alternatives. Phrases are kept specific to avoid
# broad matches that could incorrectly activate unrelated assertions.
SYNONYMS = {
    # ------------------------- ELECTRIC MOTORS -------------------------
    "motor_overheating": [
        "motor is overheating", "motor running hot", "motor is too hot",
        "motor temperature is high", "motor gets hot", "overheating",
        "motor is excessively hot", "motor temperature is rising",
        "motor becomes very hot", "motor is running at high temperature",
        "motor temperature exceeds normal", "motor is hotter than normal"
    ],
    "motor_excessive_vibration": [
        "motor is vibrating excessively", "motor shakes excessively",
        "motor has strong vibration", "motor vibrates a lot",
        "motor has excessive vibrations", "motor is shaking heavily",
        "motor vibration is unusually high", "motor vibrates abnormally",
        "motor has severe vibration", "motor is vibrating more than normal"
    ],
    "motor_unusual_noise": [
        "motor makes unusual noise", "motor makes abnormal noise",
        "motor makes strange noise", "motor is noisy",
        "motor produces unusual sounds", "motor makes grinding noise",
        "motor makes rattling noise", "motor makes knocking noise",
        "motor makes squealing noise", "motor produces abnormal sounds"
    ],
    "motor_fails_to_start": [
        "motor will not start", "motor does not start", "motor won't start",
        "motor fails to run", "motor cannot start", "motor refuses to start",
        "motor is unable to start", "motor does not turn on",
        "motor does not begin running", "motor fails during startup"
    ],
    "motor_slow_rotation": [
        "motor rotates slowly", "motor turns slower than normal",
        "motor speed is too low", "motor runs at low speed",
        "motor is rotating below normal speed", "motor turns very slowly",
        "motor rotation is slow", "motor rpm is low"
    ],
    "motor_frequent_tripping": [
        "motor protection trips repeatedly", "motor trips frequently",
        "motor keeps tripping", "motor trips again and again",
        "motor circuit breaker trips repeatedly", "motor overload trips often",
        "motor trips during operation", "motor protection keeps shutting it down"
    ],
    "motor_burning_smell": [
        "motor smells burnt", "burning odor from motor",
        "motor has a burnt smell", "motor gives off a burning smell",
        "smell of burning from the motor", "motor emits a burnt odor",
        "motor has an electrical burning smell", "burning smell near motor"
    ],
    "motor_excessive_current": [
        "motor draws high current", "motor current is too high",
        "motor is drawing excessive current", "motor consumes too much current",
        "motor current exceeds its rated value", "motor amperage is high",
        "motor draws more current than normal", "motor has overcurrent"
    ],
    "motor_inconsistent_speed": [
        "motor speed fluctuates", "motor speed is unstable",
        "motor speed keeps changing", "motor runs at varying speeds",
        "motor rpm fluctuates", "motor speed is inconsistent",
        "motor does not maintain a steady speed", "motor speed changes unexpectedly"
    ],
    "motor_sparking": [
        "motor is sparking", "sparks are coming from the motor",
        "visible sparks near the motor", "motor produces sparks",
        "electrical sparks around motor", "sparking near motor components",
        "motor has visible arcing", "electric arcing at the motor"
    ],
    "motor_low_torque": [
        "motor produces insufficient torque", "motor has low torque",
        "motor torque is too low", "motor lacks torque",
        "motor cannot provide enough turning force", "motor has weak output torque",
        "motor produces weak turning force", "motor torque is insufficient"
    ],
    "motor_abnormal_voltage": [
        "motor supply voltage is abnormal", "motor voltage is too high",
        "motor voltage is too low", "motor receives unstable voltage",
        "motor supply voltage fluctuates", "voltage supplied to motor is incorrect",
        "motor has voltage irregularities", "motor operates with abnormal voltage"
    ],
    "motor_excessive_humming": [
        "motor produces loud humming noise", "motor is humming loudly",
        "motor makes excessive humming", "motor has a loud hum",
        "motor produces a strong humming sound", "motor hums but does not start",
        "motor makes a continuous humming noise", "motor has abnormal humming"
    ],
    "motor_smoke_emission": [
        "smoke coming from motor", "motor is emitting smoke",
        "motor produces smoke", "smoke is coming out of the motor",
        "motor gives off smoke", "motor releases visible smoke",
        "motor is smoking", "smoke emerges from motor housing"
    ],
    "motor_intermittent_operation": [
        "motor operates intermittently", "motor runs intermittently",
        "motor starts and stops repeatedly", "motor keeps stopping and restarting",
        "motor operation is irregular", "motor runs sometimes and stops",
        "motor does not run continuously", "motor operation comes and goes"
    ],

    # -------------------------- MOTOR CAUSES ---------------------------
    "motor_bearing_wear": [
        "motor bearings are worn", "motor bearing is worn",
        "worn motor bearings", "motor bearings show wear",
        "motor bearing wear", "motor bearings are deteriorated",
        "motor bearings are damaged by wear", "bearing surfaces in motor are worn",
        "motor bearing has excessive wear", "wear in the motor bearings"
    ],
    "motor_winding_damage": [
        "motor windings are damaged", "motor winding is damaged",
        "damaged motor windings", "motor has damaged windings",
        "motor coil is damaged", "motor coils are damaged",
        "motor winding has a defect", "damage to motor winding",
        "stator winding is damaged", "motor winding damage"
    ],
    "motor_overloading": [
        "motor is operating above its rated load", "motor operates above rated load",
        "motor is overloaded", "motor is under excessive load",
        "motor load is above its capacity", "motor is carrying too much load",
        "motor is running under overload", "motor load exceeds its rating",
        "motor is overloaded beyond its rating", "motor is working beyond rated capacity"
    ],
    

    "motor_phase_imbalance": [
        "three phase supply is unbalanced",
        "three-phase supply is unbalanced",
        "three phase power is unbalanced",
        "three-phase power is unbalanced",
        "three phase power supply is unbalanced",
        "three-phase power supply is unbalanced",
        "the three-phase power supply is unbalanced",
        "motor has phase imbalance",
        "motor supply phases are unbalanced",
        "unequal voltage across the three phases",
        "voltage imbalance between phases",
        "phase voltages are unequal",
        "unbalanced three phase voltage",
        "three phase voltage imbalance",
        "motor is supplied with unbalanced phases",
        "motor phases have unequal voltage",
        "one phase has a different voltage"
    ],

    "motor_insulation_failure": [
        "motor winding insulation has deteriorated", "motor insulation has failed",
        "winding insulation is damaged", "motor insulation is deteriorated",
        "insulation on motor windings is damaged", "motor has insulation breakdown",
        "breakdown of winding insulation", "motor insulation resistance is low",
        "winding insulation failure", "motor insulation has broken down"
    ],
    "motor_cooling_blockage": [
        "motor cooling passages are blocked",
        "motor cooling passages are obstructed",
        "cooling passages are blocked", "cooling passages are obstructed",
        "motor cooling is blocked",
        "motor ventilation passages are blocked",
        "motor air vents are blocked", "motor cooling ducts are clogged",
        "airflow through motor is obstructed", "motor cooling vents are clogged"
    ],
    "motor_shaft_misalignment": [
        "motor shaft is misaligned", "motor shaft is out of alignment",
        "motor shaft alignment is incorrect", "motor shaft is not aligned properly",
        "shaft and motor are misaligned", "motor coupling is misaligned",
        "motor shaft alignment is faulty", "incorrect alignment of motor shaft",
        "motor and driven shaft are not aligned", "shaft misalignment in motor"
    ],
    "motor_loose_connections": [
        "motor electrical connections are loose", "loose electrical connections in motor",
        "motor terminals are loose", "motor wiring connections are loose",
        "loose wires at the motor", "motor has loose terminal connections",
        "electrical terminals on motor are loose", "motor connection is not tight",
        "loose motor power connections", "motor wiring is loosely connected"
    ],
    "motor_lubrication_failure": [
        "motor bearings have insufficient lubrication",
        "motor bearing lubrication is insufficient",
        "motor bearings are not properly lubricated",
        "motor has inadequate bearing lubrication",
        "motor bearings are running dry", "insufficient grease in motor bearings",
        "motor bearing has lost lubrication", "lubrication failure in motor bearings",
        "motor bearings lack lubricant", "inadequate lubrication of motor bearings"
    ],
    "motor_rotor_damage": [
        "motor rotor is mechanically damaged", "motor rotor is damaged",
        "damaged rotor in motor", "motor rotor has damage",
        "motor rotor is defective", "rotor components are damaged",
        "motor rotor has a mechanical defect", "broken rotor bars",
        "motor rotor bars are broken", "mechanical damage to motor rotor"
    ],

    # ----------------------- EXISTING OTHER CATEGORIES -----------------
    "machine_power_loss": [
        "machine loses mechanical power", "machine has lost mechanical power",
        "machine has lost power", "machine is losing power"
    ],
    "mechanical_overloading": [
        "machine operates above its rated load",
        "machine is operating above its rated load",
        "machine is overloaded", "machine is overloaded beyond its rating",
        "machine load exceeds its rated capacity",
        "operating above its rated load", "operating above rated load"
    ],
    "gearbox_overheating": [
        "gearbox is overheating", "gearbox running hot",
        "gearbox temperature is high"
    ],
    "gearbox_oil_leakage": [
        "oil is leaking from gearbox", "gearbox leaks oil",
        "gearbox has an oil leak"
    ],
    "gearbox_abnormal_noise": [
        "gearbox makes unusual noise", "gearbox makes strange noise"
    ],
    "bearing_overheating": [
        "bearing is overheating", "bearing running hot",
        "bearing temperature is high"
    ],
    "bearing_excessive_noise": [
        "bearing makes unusual noise", "bearing is noisy"
    ],
    "bearing_excessive_vibration": [
        "bearing vibrates excessively", "bearing has strong vibration"
    ],
    "conveyor_belt_slipping": [
        "conveyor belt is slipping", "belt slips during operation"
    ],
    "conveyor_belt_misalignment": [
        "conveyor belt is off center", "belt is tracking to one side",
        "belt moves to one side"
    ],
    "hydraulic_low_pressure": [
        "hydraulic pressure is low", "low pressure in hydraulic system"
    ],
}

CONTRACTIONS = {
    "isn't": "is not", "aren't": "are not", "wasn't": "was not",
    "weren't": "were not", "hasn't": "has not", "haven't": "have not",
    "doesn't": "does not", "don't": "do not", "didn't": "did not",
    "can't": "cannot", "couldn't": "could not", "won't": "will not",
    "wouldn't": "would not"
}


def normalize_text(text):
    """Normalize text while preserving word order for phrase matching."""
    if not isinstance(text, str):
        raise TypeError("user_text must be a string")

    text = text.lower().replace("_", " ").replace("-", " ")
    for contraction, expanded in CONTRACTIONS.items():
        text = text.replace(contraction, expanded)

    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _phrase_pattern(phrase):
    """Build a conservative phrase pattern with optional connector words."""
    words = normalize_text(phrase).split()
    if not words:
        return None

    pieces = [re.escape(words[0])]
    for word in words[1:]:
        pieces.append(r"(?:\s+(?:" + "|".join(
            re.escape(w) for w in sorted(CONNECTOR_WORDS)
        ) + r")){0,2}\s+" + re.escape(word))

    return re.compile(r"(?<![a-z0-9])" + "".join(pieces) + r"(?![a-z0-9])")


def _find_phrase_spans(text, phrase):
    """Return every non-overlapping occurrence of a phrase."""
    pattern = _phrase_pattern(phrase)
    if pattern is None:
        return []
    return [match.span() for match in pattern.finditer(text)]


def _split_clauses(text):

    """Split text at punctuation and contrast/conjunction boundaries."""
    return [part.strip() for part in re.split(
        r"\b(?:but|however|yet|whereas|although|though|and)\b|[.!?;]",
        text
    ) if part.strip()]

def _carry_subject_context(clauses, category=None):
    """Carry the machine subject into later clauses when it is omitted."""

    if not clauses:
        return clauses

    subject_by_category = {
        "electric_motors": "motor",
        "gearboxes": "gearbox",
        "bearings": "bearing",
        "conveyor_systems": "conveyor",
        "hydraulic_systems": "hydraulic system",
        "compressors": "compressor",
        "electrical_systems": "electrical system",
        "cnc_machines": "cnc machine",
        "cooling_systems": "cooling system",
        "general_mechanical_faults": "machine"
    }

    subject = subject_by_category.get(category)

    if not subject:
        return clauses

    first_clause = clauses[0]

    # Only carry the subject if it is mentioned in the first clause.
    if subject not in first_clause:
        return clauses

    updated_clauses = [first_clause]

    for clause in clauses[1:]:
        if subject not in clause:
            clause = subject + " " + clause

        updated_clauses.append(clause)

    return updated_clauses

def _is_negated(clause, start, end, assertion_name=None):
    """Detect direct negation while preserving negative fault descriptions."""

    prefix = clause[:start].split()
    matched_words = clause[start:end].split()
    context = prefix[-3:] + matched_words

    # "Does not start" and "will not start" describe a starting failure.
    if assertion_name == "motor_fails_to_start":
        return False

    for i, word in enumerate(context[:-1]):
        if word == "not" and context[i + 1] == "only":
            return False

    return any(word in NEGATION_WORDS for word in context)

def _candidate_phrases(assertion, allow_category_scoped_short_phrase=False):
    """Build explicit phrases for one assertion without broad fuzzy matching."""
    name_words = assertion["name"].replace("_", " ").split()
    phrases = [
        assertion["name"].replace("_", " "),
        assertion["description"]
    ]

    if allow_category_scoped_short_phrase and len(name_words) >= 3:
        phrases.append(" ".join(name_words[-2:]))

    phrases.extend(SYNONYMS.get(assertion["name"], []))

    unique = []
    seen = set()
    for phrase in phrases:
        normalized = normalize_text(phrase)
        if normalized and normalized not in seen:
            seen.add(normalized)
            unique.append(phrase)
    return unique



def extract_facts(user_text, category=None):
    """Extract facts using v5 phrase matching and v6 concept matching."""

    normalized_input = normalize_text(user_text)
    clauses = _split_clauses(normalized_input)
    clauses = _carry_subject_context(clauses, category)

    # Build concept-based clauses for NLP v6
    concept_clauses = build_concept_clauses(
        user_text=user_text,
        normalize_fn=normalize_text,
        category=category
    )

    recognized_facts = []
    negated_facts = []
    contradictory_facts = []
    matched_details = []

    for assertion in ASSERTIONS:
        if assertion["type"] not in {"symptom", "cause"}:
            continue

        if category and assertion["category"] != category:
            continue

        fact_name = assertion["name"]
        positive_matches = []
        negative_matches = []

        # --------------------------------
        # NLP V5: Existing phrase matching
        # --------------------------------
        for clause in clauses:
            for phrase in _candidate_phrases(
                assertion,
                allow_category_scoped_short_phrase=bool(category)
            ):
                for start, end in _find_phrase_spans(clause, phrase):
                    detail = (phrase, clause, start, end)

                    if _is_negated(clause, start, end, fact_name):
                        negative_matches.append(detail)
                    else:
                        positive_matches.append(detail)

        # --------------------------------
        # NLP V6: Concept fallback
        # Run only if V5 found nothing
        # --------------------------------
        if not positive_matches and not negative_matches:
            concept_hits = concept_match(assertion, concept_clauses)

            for hit in concept_hits:
                detail = (
                    hit["matched_phrase"],
                    hit["clause"],
                    0,
                    0
                )

                if hit["polarity"] == "negated":
                    negative_matches.append(detail)
                else:
                    positive_matches.append(detail)

        # --------------------------------
        # Combine matching results
        # --------------------------------
        if positive_matches and negative_matches:
            contradictory_facts.append(fact_name)
            phrase = positive_matches[0][0]
            polarity = "contradictory"
            match_method = "contradictory mentions"

        elif positive_matches:
            phrase = positive_matches[0][0]
            recognized_facts.append(fact_name)
            polarity = "positive"

            match_method = (
                "concept" if phrase.startswith("concepts: ")
                else (
                    "synonym"
                    if phrase in SYNONYMS.get(fact_name, [])
                    else "phrase"
                )
            )

        elif negative_matches:
            phrase = negative_matches[0][0]
            negated_facts.append(fact_name)
            polarity = "negated"
            match_method = (
                "concept" if phrase.startswith("concepts: ")
                else "negated phrase"
            )

        else:
            continue

        matched_details.append({
            "assertion": fact_name,
            "category": assertion["category"],
            "type": assertion["type"],
            "description": assertion["description"],
            "match_method": match_method,
            "matched_phrase": phrase,
            "polarity": polarity
        })

    return {
        "recognized_facts": recognized_facts,
        "negated_facts": negated_facts,
        "contradictory_facts": contradictory_facts,
        "matched_details": matched_details,
        "total_recognized": len(recognized_facts)
    }



def analyze_text(user_text, category=None):
    """Run NLP extraction followed by the existing inference engine."""
    extraction = extract_facts(user_text=user_text, category=category)

    results = diagnose_machine(
        facts=extraction["recognized_facts"],
        category=category,
        negated_facts=(extraction["negated_facts"] + extraction["contradictory_facts"])
    )

    diagnoses = results["diagnoses"]
    recognized_facts = extraction["recognized_facts"]
    contradictory_facts = extraction["contradictory_facts"]

    if diagnoses and contradictory_facts:
        analysis_status = "diagnosis_found_with_conflicts"
        analysis_message = (
            "The system found one or more possible diagnoses, but your "
            "description contains conflicting information. The disputed "
            "symptom(s) were excluded from the evidence. Please confirm "
            "whether those symptom(s) are actually present."
        )
        next_steps = [
            "Confirm whether each disputed symptom is present or absent.",
            "Provide any other symptoms observed during operation.",
            "Have a qualified technician verify the possible diagnosis."
        ]
    elif diagnoses:
        analysis_status = "diagnosis_found"
        analysis_message = (
            "The system found possible diagnosis(es) supported by the "
            "recognized evidence. These are preliminary suggestions, "
            "not confirmed faults."
        )
        next_steps = [
            "Review the supporting symptoms and recommended checks.",
            "Follow site safety procedures and have a qualified technician verify the fault."
        ]
    elif contradictory_facts:
        analysis_status = "contradictory_information"
        analysis_message = (
            "Some information is contradictory. The system excluded the "
            "disputed symptom(s), so it cannot safely make a diagnosis yet. "
            "Please clarify whether each disputed symptom is present or absent."
        )
        next_steps = [
            "Clarify whether each disputed symptom is present or absent.",
            "Describe other observable symptoms, if any.",
            "Include when the problem started and under what operating conditions."
        ]
    elif not recognized_facts:
        analysis_status = "no_recognized_symptoms"
        analysis_message = (
            "I could not recognize any symptoms or causes from your "
            "description. No diagnosis was made. Please describe specific, "
            "observable signs rather than saying only that the machine is "
            "behaving strangely."
        )
        next_steps = [
            "Mention any unusual noise, vibration, overheating, smoke, smell, leakage, or loss of power.",
            "Tell us when the problem occurs (startup, normal operation, or under load).",
            "Include the machine type and any recent maintenance or changes."
        ]
    else:
        analysis_status = "insufficient_evidence"
        analysis_message = (
            f"The system recognized {len(recognized_facts)} symptom(s), "
            "but the available evidence does not match enough conditions "
            "for a supported diagnosis. No fault has been guessed. Please "
            "provide more details or additional symptoms."
        )
        next_steps = [
            "Describe any other symptoms, such as unusual noise, vibration, overheating, smoke, smell, leakage, or power loss.",
            "Explain when the symptom occurs and whether it is continuous or intermittent.",
            "Mention operating load, recent maintenance, and any warning indicators."
        ]

    return {
        "user_input": user_text,
        "recognized_facts": recognized_facts,
        "negated_facts": extraction["negated_facts"],
        "contradictory_facts": contradictory_facts,
        "matched_details": extraction["matched_details"],
        "total_recognized": extraction["total_recognized"],
        "diagnoses": diagnoses,
        "total_diagnoses": results["total_diagnoses"],
        "total_rules_fired": results["total_rules_fired"],
        "unrecognized_facts": results["unrecognized_facts"],
        "inference_trace": results["inference_trace"],
        "incomplete_rules": results["incomplete_rules"],
        "analysis_status": analysis_status,
        "analysis_message": analysis_message,
        "next_steps": next_steps
    }


if __name__ == "__main__":
    print("NLP Processor v5 loaded.")
    print("Explicit synonym entries:", len(SYNONYMS))
    print("Electric motor synonym coverage:")
    for assertion in ASSERTIONS:
        if assertion["category"] == "electric_motors" and assertion["type"] in {"symptom", "cause"}:
            print(f"  {assertion['name']}: {len(SYNONYMS.get(assertion['name'], []))} additional phrases")
