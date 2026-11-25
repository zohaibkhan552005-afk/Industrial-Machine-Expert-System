
from inference_engine.engine import diagnose_machine

TEST_CASES = [
    {
        "rule": "R103",
        "facts": ["motor_bearing_wear", "motor_excessive_vibration"],
        "diagnosis": "possible_motor_bearing_failure"
    },
    {
        "rule": "R104",
        "facts": ["motor_lubrication_failure", "motor_unusual_noise"],
        "diagnosis": "possible_motor_bearing_failure"
    },
    {
        "rule": "R105",
        "facts": ["motor_winding_damage", "motor_smoke_emission"],
        "diagnosis": "possible_motor_winding_failure"
    },
    {
        "rule": "R106",
        "facts": ["motor_insulation_failure", "motor_burning_smell"],
        "diagnosis": "possible_motor_winding_failure"
    },
    {
        "rule": "R107",
        "facts": ["motor_overloading", "motor_excessive_current"],
        "diagnosis": "possible_motor_overload_fault"
    },
    {
        "rule": "R108",
        "facts": ["motor_phase_imbalance", "motor_abnormal_voltage"],
        "diagnosis": "possible_motor_electrical_fault"
    },
    {
        "rule": "R109",
        "facts": ["motor_loose_connections", "motor_intermittent_operation"],
        "diagnosis": "possible_motor_electrical_fault"
    }
]

print("=" * 65)
print("NEW ELECTRIC MOTOR RULE TESTS")
print("=" * 65)

passed = 0
failed = 0

for test in TEST_CASES:
    result = diagnose_machine(
        facts=test["facts"],
        category="electric_motors"
    )

    fired_ids = {
        item["rule_id"]
        for item in result["inference_trace"]
    }

    diagnosis_names = {
        item["diagnosis"]
        for item in result["diagnoses"]
    }

    success = (
        test["rule"] in fired_ids
        and test["diagnosis"] in diagnosis_names
    )

    if success:
        passed += 1
        status = "PASS"
    else:
        failed += 1
        status = "FAIL"

    print(f"\n{test['rule']}: {status}")
    print("Input:", test["facts"])
    print("Expected:", test["diagnosis"])
    print("Fired rules:", sorted(fired_ids))
    print("Diagnoses:", sorted(diagnosis_names))

print("\n" + "=" * 65)
print(f"PASSED: {passed}/7")
print(f"FAILED: {failed}/7")
print("=" * 65)

if failed:
    raise AssertionError("Some new motor rule tests failed.")
