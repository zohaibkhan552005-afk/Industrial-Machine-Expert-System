
# ============================================================
# INDUSTRIAL MACHINE FAULT DIAGNOSIS EXPERT SYSTEM
# File: knowledge_base/assertions.py
# Total Assertions: 300
# Categories: 10
# ============================================================

ASSERTIONS = []


def add_category(category, entries):
    """Add assertions and automatically assign unique IDs."""
    for name, description, assertion_type in entries:
        ASSERTIONS.append({
            "id": f"A{len(ASSERTIONS) + 1:03d}",
            "category": category,
            "name": name,
            "description": description,
            "type": assertion_type
        })


# ============================================================
# CATEGORY 1: ELECTRIC MOTORS (A001-A030)
# 15 Symptoms, 10 Causes, 5 Diagnoses
# ============================================================

add_category("electric_motors", [
    ("motor_overheating", "Motor temperature is abnormally high.", "symptom"),
    ("motor_excessive_vibration", "Motor produces excessive vibration.", "symptom"),
    ("motor_unusual_noise", "Motor produces abnormal operating noise.", "symptom"),
    ("motor_fails_to_start", "Motor does not start when powered.", "symptom"),
    ("motor_slow_rotation", "Motor rotates slower than normal.", "symptom"),
    ("motor_frequent_tripping", "Motor protection trips repeatedly.", "symptom"),
    ("motor_burning_smell", "Burning odor comes from the motor.", "symptom"),
    ("motor_excessive_current", "Motor draws excessive electrical current.", "symptom"),
    ("motor_inconsistent_speed", "Motor speed fluctuates during operation.", "symptom"),
    ("motor_sparking", "Visible sparking occurs near motor components.", "symptom"),
    ("motor_low_torque", "Motor produces insufficient torque.", "symptom"),
    ("motor_abnormal_voltage", "Motor supply voltage is abnormal.", "symptom"),
    ("motor_excessive_humming", "Motor produces loud humming noise.", "symptom"),
    ("motor_smoke_emission", "Smoke is emitted from the motor.", "symptom"),
    ("motor_intermittent_operation", "Motor operates intermittently.", "symptom"),

    ("motor_bearing_wear", "Motor bearings show signs of wear.", "cause"),
    ("motor_winding_damage", "Motor windings are damaged.", "cause"),
    ("motor_overloading", "Motor operates above its rated load.", "cause"),
    ("motor_phase_imbalance", "Three-phase supply is unbalanced.", "cause"),
    ("motor_insulation_failure", "Motor winding insulation has deteriorated.", "cause"),
    ("motor_cooling_blockage", "Motor cooling passages are blocked.", "cause"),
    ("motor_shaft_misalignment", "Motor shaft is improperly aligned.", "cause"),
    ("motor_loose_connections", "Electrical connections are loose.", "cause"),
    ("motor_lubrication_failure", "Motor bearing lubrication is insufficient.", "cause"),
    ("motor_rotor_damage", "Motor rotor has mechanical damage.", "cause"),

    ("possible_motor_bearing_failure", "Motor bearing may be damaged.", "diagnosis"),
    ("possible_motor_winding_failure", "Motor winding may be defective.", "diagnosis"),
    ("possible_motor_overload_fault", "Motor may be experiencing overload.", "diagnosis"),
    ("possible_motor_cooling_failure", "Motor cooling system may be ineffective.", "diagnosis"),
    ("possible_motor_electrical_fault", "Motor may have an electrical supply fault.", "diagnosis")
])


# ============================================================
# CATEGORY 2: GEARBOXES (A031-A060)
# ============================================================

add_category("gearboxes", [
    ("gearbox_overheating", "Gearbox temperature is unusually high.", "symptom"),
    ("gearbox_abnormal_noise", "Gearbox produces unusual noise.", "symptom"),
    ("gearbox_excessive_vibration", "Gearbox vibrates excessively.", "symptom"),
    ("gearbox_oil_leakage", "Lubricating oil leaks from gearbox.", "symptom"),
    ("gearbox_low_output_speed", "Gearbox output speed is too low.", "symptom"),
    ("gearbox_output_fluctuation", "Gearbox output speed fluctuates.", "symptom"),
    ("gearbox_power_loss", "Gearbox transmits insufficient power.", "symptom"),
    ("gearbox_rough_operation", "Gearbox operates roughly.", "symptom"),
    ("gearbox_metal_particles", "Metal particles appear in gearbox oil.", "symptom"),
    ("gearbox_shaft_noise", "Gearbox shaft produces abnormal noise.", "symptom"),
    ("gearbox_oil_discoloration", "Gearbox oil has unusual discoloration.", "symptom"),
    ("gearbox_abnormal_backlash", "Gearbox backlash is excessive.", "symptom"),
    ("gearbox_seal_leakage", "Oil escapes around gearbox seals.", "symptom"),
    ("gearbox_intermittent_jamming", "Gearbox intermittently jams.", "symptom"),
    ("gearbox_excessive_load", "Gearbox experiences excessive operating load.", "symptom"),

    ("gear_teeth_wear", "Gear teeth are excessively worn.", "cause"),
    ("gear_teeth_damage", "Gear teeth are chipped or broken.", "cause"),
    ("gearbox_low_lubrication", "Gearbox has insufficient lubricant.", "cause"),
    ("gearbox_wrong_lubricant", "Incorrect lubricant is being used.", "cause"),
    ("gearbox_shaft_misalignment", "Gearbox shafts are misaligned.", "cause"),
    ("gearbox_bearing_damage", "Gearbox bearings are damaged.", "cause"),
    ("gearbox_overloading", "Gearbox operates above rated capacity.", "cause"),
    ("gearbox_seal_wear", "Gearbox sealing components are worn.", "cause"),
    ("gearbox_contaminated_oil", "Gearbox lubricant is contaminated.", "cause"),
    ("gearbox_mounting_looseness", "Gearbox mounting bolts are loose.", "cause"),

    ("possible_gear_wear", "Gear teeth may be excessively worn.", "diagnosis"),
    ("possible_gearbox_bearing_failure", "Gearbox bearing failure is suspected.", "diagnosis"),
    ("possible_gearbox_lubrication_failure", "Gearbox lubrication failure is suspected.", "diagnosis"),
    ("possible_gearbox_alignment_fault", "Gearbox alignment fault is suspected.", "diagnosis"),
    ("possible_gearbox_seal_failure", "Gearbox seal failure is suspected.", "diagnosis")
])


# ============================================================
# CATEGORY 3: BEARINGS (A061-A090)
# ============================================================

add_category("bearings", [
    ("bearing_overheating", "Bearing temperature is abnormally high.", "symptom"),
    ("bearing_excessive_noise", "Bearing produces excessive noise.", "symptom"),
    ("bearing_excessive_vibration", "Bearing produces abnormal vibration.", "symptom"),
    ("bearing_grinding_sound", "Grinding noise comes from the bearing.", "symptom"),
    ("bearing_irregular_rotation", "Bearing rotates irregularly.", "symptom"),
    ("bearing_excessive_play", "Bearing has excessive mechanical clearance.", "symptom"),
    ("bearing_seizure", "Bearing rotation becomes completely restricted.", "symptom"),
    ("bearing_grease_leakage", "Grease escapes from the bearing housing.", "symptom"),
    ("bearing_metallic_particles", "Metal particles are found near the bearing.", "symptom"),
    ("bearing_shaft_noise", "Abnormal noise occurs around the bearing shaft.", "symptom"),
    ("bearing_surface_damage", "Visible surface damage appears on bearing.", "symptom"),
    ("bearing_corrosion_marks", "Corrosion marks appear on bearing surfaces.", "symptom"),
    ("bearing_loose_fitting", "Bearing is loose in its housing.", "symptom"),
    ("bearing_unstable_temperature", "Bearing temperature fluctuates abnormally.", "symptom"),
    ("bearing_repeated_failure", "Bearing fails repeatedly during operation.", "symptom"),

    ("bearing_lubrication_shortage", "Bearing has insufficient lubrication.", "cause"),
    ("bearing_overlubrication", "Bearing contains excessive lubricant.", "cause"),
    ("bearing_contamination", "Dust or particles contaminate bearing.", "cause"),
    ("bearing_misalignment", "Bearing is incorrectly aligned.", "cause"),
    ("bearing_improper_installation", "Bearing was installed incorrectly.", "cause"),
    ("bearing_excessive_load", "Bearing experiences excessive mechanical load.", "cause"),
    ("bearing_raceway_damage", "Bearing raceway has surface damage.", "cause"),
    ("bearing_corrosion", "Bearing surfaces are corroded.", "cause"),
    ("bearing_fatigue", "Bearing material shows fatigue damage.", "cause"),
    ("bearing_shaft_looseness", "Bearing fit on the shaft is loose.", "cause"),

    ("possible_bearing_wear", "Bearing wear is suspected.", "diagnosis"),
    ("possible_bearing_lubrication_failure", "Bearing lubrication failure is suspected.", "diagnosis"),
    ("possible_bearing_contamination_fault", "Bearing contamination is suspected.", "diagnosis"),
    ("possible_bearing_misalignment", "Bearing alignment fault is suspected.", "diagnosis"),
    ("possible_bearing_failure", "Bearing failure is suspected.", "diagnosis")
])


# ============================================================
# CATEGORY 4: CONVEYOR SYSTEMS (A091-A120)
# ============================================================

add_category("conveyor_systems", [
    ("conveyor_belt_slipping", "Conveyor belt slips during operation.", "symptom"),
    ("conveyor_belt_misalignment", "Conveyor belt moves away from its center.", "symptom"),
    ("conveyor_motor_overheating", "Conveyor drive motor overheats.", "symptom"),
    ("conveyor_abnormal_noise", "Conveyor produces abnormal noise.", "symptom"),
    ("conveyor_excessive_vibration", "Conveyor vibrates excessively.", "symptom"),
    ("conveyor_slow_movement", "Conveyor moves slower than expected.", "symptom"),
    ("conveyor_complete_stoppage", "Conveyor stops moving unexpectedly.", "symptom"),
    ("conveyor_material_spillage", "Material spills from the conveyor.", "symptom"),
    ("conveyor_belt_tear", "Conveyor belt has visible tears.", "symptom"),
    ("conveyor_roller_jamming", "Conveyor rollers become jammed.", "symptom"),
    ("conveyor_irregular_speed", "Conveyor speed fluctuates.", "symptom"),
    ("conveyor_overloading", "Conveyor carries excessive material.", "symptom"),
    ("conveyor_tracking_problem", "Conveyor belt tracking is unstable.", "symptom"),
    ("conveyor_chain_looseness", "Conveyor drive chain is loose.", "symptom"),
    ("conveyor_abnormal_heat", "Conveyor components generate excessive heat.", "symptom"),

    ("conveyor_low_belt_tension", "Conveyor belt tension is insufficient.", "cause"),
    ("conveyor_drive_roller_wear", "Drive roller surface is worn.", "cause"),
    ("conveyor_roller_bearing_damage", "Conveyor roller bearings are damaged.", "cause"),
    ("conveyor_frame_misalignment", "Conveyor frame is improperly aligned.", "cause"),
    ("conveyor_material_jamming", "Material is obstructing conveyor movement.", "cause"),
    ("conveyor_motor_fault", "Conveyor drive motor has a fault.", "cause"),
    ("conveyor_chain_wear", "Conveyor chain is excessively worn.", "cause"),
    ("conveyor_pulley_damage", "Conveyor pulley is damaged.", "cause"),
    ("conveyor_excessive_friction", "Excessive friction affects belt movement.", "cause"),
    ("conveyor_drive_failure", "Conveyor drive mechanism is defective.", "cause"),

    ("possible_belt_tension_fault", "Incorrect belt tension is suspected.", "diagnosis"),
    ("possible_conveyor_alignment_fault", "Conveyor alignment fault is suspected.", "diagnosis"),
    ("possible_conveyor_bearing_failure", "Conveyor roller bearing failure is suspected.", "diagnosis"),
    ("possible_conveyor_drive_failure", "Conveyor drive failure is suspected.", "diagnosis"),
    ("possible_conveyor_blockage", "Conveyor material blockage is suspected.", "diagnosis")
])


# ============================================================
# CATEGORY 5: HYDRAULIC SYSTEMS (A121-A150)
# ============================================================

add_category("hydraulic_systems", [
    ("hydraulic_low_pressure", "Hydraulic pressure is below normal.", "symptom"),
    ("hydraulic_overheating", "Hydraulic fluid temperature is high.", "symptom"),
    ("hydraulic_fluid_leakage", "Hydraulic fluid leaks from the system.", "symptom"),
    ("hydraulic_slow_actuator", "Hydraulic actuator moves slowly.", "symptom"),
    ("hydraulic_weak_force", "Hydraulic system produces insufficient force.", "symptom"),
    ("hydraulic_pump_noise", "Hydraulic pump produces abnormal noise.", "symptom"),
    ("hydraulic_pressure_fluctuation", "Hydraulic pressure fluctuates.", "symptom"),
    ("hydraulic_foaming", "Foam appears in hydraulic fluid.", "symptom"),
    ("hydraulic_cylinder_drift", "Hydraulic cylinder moves without command.", "symptom"),
    ("hydraulic_jerky_motion", "Hydraulic actuator moves unevenly.", "symptom"),
    ("hydraulic_filter_blockage", "Hydraulic filter becomes blocked.", "symptom"),
    ("hydraulic_pump_failure", "Hydraulic pump fails to operate correctly.", "symptom"),
    ("hydraulic_fluid_discoloration", "Hydraulic fluid changes color.", "symptom"),
    ("hydraulic_system_vibration", "Hydraulic system vibrates excessively.", "symptom"),
    ("hydraulic_actuator_stoppage", "Hydraulic actuator stops unexpectedly.", "symptom"),

    ("hydraulic_fluid_shortage", "Hydraulic reservoir contains insufficient fluid.", "cause"),
    ("hydraulic_air_ingress", "Air enters the hydraulic circuit.", "cause"),
    ("hydraulic_pump_wear", "Hydraulic pump components are worn.", "cause"),
    ("hydraulic_seal_damage", "Hydraulic seals are damaged.", "cause"),
    ("hydraulic_filter_clogging", "Hydraulic filter is clogged.", "cause"),
    ("hydraulic_valve_malfunction", "Hydraulic control valve malfunctions.", "cause"),
    ("hydraulic_fluid_contamination", "Hydraulic fluid contains contaminants.", "cause"),
    ("hydraulic_relief_valve_fault", "Pressure relief valve is defective.", "cause"),
    ("hydraulic_cylinder_seal_wear", "Cylinder seals are worn.", "cause"),
    ("hydraulic_cooling_failure", "Hydraulic cooling is ineffective.", "cause"),

    ("possible_hydraulic_pump_failure", "Hydraulic pump failure is suspected.", "diagnosis"),
    ("possible_hydraulic_leakage_fault", "Hydraulic leakage is suspected.", "diagnosis"),
    ("possible_hydraulic_filter_blockage", "Hydraulic filter blockage is suspected.", "diagnosis"),
    ("possible_hydraulic_valve_failure", "Hydraulic valve failure is suspected.", "diagnosis"),
    ("possible_hydraulic_pressure_fault", "Hydraulic pressure control fault is suspected.", "diagnosis")
])


# ============================================================
# CATEGORY 6: COMPRESSORS (A151-A180)
# ============================================================

add_category("compressors", [
    ("compressor_overheating", "Compressor temperature is excessively high.", "symptom"),
    ("compressor_low_pressure", "Compressor delivers insufficient pressure.", "symptom"),
    ("compressor_excessive_noise", "Compressor produces unusual noise.", "symptom"),
    ("compressor_excessive_vibration", "Compressor vibrates excessively.", "symptom"),
    ("compressor_air_leakage", "Compressed air escapes from the system.", "symptom"),
    ("compressor_fails_to_start", "Compressor fails to start.", "symptom"),
    ("compressor_frequent_shutdown", "Compressor shuts down repeatedly.", "symptom"),
    ("compressor_high_current", "Compressor motor draws excessive current.", "symptom"),
    ("compressor_oil_leakage", "Compressor lubricating oil leaks.", "symptom"),
    ("compressor_low_airflow", "Compressor produces insufficient airflow.", "symptom"),
    ("compressor_pressure_fluctuation", "Compressor output pressure fluctuates.", "symptom"),
    ("compressor_slow_pressure_build", "Compressor builds pressure slowly.", "symptom"),
    ("compressor_oil_contamination", "Compressor oil appears contaminated.", "symptom"),
    ("compressor_water_discharge", "Excessive water appears in compressed air.", "symptom"),
    ("compressor_unusual_smell", "Unusual odor comes from compressor.", "symptom"),

    ("compressor_air_filter_blockage", "Compressor air filter is clogged.", "cause"),
    ("compressor_oil_shortage", "Compressor has insufficient lubricating oil.", "cause"),
    ("compressor_valve_damage", "Compressor valves are damaged.", "cause"),
    ("compressor_piston_wear", "Compressor piston components are worn.", "cause"),
    ("compressor_belt_looseness", "Compressor drive belt is loose.", "cause"),
    ("compressor_cooling_failure", "Compressor cooling is insufficient.", "cause"),
    ("compressor_air_leak", "Compressed air piping has leakage.", "cause"),
    ("compressor_motor_fault", "Compressor motor is defective.", "cause"),
    ("compressor_pressure_switch_fault", "Pressure switch is malfunctioning.", "cause"),
    ("compressor_moisture_accumulation", "Moisture accumulates inside the system.", "cause"),

    ("possible_compressor_overheating_fault", "Compressor overheating fault is suspected.", "diagnosis"),
    ("possible_compressor_valve_failure", "Compressor valve failure is suspected.", "diagnosis"),
    ("possible_compressor_air_leakage", "Compressor air leakage is suspected.", "diagnosis"),
    ("possible_compressor_motor_failure", "Compressor motor failure is suspected.", "diagnosis"),
    ("possible_compressor_pressure_fault", "Compressor pressure regulation fault is suspected.", "diagnosis")
])


# ============================================================
# CATEGORY 7: ELECTRICAL SYSTEMS (A181-A210)
# ============================================================

add_category("electrical_systems", [
    ("electrical_power_failure", "Machine does not receive electrical power.", "symptom"),
    ("electrical_voltage_drop", "Supply voltage drops below normal.", "symptom"),
    ("electrical_voltage_fluctuation", "Supply voltage fluctuates abnormally.", "symptom"),
    ("electrical_circuit_breaker_tripping", "Circuit breaker trips repeatedly.", "symptom"),
    ("electrical_fuse_blowing", "Electrical fuse repeatedly blows.", "symptom"),
    ("electrical_panel_overheating", "Electrical control panel overheats.", "symptom"),
    ("electrical_burning_smell", "Burning odor comes from electrical equipment.", "symptom"),
    ("electrical_sparking", "Electrical connections produce sparks.", "symptom"),
    ("electrical_control_failure", "Machine electrical controls fail.", "symptom"),
    ("electrical_phase_loss", "One electrical supply phase is missing.", "symptom"),
    ("electrical_ground_fault", "Electrical leakage to ground is detected.", "symptom"),
    ("electrical_contact_failure", "Electrical contacts fail to connect.", "symptom"),
    ("electrical_unstable_supply", "Electrical supply is unstable.", "symptom"),
    ("electrical_relay_malfunction", "Electrical relay operates incorrectly.", "symptom"),
    ("electrical_panel_noise", "Electrical panel produces unusual noise.", "symptom"),

    ("electrical_loose_wiring", "Electrical wiring connections are loose.", "cause"),
    ("electrical_overloading", "Electrical circuit carries excessive load.", "cause"),
    ("electrical_insulation_damage", "Electrical insulation is damaged.", "cause"),
    ("electrical_short_circuit", "An unintended electrical connection exists.", "cause"),
    ("electrical_ground_leakage", "Current leaks through an unintended ground path.", "cause"),
    ("electrical_phase_imbalance", "Three-phase supply is unbalanced.", "cause"),
    ("electrical_contactor_damage", "Electrical contactor is damaged.", "cause"),
    ("electrical_relay_failure", "Electrical relay is defective.", "cause"),
    ("electrical_cooling_blockage", "Electrical panel ventilation is obstructed.", "cause"),
    ("electrical_supply_fault", "Incoming electrical supply is defective.", "cause"),

    ("possible_electrical_overload", "Electrical overload is suspected.", "diagnosis"),
    ("possible_electrical_short_circuit", "Electrical short circuit is suspected.", "diagnosis"),
    ("possible_electrical_phase_fault", "Electrical phase fault is suspected.", "diagnosis"),
    ("possible_electrical_connection_failure", "Electrical connection failure is suspected.", "diagnosis"),
    ("possible_electrical_control_fault", "Electrical control system fault is suspected.", "diagnosis")
])


# ============================================================
# CATEGORY 8: CNC MACHINES (A211-A240)
# ============================================================

add_category("cnc_machines", [
    ("cnc_positioning_error", "CNC machine positioning is inaccurate.", "symptom"),
    ("cnc_tool_wear", "CNC cutting tool shows excessive wear.", "symptom"),
    ("cnc_spindle_overheating", "CNC spindle temperature is high.", "symptom"),
    ("cnc_spindle_noise", "CNC spindle produces abnormal noise.", "symptom"),
    ("cnc_excessive_vibration", "CNC machine vibrates excessively.", "symptom"),
    ("cnc_axis_movement_failure", "One or more CNC axes fail to move.", "symptom"),
    ("cnc_surface_finish_defect", "Machined surface has poor finish.", "symptom"),
    ("cnc_tool_breakage", "CNC cutting tool breaks during operation.", "symptom"),
    ("cnc_program_execution_error", "CNC program fails during execution.", "symptom"),
    ("cnc_unexpected_shutdown", "CNC machine shuts down unexpectedly.", "symptom"),
    ("cnc_feed_rate_problem", "CNC feed rate is incorrect.", "symptom"),
    ("cnc_coolant_flow_problem", "CNC coolant flow is insufficient.", "symptom"),
    ("cnc_spindle_speed_fluctuation", "CNC spindle speed fluctuates.", "symptom"),
    ("cnc_machine_accuracy_loss", "CNC machining accuracy deteriorates.", "symptom"),
    ("cnc_tool_changer_failure", "Automatic tool changer fails.", "symptom"),

    ("cnc_tool_dullness", "Cutting tool has become dull.", "cause"),
    ("cnc_axis_misalignment", "CNC machine axes are misaligned.", "cause"),
    ("cnc_spindle_bearing_wear", "Spindle bearings are worn.", "cause"),
    ("cnc_servo_motor_fault", "CNC servo motor is defective.", "cause"),
    ("cnc_encoder_failure", "Position encoder provides incorrect feedback.", "cause"),
    ("cnc_coolant_blockage", "CNC coolant passages are blocked.", "cause"),
    ("cnc_programming_error", "CNC program contains incorrect instructions.", "cause"),
    ("cnc_tool_holder_looseness", "Cutting tool holder is loose.", "cause"),
    ("cnc_guideway_wear", "Machine guideways are excessively worn.", "cause"),
    ("cnc_power_supply_fault", "CNC power supply is defective.", "cause"),

    ("possible_cnc_spindle_failure", "CNC spindle failure is suspected.", "diagnosis"),
    ("possible_cnc_tool_wear_fault", "CNC tool wear fault is suspected.", "diagnosis"),
    ("possible_cnc_axis_fault", "CNC axis movement fault is suspected.", "diagnosis"),
    ("possible_cnc_coolant_failure", "CNC coolant system failure is suspected.", "diagnosis"),
    ("possible_cnc_positioning_fault", "CNC positioning fault is suspected.", "diagnosis")
])


# ============================================================
# CATEGORY 9: COOLING SYSTEMS (A241-A270)
# ============================================================

add_category("cooling_systems", [
    ("cooling_high_temperature", "Cooling system temperature is too high.", "symptom"),
    ("cooling_low_temperature", "Cooling system temperature is below the expected range.", "symptom"),
    ("cooling_fluid_leakage", "Cooling fluid leaks from the system.", "symptom"),
    ("cooling_low_flow", "Cooling fluid flow is insufficient.", "symptom"),
    ("cooling_pump_noise", "Cooling pump produces unusual noise.", "symptom"),
    ("cooling_fan_failure", "Cooling fan fails to operate.", "symptom"),
    ("cooling_excessive_vibration", "Cooling equipment vibrates excessively.", "symptom"),
    ("cooling_pressure_drop", "Cooling system pressure drops.", "symptom"),
    ("cooling_filter_blockage", "Cooling system filter becomes blocked.", "symptom"),
    ("cooling_temperature_fluctuation", "Cooling temperature fluctuates.", "symptom"),
    ("cooling_compressor_failure", "Cooling compressor fails to operate.", "symptom"),
    ("cooling_abnormal_noise", "Cooling system produces abnormal noise.", "symptom"),
    ("cooling_uneven_distribution", "Cooling is unevenly distributed.", "symptom"),
    ("cooling_heat_exchanger_overheating", "Heat exchanger operates at excessive temperature.", "symptom"),
    ("cooling_frequent_shutdown", "Cooling system shuts down repeatedly.", "symptom"),

    ("cooling_refrigerant_shortage", "Cooling system has insufficient refrigerant.", "cause"),
    ("cooling_pump_wear", "Cooling pump components are worn.", "cause"),
    ("cooling_fan_motor_failure", "Cooling fan motor is defective.", "cause"),
    ("cooling_filter_clogging", "Cooling filter is clogged.", "cause"),
    ("cooling_pipe_blockage", "Cooling pipes are obstructed.", "cause"),
    ("cooling_heat_exchanger_fouling", "Heat exchanger surfaces are contaminated.", "cause"),
    ("cooling_thermostat_failure", "Cooling thermostat is defective.", "cause"),
    ("cooling_valve_malfunction", "Cooling control valve malfunctions.", "cause"),
    ("cooling_refrigerant_leak", "Refrigerant escapes from the cooling circuit.", "cause"),
    ("cooling_airflow_restriction", "Airflow through cooling equipment is restricted.", "cause"),

    ("possible_cooling_pump_failure", "Cooling pump failure is suspected.", "diagnosis"),
    ("possible_cooling_flow_fault", "Cooling fluid flow fault is suspected.", "diagnosis"),
    ("possible_cooling_refrigerant_fault", "Refrigerant shortage or leakage is suspected.", "diagnosis"),
    ("possible_cooling_heat_exchanger_fault", "Heat exchanger performance fault is suspected.", "diagnosis"),
    ("possible_cooling_fan_failure", "Cooling fan failure is suspected.", "diagnosis")
])


# ============================================================
# CATEGORY 10: GENERAL MECHANICAL FAULTS (A271-A300)
# ============================================================

add_category("general_mechanical_faults", [
    ("machine_excessive_vibration", "Machine produces excessive vibration.", "symptom"),
    ("machine_abnormal_noise", "Machine produces unusual operating noise.", "symptom"),
    ("machine_overheating", "Machine temperature is abnormally high.", "symptom"),
    ("machine_power_loss", "Machine loses mechanical power.", "symptom"),
    ("machine_unexpected_stoppage", "Machine stops unexpectedly.", "symptom"),
    ("machine_irregular_movement", "Machine movement is irregular.", "symptom"),
    ("machine_excessive_friction", "Machine experiences excessive friction.", "symptom"),
    ("machine_shaft_noise", "Machine shaft produces abnormal noise.", "symptom"),
    ("machine_component_looseness", "Machine components are loose.", "symptom"),
    ("machine_reduced_efficiency", "Machine operating efficiency decreases.", "symptom"),
    ("machine_alignment_problem", "Machine alignment is incorrect.", "symptom"),
    ("machine_repeated_jamming", "Machine repeatedly becomes jammed.", "symptom"),
    ("machine_excessive_wear", "Machine components wear excessively.", "symptom"),
    ("machine_unbalanced_rotation", "Rotating machine components are unbalanced.", "symptom"),
    ("machine_abnormal_movement", "Machine movement differs from normal operation.", "symptom"),

    ("mechanical_misalignment", "Mechanical components are improperly aligned.", "cause"),
    ("mechanical_lubrication_failure", "Mechanical components lack proper lubrication.", "cause"),
    ("mechanical_component_wear", "Mechanical components are worn.", "cause"),
    ("mechanical_fastener_looseness", "Mechanical fasteners are loose.", "cause"),
    ("mechanical_shaft_damage", "Mechanical shaft is damaged.", "cause"),
    ("mechanical_overloading", "Machine operates above its rated load.", "cause"),
    ("mechanical_imbalance", "Rotating components have uneven mass distribution.", "cause"),
    ("mechanical_excessive_friction", "Mechanical contact surfaces create excessive friction.", "cause"),
    ("mechanical_corrosion", "Mechanical components are corroded.", "cause"),
    ("mechanical_deformation", "Mechanical components have changed shape.", "cause"),

    ("possible_mechanical_misalignment", "Mechanical misalignment is suspected.", "diagnosis"),
    ("possible_mechanical_wear", "Mechanical component wear is suspected.", "diagnosis"),
    ("possible_mechanical_overload", "Mechanical overload is suspected.", "diagnosis"),
    ("possible_mechanical_imbalance", "Rotating component imbalance is suspected.", "diagnosis"),
    ("possible_mechanical_lubrication_failure", "Mechanical lubrication failure is suspected.", "diagnosis")
])


# ============================================================
# KNOWLEDGE BASE VALIDATION
# ============================================================

# Total number of assertions
TOTAL_ASSERTIONS = len(ASSERTIONS)

# Check unique assertion IDs
assertion_ids = [item["id"] for item in ASSERTIONS]

# Check unique assertion names
assertion_names = [item["name"] for item in ASSERTIONS]

# Count assertions by category
CATEGORY_COUNTS = {}

for item in ASSERTIONS:
    category = item["category"]
    CATEGORY_COUNTS[category] = CATEGORY_COUNTS.get(category, 0) + 1

# Count assertions by type
TYPE_COUNTS = {}

for item in ASSERTIONS:
    assertion_type = item["type"]
    TYPE_COUNTS[assertion_type] = TYPE_COUNTS.get(assertion_type, 0) + 1

# Validate knowledge base
assert TOTAL_ASSERTIONS == 300, "Assertion count must be 300!"
assert len(set(assertion_ids)) == 300, "Duplicate assertion IDs found!"
assert len(set(assertion_names)) == 300, "Duplicate assertion names found!"
assert len(CATEGORY_COUNTS) == 10, "There must be 10 categories!"
assert all(count == 30 for count in CATEGORY_COUNTS.values()), "Each category must have 30 assertions!"
assert TYPE_COUNTS == {
    "symptom": 150,
    "cause": 100,
    "diagnosis": 50
}, "Assertion type distribution is incorrect!"

print("==========================================")
print("INDUSTRIAL MACHINE EXPERT SYSTEM")
print("KNOWLEDGE BASE VALIDATION")
print("==========================================")
print("Total Assertions:", TOTAL_ASSERTIONS)
print("Total Categories:", len(CATEGORY_COUNTS))
print("Symptoms:", TYPE_COUNTS["symptom"])
print("Causes:", TYPE_COUNTS["cause"])
print("Diagnoses:", TYPE_COUNTS["diagnosis"])

print("\nCategory-wise Assertion Count:")

for category, count in CATEGORY_COUNTS.items():
    print(category, ":", count)

print("\nKnowledge Base loaded successfully!")
