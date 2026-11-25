
import streamlit as st
import sys
from pathlib import Path

# --------------------------------------------------
# Ensure Python can access the project folders
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import our NLP processor
from nlp.processor import analyze_text, SYNONYMS
from nlp import nlp_concepts
from nlp.processor import SYNONYMS
from nlp.integrate import enhance_nlp
from inference_engine.engine import diagnose_machine
# Apply NLP extensions only once per Python process
if not getattr(nlp_concepts, "_improvements_applied", False):

    NLP_ENHANCEMENT = enhance_nlp(
        concepts_module=nlp_concepts,
        synonyms_dict=SYNONYMS
    )

    if NLP_ENHANCEMENT["concepts_ok"]:
        nlp_concepts._improvements_applied = True

    print("NLP Enhancement:", NLP_ENHANCEMENT)


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Industrial Machine Expert System",
    page_icon="⚙️",
    layout="wide"
)


# --------------------------------------------------
# Machine categories
# --------------------------------------------------

CATEGORIES = {
    "All Machine Categories": None,
    "Electric Motors": "electric_motors",
    "Gearboxes": "gearboxes",
    "Bearings": "bearings",
    "Conveyor Systems": "conveyor_systems",
    "Hydraulic Systems": "hydraulic_systems",
    "Compressors": "compressors",
    "Electrical Systems": "electrical_systems",
    "CNC Machines": "cnc_machines",
    "Cooling Systems": "cooling_systems",
    "General Mechanical Faults": "general_mechanical_faults"
}


# --------------------------------------------------
# Application heading
# --------------------------------------------------

st.title("⚙️ Industrial Machine Fault Diagnosis")
st.subheader("AI-Based Rule-Driven Expert System")

st.write(
    "Describe the problem with your industrial machine. "
    "The expert system will analyze the symptoms and provide "
    "a possible diagnosis and recommended solution."
)

st.divider()


# --------------------------------------------------
# User input section
# --------------------------------------------------

st.header("1. Enter Machine Information")

selected_category = st.selectbox(
    "Select Machine Category",
    options=list(CATEGORIES.keys())
)

machine_problem = st.text_area(
    "Describe the machine problem:",
    placeholder=(
        "Example: The electric motor is overheating, "
        "making unusual noise, and producing excessive vibration."
    ),
    height=130
)

analyze_button = st.button(
    "🔍 Analyze Machine Problem",
    type="primary",
    use_container_width=True
)



# --------------------------------------------------
# Diagnosis section
# --------------------------------------------------

if analyze_button:

    if not machine_problem.strip():
        st.warning("Please describe the machine problem first.")

    else:
        category_code = CATEGORIES[selected_category]

        with st.spinner("Analyzing machine symptoms..."):
            try:
                result = analyze_text(
                    machine_problem,
                    category=category_code
                )

                # Clear previous checkbox selections for a new analysis.
                for key in list(st.session_state.keys()):
                    if key.startswith("confirmed_symptom_"):
                        del st.session_state[key]

                # Preserve the original NLP analysis.
                st.session_state["base_result"] = result
                st.session_state["current_result"] = result
                st.session_state["analysis_category"] = category_code
                st.session_state["confirmed_facts"] = []

            except Exception as error:
                st.error("An error occurred during analysis.")
                st.exception(error)


# Display results whenever an analysis exists.
# This also keeps results visible after Streamlit reruns.

if "base_result" in st.session_state:

    base_result = st.session_state["base_result"]
    result = st.session_state["current_result"]

    category_code = st.session_state["analysis_category"]

    # --------------------------------------------------
    # Interactive rule completion
    # --------------------------------------------------

    incomplete_rules = result.get("incomplete_rules", [])

    if incomplete_rules:

        st.divider()
        st.header("Additional Symptom Confirmation")

        st.write(
            "The system found rules that partially match your "
            "description. Some conditions are still missing."
        )

        st.info(
            "Select only symptoms that you have actually observed. "
            "The system will not assume that suggested symptoms are present."
        )

        # Collect unique missing facts and the rules that need them.
        missing_fact_map = {}

        original_negative = set(
            base_result.get("negated_facts", [])
            + base_result.get("contradictory_facts", [])
        )

        for rule in incomplete_rules:

            for detail in rule.get("missing_details", []):

                fact = detail["name"]

                # Never suggest a symptom explicitly denied by the user.
                if fact in original_negative:
                    continue

                if fact not in missing_fact_map:
                    missing_fact_map[fact] = {
                        "description": detail["description"],
                        "rules": []
                    }

                missing_fact_map[fact]["rules"].append(
                    rule["rule_id"]
                )

        if missing_fact_map:

            st.subheader("Select the additional symptoms")

            with st.form("confirm_additional_symptoms"):

                for fact, details in sorted(missing_fact_map.items()):

                    rule_ids = ", ".join(
                        sorted(set(details["rules"]))
                    )

                    st.checkbox(
                        f"{details['description']} "
                        f"(Required by: {rule_ids})",
                        key=f"confirmed_symptom_{fact}"
                    )

                update_button = st.form_submit_button(
                    "Update Diagnosis",
                    type="primary",
                    use_container_width=True
                )

            if update_button:

                newly_confirmed = [
                    fact
                    for fact in missing_fact_map
                    if st.session_state.get(
                        f"confirmed_symptom_{fact}", False
                    )
                ]

                # Keep previously confirmed facts as well.
                confirmed_facts = sorted(
                    set(st.session_state["confirmed_facts"])
                    | set(newly_confirmed)
                )

                st.session_state["confirmed_facts"] = confirmed_facts

                # Combine original NLP facts with user-confirmed facts.
                combined_facts = sorted(
                    set(base_result.get("recognized_facts", []))
                    | set(confirmed_facts)
                )

                # Preserve all original negative information.
                negative_facts = (
                    base_result.get("negated_facts", [])
                    + base_result.get("contradictory_facts", [])
                )

                with st.spinner("Updating machine diagnosis..."):

                    updated = diagnose_machine(
                        facts=combined_facts,
                        category=category_code,
                        negated_facts=negative_facts
                    )

                # Update inference results without changing NLP results.
                updated_result = dict(base_result)

                updated_result.update({
                    "diagnoses": updated["diagnoses"],
                    "total_diagnoses": updated["total_diagnoses"],
                    "total_rules_fired": updated["total_rules_fired"],
                    "incomplete_rules": updated["incomplete_rules"],
                    "inference_trace": updated["inference_trace"],
                    "unrecognized_facts": updated["unrecognized_facts"]
                })

                if updated["diagnoses"]:
                    updated_result["analysis_status"] = "diagnosis_found"
                    updated_result["analysis_message"] = (
                        "The system found possible diagnoses after "
                        "including your confirmed symptoms. These are "
                        "preliminary suggestions, not confirmed faults."
                    )
                else:
                    updated_result["analysis_status"] = "insufficient_evidence"
                    updated_result["analysis_message"] = (
                        "Your confirmed symptoms were included, but "
                        "the available evidence still does not satisfy "
                        "a complete diagnostic rule."
                    )

                st.session_state["current_result"] = updated_result
                result = updated_result

                st.success("Diagnosis updated successfully.")

        else:
            st.info(
                "No additional selectable symptoms are available "
                "for the current incomplete rules."
            )

    # --------------------------------------------------
    # Analysis results
    # --------------------------------------------------

    st.divider()
    st.header("2. Analysis Results")

    # Original NLP-recognized facts.
    st.subheader("Recognized Symptoms and Causes")

    recognized_facts = base_result.get("recognized_facts", [])

    if recognized_facts:

        st.success(
            f"{len(recognized_facts)} facts recognized from your description."
        )

        for fact in recognized_facts:
            st.write("✓", fact.replace("_", " ").title())

    else:
        st.warning("No known symptoms or causes were recognized.")

    # Separately display user-confirmed suggestions.
    confirmed_facts = st.session_state.get("confirmed_facts", [])

    if confirmed_facts:

        st.subheader("Additional User-Confirmed Symptoms")

        for fact in confirmed_facts:
            st.write("✓", fact.replace("_", " ").title())

    # --------------------------------------------------
    # Analysis status and guidance
    # --------------------------------------------------

    analysis_status = result.get("analysis_status", "")
    analysis_message = result.get("analysis_message", "")

    if analysis_message:

        if analysis_status in (
            "no_recognized_symptoms",
            "insufficient_evidence",
            "contradictory_information",
            "diagnosis_found_with_conflicts"
        ):
            st.warning(analysis_message)
        else:
            st.info(analysis_message)

    next_steps = result.get("next_steps", [])

    if next_steps:
        st.markdown("**What to provide or do next:**")

        for step in next_steps:
            st.write("•", step)

    # --------------------------------------------------
    # Diagnosis results
    # --------------------------------------------------

    st.subheader("Expert System Diagnosis")

    diagnoses = result.get("diagnoses", [])

    if diagnoses:

        for index, diagnosis in enumerate(diagnoses, start=1):

            severity = diagnosis.get(
                "severity", "unknown"
            ).upper()

            st.markdown(f"### Diagnosis {index}")

            if severity == "CRITICAL":
                st.error(f"Severity: {severity}")

            elif severity == "HIGH":
                st.warning(f"Severity: {severity}")

            elif severity == "MEDIUM":
                st.info(f"Severity: {severity}")

            else:
                st.success(f"Severity: {severity}")

            st.write(
                "**Possible Fault:**",
                diagnosis.get("diagnosis", "Not available")
            )

            st.write(
                "**Recommended Solution:**",
                diagnosis.get("solution", "Not available")
            )

            st.write(
                "**Explanation:**",
                diagnosis.get("explanation", "Not available")
            )

            st.write(
                "**Rule IDs:**",
                diagnosis.get(
                    "rule_ids",
                    [diagnosis.get("rule_id", "Not available")]
                )
            )

            st.write(
                "**Matched Conditions:**",
                diagnosis.get("matched_conditions", [])
            )

            st.divider()

    else:
        st.warning(
            "No complete diagnostic rule has been satisfied yet."
        )

    # --------------------------------------------------
    # Inference engine statistics
    # --------------------------------------------------

    st.subheader("3. Inference Engine Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "NLP Recognized Facts",
        len(recognized_facts)
    )

    col2.metric(
        "Diagnoses Found",
        result.get("total_diagnoses", 0)
    )

    col3.metric(
        "Rules Fired",
        result.get("total_rules_fired", 0)
    )

    # --------------------------------------------------
    # Inference trace
    # --------------------------------------------------

    with st.expander("View Inference Trace"):

        trace = result.get("inference_trace", [])

        if trace:
            for step in trace:
                st.write(step)
        else:
            st.write("No inference steps were recorded.")

    # --------------------------------------------------
    # Unrecognized facts
    # --------------------------------------------------

    with st.expander("View Unrecognized Information"):

        unrecognized = result.get("unrecognized_facts", [])

        if unrecognized:
            st.write(unrecognized)
        else:
            st.write("No unrecognized facts were returned.")

    # --------------------------------------------------
    # Recognized assertion details
    # --------------------------------------------------

    with st.expander("View Recognized Fact Details"):

        st.json(base_result.get("matched_details", []))



# --------------------------------------------------
# Safety notice
# --------------------------------------------------

st.divider()

st.warning(
    "Safety Notice: This expert system provides preliminary "
    "diagnostic suggestions. Always follow industrial safety "
    "procedures. Isolate machinery before inspection and consult "
    "a qualified technician for repairs."
)

st.caption(
    "Industrial Machine Fault Diagnosis Expert System | "
    "Python + Streamlit | Rule-Based AI"
)