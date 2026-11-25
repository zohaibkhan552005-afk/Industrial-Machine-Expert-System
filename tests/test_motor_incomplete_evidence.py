
from inference_engine.engine import diagnose_machine

TEST_CASES = [
    ("R103", ["motor_bearing_wear"]),
    ("R104", ["motor_lubrication_failure"]),
    ("R105", ["motor_winding_damage"]),
    ("R106", ["motor_insulation_failure"]),
    ("R107", ["motor_overloading"]),
    ("R108", ["motor_phase_imbalance"]),
    ("R109", ["motor_loose_connections"]),
]

print("=" * 60)
print("MOTOR INCOMPLETE EVIDENCE TEST")
print("=" * 60)

passed = 0
failed = 0

for rule_id, facts in TEST_CASES:
    result = diagnose_machine(
        facts=facts,
        category="electric_motors"
    )

    fired_ids = {
        item["rule_id"]
        for item in result["inference_trace"]
    }

    success = rule_id not in fired_ids

    if success:
        passed += 1
        status = "PASS"
    else:
        failed += 1
        status = "FAIL"

    print(f"{rule_id}: {status} | Input: {facts}")

print("\n" + "=" * 60)
print(f"PASSED: {passed}/7")
print(f"FAILED: {failed}/7")
print("=" * 60)

if failed:
    raise AssertionError("Incomplete evidence test failed.")
