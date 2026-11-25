
# ============================================================
# INDUSTRIAL MACHINE FAULT DIAGNOSIS EXPERT SYSTEM
# File: knowledge_base/rules.py
# Total Rules: 102
# Categories: 10
# Inference: Forward Chaining
# ============================================================

RULES = []


def add_category(category, entries):
    """Add rules and automatically generate unique rule IDs."""

    for conditions, diagnosis, solution, explanation, severity in entries:
        RULES.append({
            "id": f"R{len(RULES) + 1:03d}",
            "category": category,
            "conditions": conditions,
            "diagnosis": diagnosis,
            "solution": solution,
            "explanation": explanation,
            "severity": severity
        })


# ============================================================
# CATEGORY 1: ELECTRIC MOTORS (R001-R010)
# ============================================================

add_category("electric_motors", [

    (
        ["motor_overheating", "motor_excessive_vibration", "motor_unusual_noise"],
        "possible_motor_bearing_failure",
        "Stop the motor if overheating or vibration is severe. Have a qualified technician inspect the bearings, lubrication and alignment.",
        "Overheating, vibration and unusual noise together may indicate damaged motor bearings.",
        "high"
    ),

    (
        ["motor_overheating", "motor_excessive_current"],
        "possible_motor_overload_fault",
        "Check the motor load against its rated capacity. Inspect the driven equipment and electrical protection settings.",
        "Excessive current combined with overheating may indicate motor overload.",
        "high"
    ),

    (
        ["motor_fails_to_start", "motor_excessive_humming"],
        "possible_motor_electrical_fault",
        "Have a qualified electrician check the supply voltage, phase condition, starter and motor windings.",
        "A motor that hums without starting may have a supply, starting circuit or winding problem.",
        "high"
    ),

    (
        ["motor_burning_smell", "motor_smoke_emission"],
        "possible_motor_winding_failure",
        "Immediately isolate the equipment using the approved shutdown procedure. Do not restart until the windings and insulation have been inspected.",
        "Burning odor and smoke may indicate serious insulation or winding damage.",
        "critical"
    ),

    (
        ["motor_abnormal_voltage", "motor_inconsistent_speed"],
        "possible_motor_electrical_fault",
        "Have a qualified electrician measure the supply voltage and inspect the electrical supply and motor connections.",
        "Abnormal voltage can cause unstable motor speed.",
        "high"
    ),

    (
        ["motor_slow_rotation", "motor_low_torque"],
        "possible_motor_overload_fault",
        "Inspect the mechanical load, motor rating and supply conditions before returning the motor to service.",
        "Low speed and insufficient torque may indicate overload or inadequate motor supply.",
        "medium"
    ),

    (
        ["motor_frequent_tripping", "motor_excessive_current"],
        "possible_motor_overload_fault",
        "Check the actual operating current, mechanical load and protective devices. Do not repeatedly reset the protection.",
        "Repeated tripping with excessive current suggests an overload or related electrical fault.",
        "high"
    ),

    (
        ["motor_excessive_humming", "motor_abnormal_voltage"],
        "possible_motor_electrical_fault",
        "Arrange an electrical inspection of the supply phases, connections and motor circuit.",
        "Abnormal voltage and excessive humming can indicate an electrical supply or magnetic imbalance problem.",
        "high"
    ),

    (
        ["motor_excessive_vibration", "motor_intermittent_operation"],
        "possible_motor_bearing_failure",
        "Inspect bearing condition, shaft alignment and mounting stability before restarting the equipment.",
        "Excessive vibration and intermittent operation may be associated with mechanical bearing damage.",
        "high"
    ),

    (
        ["motor_overheating", "motor_burning_smell"],
        "possible_motor_winding_failure",
        "Shut down and isolate the motor. Arrange inspection of the winding insulation, ventilation and electrical supply.",
        "Overheating combined with a burning smell may indicate winding insulation deterioration.",
        "critical"
    )
])


# ============================================================
# CATEGORY 2: GEARBOXES (R011-R020)
# ============================================================

add_category("gearboxes", [

    (
        ["gearbox_overheating", "gearbox_oil_leakage"],
        "possible_gearbox_lubrication_failure",
        "Inspect oil level, seals and lubricant condition. Refill only with the manufacturer's specified lubricant.",
        "Oil leakage may reduce lubrication and cause gearbox overheating.",
        "high"
    ),

    (
        ["gearbox_abnormal_noise", "gearbox_metal_particles"],
        "possible_gear_wear",
        "Arrange an inspection of internal gear teeth and oil contamination. Replace damaged components as required.",
        "Abnormal noise combined with metal particles may indicate gear tooth wear or damage.",
        "high"
    ),

    (
        ["gearbox_excessive_vibration", "gearbox_shaft_noise"],
        "possible_gearbox_alignment_fault",
        "Inspect gearbox shaft alignment, coupling condition and mounting.",
        "Vibration and shaft noise may indicate misalignment or mechanical looseness.",
        "high"
    ),

    (
        ["gearbox_overheating", "gearbox_oil_discoloration"],
        "possible_gearbox_lubrication_failure",
        "Check lubricant quality, operating temperature and oil specification. Replace contaminated lubricant according to maintenance procedures.",
        "Discolored oil and excessive heat may indicate lubricant degradation.",
        "high"
    ),

    (
        ["gearbox_seal_leakage", "gearbox_oil_leakage"],
        "possible_gearbox_seal_failure",
        "Inspect gearbox seals and sealing surfaces. Replace damaged seals and verify correct oil level.",
        "Oil leakage around the sealing area may indicate deteriorated seals.",
        "medium"
    ),

    (
        ["gearbox_low_output_speed", "gearbox_power_loss"],
        "possible_gear_wear",
        "Inspect gear teeth, coupling and transmission components for wear or damage.",
        "Reduced output speed and power may indicate damaged or worn transmission components.",
        "medium"
    ),

    (
        ["gearbox_abnormal_backlash", "gearbox_rough_operation"],
        "possible_gear_wear",
        "Measure gear backlash according to manufacturer specifications and inspect the gear assembly.",
        "Excessive backlash and rough operation may indicate gear wear.",
        "medium"
    ),

    (
        ["gearbox_excessive_load", "gearbox_overheating"],
        "possible_gearbox_lubrication_failure",
        "Verify the gearbox load rating and lubrication condition. Reduce excessive loading.",
        "Excessive operating load can increase friction and gearbox temperature.",
        "high"
    ),

    (
        ["gearbox_bearing_damage", "gearbox_excessive_vibration"],
        "possible_gearbox_bearing_failure",
        "Arrange bearing inspection and check shaft alignment and lubrication.",
        "Known bearing damage combined with excessive vibration supports suspected bearing failure.",
        "high"
    ),

    (
        ["gearbox_oil_leakage", "gearbox_mounting_looseness"],
        "possible_gearbox_seal_failure",
        "Inspect mounting surfaces, fasteners and seals. Correct mounting issues before operation.",
        "Loose mounting may contribute to vibration and sealing problems.",
        "medium"
    )
])


# ============================================================
# CATEGORY 3: BEARINGS (R021-R030)
# ============================================================

add_category("bearings", [

    (
        ["bearing_overheating", "bearing_excessive_noise"],
        "possible_bearing_failure",
        "Stop the equipment if the bearing is severely overheating. Arrange inspection and replacement if damaged.",
        "High temperature and abnormal noise may indicate bearing damage.",
        "high"
    ),

    (
        ["bearing_excessive_vibration", "bearing_grinding_sound"],
        "possible_bearing_wear",
        "Inspect bearing rolling elements and raceways for wear and surface damage.",
        "Vibration combined with grinding noise may indicate internal bearing wear.",
        "high"
    ),

    (
        ["bearing_grease_leakage", "bearing_overheating"],
        "possible_bearing_lubrication_failure",
        "Inspect grease condition, seals and lubrication quantity. Apply the correct lubricant according to specifications.",
        "Grease leakage and overheating may indicate a lubrication or sealing problem.",
        "high"
    ),

    (
        ["bearing_metallic_particles", "bearing_surface_damage"],
        "possible_bearing_contamination_fault",
        "Inspect the bearing and housing for contamination. Clean or replace components using approved maintenance procedures.",
        "Metal particles and surface damage may indicate contamination-related deterioration.",
        "high"
    ),

    (
        ["bearing_corrosion_marks", "bearing_irregular_rotation"],
        "possible_bearing_contamination_fault",
        "Inspect for moisture ingress and corrosion. Replace severely corroded bearings.",
        "Corrosion may interfere with smooth bearing rotation.",
        "medium"
    ),

    (
        ["bearing_excessive_play", "bearing_loose_fitting"],
        "possible_bearing_wear",
        "Measure bearing clearance and inspect the shaft and housing fit.",
        "Excessive play and loose fitting may indicate wear or incorrect installation.",
        "medium"
    ),

    (
        ["bearing_seizure", "bearing_overheating"],
        "possible_bearing_failure",
        "Stop the machine immediately and isolate it. Have the bearing and connected shaft inspected.",
        "A seized and overheating bearing indicates a potentially serious mechanical failure.",
        "critical"
    ),

    (
        ["bearing_repeated_failure", "bearing_improper_installation"],
        "possible_bearing_misalignment",
        "Review installation procedures, shaft alignment, bearing fit and applied loads.",
        "Repeated failures may result from improper installation or misalignment.",
        "high"
    ),

    (
        ["bearing_unstable_temperature", "bearing_excessive_vibration"],
        "possible_bearing_lubrication_failure",
        "Inspect lubrication quantity, bearing clearance and mechanical alignment.",
        "Temperature instability and vibration may indicate lubrication or mechanical problems.",
        "medium"
    ),

    (
        ["bearing_surface_damage", "bearing_fatigue"],
        "possible_bearing_wear",
        "Arrange a detailed bearing inspection and replace components showing fatigue damage.",
        "Surface damage and fatigue are indicators of bearing deterioration.",
        "high"
    )
])


# ============================================================
# CATEGORY 4: CONVEYOR SYSTEMS (R031-R040)
# ============================================================

add_category("conveyor_systems", [

    (
        ["conveyor_belt_slipping", "conveyor_slow_movement"],
        "possible_belt_tension_fault",
        "Inspect belt tension, drive roller condition and material loading. Adjust tension according to manufacturer instructions.",
        "Slipping and slow movement may indicate insufficient belt tension.",
        "medium"
    ),

    (
        ["conveyor_belt_misalignment", "conveyor_tracking_problem"],
        "possible_conveyor_alignment_fault",
        "Inspect idlers, pulleys and conveyor frame alignment. Adjust belt tracking using the approved procedure.",
        "Belt misalignment and unstable tracking indicate a possible alignment problem.",
        "medium"
    ),

    (
        ["conveyor_roller_jamming", "conveyor_abnormal_noise"],
        "possible_conveyor_bearing_failure",
        "Inspect roller bearings and remove obstructions after safely isolating the conveyor.",
        "Jammed rollers and abnormal noise may indicate damaged roller bearings.",
        "high"
    ),

    (
        ["conveyor_complete_stoppage", "conveyor_motor_overheating"],
        "possible_conveyor_drive_failure",
        "Inspect the drive motor, gearbox and overload protection. Do not repeatedly restart the system.",
        "Complete stoppage with motor overheating may indicate drive failure or overload.",
        "high"
    ),

    (
        ["conveyor_material_spillage", "conveyor_belt_misalignment"],
        "possible_conveyor_alignment_fault",
        "Check belt tracking, loading position and conveyor frame alignment.",
        "An incorrectly tracked belt may cause material spillage.",
        "medium"
    ),

    (
        ["conveyor_belt_tear", "conveyor_abnormal_heat"],
        "possible_conveyor_drive_failure",
        "Stop and isolate the conveyor. Inspect the belt, rollers and drive system before replacing damaged components.",
        "Belt damage and abnormal heat may indicate excessive friction or drive problems.",
        "high"
    ),

    (
        ["conveyor_overloading", "conveyor_slow_movement"],
        "possible_conveyor_drive_failure",
        "Compare material loading with conveyor capacity and inspect the drive motor and transmission.",
        "Excessive material loading can reduce conveyor speed and overload the drive.",
        "high"
    ),

    (
        ["conveyor_chain_looseness", "conveyor_irregular_speed"],
        "possible_conveyor_drive_failure",
        "Inspect chain tension, sprockets and drive components. Adjust or replace worn parts.",
        "Loose drive chains may cause inconsistent conveyor movement.",
        "medium"
    ),

    (
        ["conveyor_roller_jamming", "conveyor_excessive_vibration"],
        "possible_conveyor_bearing_failure",
        "Isolate the conveyor and inspect jammed rollers, bearings and mounting points.",
        "Roller jamming combined with vibration may indicate mechanical bearing problems.",
        "high"
    ),

    (
        ["conveyor_material_jamming", "conveyor_complete_stoppage"],
        "possible_conveyor_blockage",
        "Stop and isolate the conveyor before removing obstructing material. Inspect the transfer points.",
        "Material obstruction may prevent the conveyor from moving.",
        "high"
    )
])


# ============================================================
# CATEGORY 5: HYDRAULIC SYSTEMS (R041-R050)
# ============================================================

add_category("hydraulic_systems", [

    (
        ["hydraulic_low_pressure", "hydraulic_slow_actuator"],
        "possible_hydraulic_pump_failure",
        "Have a qualified technician inspect pump performance, fluid level and pressure readings.",
        "Low pressure and slow actuator movement may indicate inadequate pump output.",
        "high"
    ),

    (
        ["hydraulic_fluid_leakage", "hydraulic_pressure_fluctuation"],
        "possible_hydraulic_leakage_fault",
        "Isolate the hydraulic system safely and inspect hoses, fittings and seals. Never search for high-pressure leaks using bare hands.",
        "Fluid leakage may cause unstable hydraulic pressure.",
        "high"
    ),

    (
        ["hydraulic_overheating", "hydraulic_fluid_discoloration"],
        "possible_hydraulic_pressure_fault",
        "Check fluid condition, cooling performance and operating pressure. Replace degraded fluid according to specifications.",
        "High temperature and discolored fluid may indicate fluid degradation or abnormal operating conditions.",
        "high"
    ),

    (
        ["hydraulic_pump_noise", "hydraulic_air_ingress"],
        "possible_hydraulic_pump_failure",
        "Inspect the pump inlet, reservoir level and suction connections for air ingress.",
        "Air entering the hydraulic system may cause pump noise and cavitation-like symptoms.",
        "high"
    ),

    (
        ["hydraulic_filter_blockage", "hydraulic_slow_actuator"],
        "possible_hydraulic_filter_blockage",
        "Inspect the filter indicator and replace clogged filters using the manufacturer's procedure.",
        "Restricted fluid flow caused by filter blockage can slow actuator movement.",
        "medium"
    ),

    (
        ["hydraulic_cylinder_drift", "hydraulic_jerky_motion"],
        "possible_hydraulic_valve_failure",
        "Inspect directional and control valves and cylinder seals for internal leakage.",
        "Uncontrolled cylinder movement and jerky operation may indicate valve or seal problems.",
        "high"
    ),

    (
        ["hydraulic_weak_force", "hydraulic_low_pressure"],
        "possible_hydraulic_pressure_fault",
        "Check pressure settings, relief valve operation, pump output and fluid level.",
        "Low pressure can reduce the force generated by hydraulic actuators.",
        "high"
    ),

    (
        ["hydraulic_foaming", "hydraulic_system_vibration"],
        "possible_hydraulic_pump_failure",
        "Inspect reservoir fluid level, suction line connections and air contamination.",
        "Foaming may indicate air entering the fluid, which can contribute to unstable operation.",
        "medium"
    ),

    (
        ["hydraulic_actuator_stoppage", "hydraulic_valve_malfunction"],
        "possible_hydraulic_valve_failure",
        "Inspect the control valve, electrical control signal and hydraulic flow path.",
        "A malfunctioning valve may interrupt actuator movement.",
        "high"
    ),

    (
        ["hydraulic_fluid_contamination", "hydraulic_filter_blockage"],
        "possible_hydraulic_filter_blockage",
        "Inspect the contamination source, replace affected filters and restore fluid cleanliness.",
        "Contaminated hydraulic fluid can clog filters and restrict system flow.",
        "medium"
    )
])


# ============================================================
# CATEGORY 6: COMPRESSORS (R051-R060)
# ============================================================

add_category("compressors", [

    (
        ["compressor_overheating", "compressor_low_pressure"],
        "possible_compressor_overheating_fault",
        "Inspect cooling airflow, filters, lubrication and operating pressure.",
        "Overheating combined with low pressure may indicate restricted airflow or compressor performance problems.",
        "high"
    ),

    (
        ["compressor_air_leakage", "compressor_slow_pressure_build"],
        "possible_compressor_air_leakage",
        "Inspect pipe connections, hoses, fittings and storage tank connections for leaks.",
        "Air leakage can prevent the system from building pressure at the expected rate.",
        "medium"
    ),

    (
        ["compressor_excessive_noise", "compressor_excessive_vibration"],
        "possible_compressor_motor_failure",
        "Inspect mounting, drive coupling, bearings and motor condition.",
        "Abnormal noise and vibration may indicate mechanical or motor-related problems.",
        "high"
    ),

    (
        ["compressor_oil_leakage", "compressor_oil_contamination"],
        "possible_compressor_overheating_fault",
        "Inspect oil seals, lubricant condition and operating temperature.",
        "Oil leakage and contamination may contribute to inadequate lubrication and overheating.",
        "high"
    ),

    (
        ["compressor_fails_to_start", "compressor_high_current"],
        "possible_compressor_motor_failure",
        "Have a qualified electrician inspect the motor, starting circuit and electrical protection.",
        "Failure to start with excessive current may indicate motor or starting circuit problems.",
        "high"
    ),

    (
        ["compressor_low_airflow", "compressor_air_filter_blockage"],
        "possible_compressor_pressure_fault",
        "Inspect the air intake filter and replace it if blocked.",
        "A restricted air intake can reduce compressor airflow.",
        "medium"
    ),

    (
        ["compressor_pressure_fluctuation", "compressor_pressure_switch_fault"],
        "possible_compressor_pressure_fault",
        "Have a technician inspect the pressure switch, pressure sensor and control settings.",
        "A defective pressure switch may cause unstable pressure control.",
        "medium"
    ),

    (
        ["compressor_water_discharge", "compressor_moisture_accumulation"],
        "possible_compressor_pressure_fault",
        "Inspect the moisture separator, condensate drain and air dryer.",
        "Moisture accumulation may indicate inadequate condensate removal or drying.",
        "medium"
    ),

    (
        ["compressor_frequent_shutdown", "compressor_overheating"],
        "possible_compressor_overheating_fault",
        "Inspect cooling filters, ventilation and thermal protection. Allow safe cooling before further operation.",
        "Repeated shutdown with high temperature may indicate thermal protection activation.",
        "high"
    ),

    (
        ["compressor_low_pressure", "compressor_valve_damage"],
        "possible_compressor_valve_failure",
        "Arrange inspection of compressor inlet and discharge valves.",
        "Damaged compressor valves can reduce compression efficiency and output pressure.",
        "high"
    )
])


# ============================================================
# CATEGORY 7: ELECTRICAL SYSTEMS (R061-R070)
# ============================================================

add_category("electrical_systems", [

    (
        ["electrical_voltage_drop", "electrical_unstable_supply"],
        "possible_electrical_connection_failure",
        "Have a qualified electrician inspect incoming supply connections, cable condition and voltage measurements.",
        "Voltage drops and unstable supply may indicate poor electrical connections or supply problems.",
        "high"
    ),

    (
        ["electrical_circuit_breaker_tripping", "electrical_overloading"],
        "possible_electrical_overload",
        "Check circuit load against its rated capacity and inspect protective devices.",
        "Excessive electrical load may cause repeated circuit breaker trips.",
        "high"
    ),

    (
        ["electrical_fuse_blowing", "electrical_short_circuit"],
        "possible_electrical_short_circuit",
        "Keep the circuit isolated and arrange fault tracing by a qualified electrician before replacing the fuse.",
        "A short circuit can cause excessive current and repeated fuse failure.",
        "critical"
    ),

    (
        ["electrical_panel_overheating", "electrical_loose_wiring"],
        "possible_electrical_connection_failure",
        "Isolate the panel according to electrical safety procedures. Have connections inspected and tightened by a qualified electrician.",
        "Loose electrical connections can generate resistance heating.",
        "high"
    ),

    (
        ["electrical_phase_loss", "electrical_phase_imbalance"],
        "possible_electrical_phase_fault",
        "Have a qualified electrician inspect all supply phases, protective devices and connections.",
        "Missing or unbalanced phases may cause abnormal three-phase equipment operation.",
        "critical"
    ),

    (
        ["electrical_burning_smell", "electrical_sparking"],
        "possible_electrical_control_fault",
        "Immediately isolate the affected equipment if safe to do so. Do not touch the panel until it has been made electrically safe.",
        "Burning odor and sparking may indicate dangerous electrical damage.",
        "critical"
    ),

    (
        ["electrical_ground_fault", "electrical_insulation_damage"],
        "possible_electrical_short_circuit",
        "Keep the equipment isolated and arrange insulation resistance and ground-fault testing by a qualified electrician.",
        "Insulation damage may allow unintended current flow to ground.",
        "critical"
    ),

    (
        ["electrical_relay_malfunction", "electrical_control_failure"],
        "possible_electrical_control_fault",
        "Inspect relay operation, control wiring and control circuit signals.",
        "Relay malfunction can interrupt machine control functions.",
        "medium"
    ),

    (
        ["electrical_contact_failure", "electrical_control_failure"],
        "possible_electrical_connection_failure",
        "Inspect contactors, terminal connections and control circuit continuity.",
        "Poor electrical contacts may prevent reliable control circuit operation.",
        "medium"
    ),

    (
        ["electrical_power_failure", "electrical_supply_fault"],
        "possible_electrical_phase_fault",
        "Have a qualified electrician verify incoming power, isolators, fuses and supply continuity.",
        "An incoming electrical supply fault may prevent the machine from receiving power.",
        "high"
    )
])


# ============================================================
# CATEGORY 8: CNC MACHINES (R071-R080)
# ============================================================

add_category("cnc_machines", [

    (
        ["cnc_spindle_overheating", "cnc_spindle_noise"],
        "possible_cnc_spindle_failure",
        "Stop machining and arrange inspection of spindle bearings, lubrication and cooling.",
        "Spindle overheating and abnormal noise may indicate spindle bearing or mechanical problems.",
        "high"
    ),

    (
        ["cnc_tool_wear", "cnc_surface_finish_defect"],
        "possible_cnc_tool_wear_fault",
        "Inspect cutting tool condition and replace worn tools using the approved tool-change procedure.",
        "Worn cutting tools can produce poor surface finishes.",
        "medium"
    ),

    (
        ["cnc_positioning_error", "cnc_machine_accuracy_loss"],
        "possible_cnc_positioning_fault",
        "Inspect axis calibration, encoder feedback and machine alignment according to manufacturer procedures.",
        "Positioning errors and reduced accuracy may indicate calibration or feedback problems.",
        "high"
    ),

    (
        ["cnc_axis_movement_failure", "cnc_servo_motor_fault"],
        "possible_cnc_axis_fault",
        "Have a qualified technician inspect the servo motor, drive, feedback system and axis mechanics.",
        "Servo motor faults may prevent correct axis movement.",
        "high"
    ),

    (
        ["cnc_coolant_flow_problem", "cnc_coolant_blockage"],
        "possible_cnc_coolant_failure",
        "Inspect coolant filters, pumps and delivery passages. Restore flow using approved maintenance procedures.",
        "Blocked coolant passages may restrict coolant delivery.",
        "medium"
    ),

    (
        ["cnc_excessive_vibration", "cnc_spindle_noise"],
        "possible_cnc_spindle_failure",
        "Inspect spindle bearings, tool holder condition and machine mounting.",
        "Vibration and spindle noise may indicate spindle mechanical deterioration.",
        "high"
    ),

    (
        ["cnc_tool_breakage", "cnc_feed_rate_problem"],
        "possible_cnc_tool_wear_fault",
        "Review feed rate, cutting parameters, tool condition and material specifications.",
        "Incorrect feed settings and worn tools may contribute to cutting tool breakage.",
        "medium"
    ),

    (
        ["cnc_program_execution_error", "cnc_power_supply_fault"],
        "possible_cnc_axis_fault",
        "Check machine alarms, power supply condition and control system diagnostics before restarting.",
        "Power supply problems can interfere with CNC control and program execution.",
        "high"
    ),

    (
        ["cnc_tool_changer_failure", "cnc_unexpected_shutdown"],
        "possible_cnc_axis_fault",
        "Inspect tool changer mechanisms, control alarms and interlock conditions with the machine isolated as required.",
        "A tool changer fault or interlock problem may interrupt machine operation.",
        "high"
    ),

    (
        ["cnc_spindle_speed_fluctuation", "cnc_spindle_overheating"],
        "possible_cnc_spindle_failure",
        "Inspect spindle drive, cooling, bearings and speed feedback system.",
        "Unstable spindle speed and overheating may indicate a spindle drive or mechanical problem.",
        "high"
    )
])


# ============================================================
# CATEGORY 9: COOLING SYSTEMS (R081-R090)
# ============================================================

add_category("cooling_systems", [

    (
        ["cooling_high_temperature", "cooling_low_flow"],
        "possible_cooling_flow_fault",
        "Inspect coolant circulation, pump operation and pipe restrictions.",
        "Insufficient coolant flow can reduce heat removal and increase temperature.",
        "high"
    ),

    (
        ["cooling_fluid_leakage", "cooling_pressure_drop"],
        "possible_cooling_refrigerant_fault",
        "Inspect the circuit for leaks and have refrigerant systems serviced by qualified personnel.",
        "Fluid leakage may cause cooling pressure to decrease.",
        "high"
    ),

    (
        ["cooling_pump_noise", "cooling_excessive_vibration"],
        "possible_cooling_pump_failure",
        "Inspect pump bearings, mounting, inlet conditions and alignment.",
        "Pump noise combined with vibration may indicate mechanical pump damage.",
        "high"
    ),

    (
        ["cooling_fan_failure", "cooling_high_temperature"],
        "possible_cooling_fan_failure",
        "Inspect the cooling fan, motor, power supply and ventilation path.",
        "A failed cooling fan may reduce heat dissipation.",
        "high"
    ),

    (
        ["cooling_filter_blockage", "cooling_low_flow"],
        "possible_cooling_flow_fault",
        "Inspect and replace clogged filters according to the cooling system maintenance procedure.",
        "A blocked filter can restrict cooling fluid circulation.",
        "medium"
    ),

    (
        ["cooling_heat_exchanger_overheating", "cooling_temperature_fluctuation"],
        "possible_cooling_heat_exchanger_fault",
        "Inspect heat exchanger surfaces, coolant flow and temperature sensors.",
        "Heat exchanger fouling or restricted flow may reduce heat transfer performance.",
        "high"
    ),

    (
        ["cooling_compressor_failure", "cooling_high_temperature"],
        "possible_cooling_refrigerant_fault",
        "Arrange inspection of the compressor, refrigerant circuit and temperature controls.",
        "Cooling compressor failure can prevent effective heat removal.",
        "high"
    ),

    (
        ["cooling_uneven_distribution", "cooling_pipe_blockage"],
        "possible_cooling_flow_fault",
        "Inspect distribution pipes, valves and flow balancing.",
        "Blocked pipes may cause uneven cooling distribution.",
        "medium"
    ),

    (
        ["cooling_frequent_shutdown", "cooling_thermostat_failure"],
        "possible_cooling_heat_exchanger_fault",
        "Inspect thermostat readings, temperature sensors and system protection settings.",
        "Faulty temperature control may cause unnecessary shutdowns.",
        "medium"
    ),

    (
        ["cooling_refrigerant_leak", "cooling_pressure_drop"],
        "possible_cooling_refrigerant_fault",
        "Have a qualified refrigeration technician locate the leak, repair it and verify the refrigerant charge.",
        "Refrigerant leakage can cause cooling circuit pressure to drop.",
        "high"
    )
])


# ============================================================
# CATEGORY 10: GENERAL MECHANICAL FAULTS (R091-R100)
# ============================================================

add_category("general_mechanical_faults", [

    (
        ["machine_excessive_vibration", "machine_unbalanced_rotation"],
        "possible_mechanical_imbalance",
        "Inspect rotating components and arrange balancing according to machine specifications.",
        "Excessive vibration with unbalanced rotation suggests a rotating component imbalance.",
        "high"
    ),

    (
        ["machine_abnormal_noise", "machine_component_looseness"],
        "possible_mechanical_wear",
        "Inspect mechanical fasteners, mounting points and worn components.",
        "Loose components may produce abnormal operating noise.",
        "medium"
    ),

    (
        ["machine_overheating", "machine_excessive_friction"],
        "possible_mechanical_lubrication_failure",
        "Inspect lubrication points, friction surfaces and operating clearances.",
        "Excessive friction can generate heat when lubrication is inadequate.",
        "high"
    ),

    (
        ["machine_alignment_problem", "machine_shaft_noise"],
        "possible_mechanical_misalignment",
        "Check shaft alignment, coupling condition and mounting stability.",
        "Shaft noise and alignment problems may indicate mechanical misalignment.",
        "high"
    ),

    (
        ["machine_power_loss", "machine_excessive_wear"],
        "possible_mechanical_wear",
        "Inspect mechanical transmission components, friction surfaces and worn parts.",
        "Worn mechanical components may reduce power transmission efficiency.",
        "medium"
    ),

    (
        ["machine_repeated_jamming", "machine_irregular_movement"],
        "possible_mechanical_wear",
        "Safely isolate the equipment and inspect moving components for obstruction, wear and deformation.",
        "Repeated jamming and irregular movement may indicate damaged or obstructed mechanical components.",
        "high"
    ),

    (
        ["machine_component_looseness", "machine_excessive_vibration"],
        "possible_mechanical_misalignment",
        "Inspect fasteners, machine mounting and alignment using approved maintenance procedures.",
        "Loose mounting and vibration may be associated with mechanical instability or misalignment.",
        "high"
    ),

    (
        ["machine_reduced_efficiency", "machine_excessive_friction"],
        "possible_mechanical_lubrication_failure",
        "Inspect lubrication condition, friction surfaces and mechanical clearances.",
        "Excessive friction can reduce overall mechanical efficiency.",
        "medium"
    ),

    (
        ["machine_unexpected_stoppage", "machine_shaft_noise"],
        "possible_mechanical_wear",
        "Stop and isolate the equipment. Inspect the shaft, bearings and connected transmission components.",
        "Shaft noise and unexpected stoppage may indicate a serious mechanical problem.",
        "high"
    ),

    (
        ["machine_excessive_wear", "machine_alignment_problem"],
        "possible_mechanical_misalignment",
        "Inspect alignment, shaft condition and component wear. Correct alignment before returning equipment to service.",
        "Misalignment may accelerate mechanical wear.",
        "high"
    )
])


# ============================================================
# ADDITIONAL COVERAGE RULES (R101-R102)
# These rules cover diagnoses that previously had no supporting rule.
# ============================================================

add_category("electric_motors", [
    (
        ["motor_overheating", "motor_cooling_blockage"],
        "possible_motor_cooling_failure",
        "Shut down the motor if its temperature exceeds safe operating limits. Have a qualified technician inspect cooling passages, fan operation and ventilation before restarting.",
        "Motor overheating together with a confirmed blockage in its cooling passages supports a possible motor cooling failure.",
        "high"
    )
])

add_category("general_mechanical_faults", [
    (
        ["machine_power_loss", "mechanical_overloading"],
        "possible_mechanical_overload",
        "Reduce the load using the approved operating procedure and have a qualified technician verify the machine rating, load and drive condition before returning it to service.",
        "Machine power loss together with a confirmed condition of operating above the rated load supports a possible mechanical overload.",
        "high"
    )
])


# ============================================================
# ADDITIONAL ELECTRIC MOTOR DIAGNOSTIC RULES (R103-R109)
# ============================================================

add_category("electric_motors", [

    # R103: Bearing wear
    (
        ["motor_bearing_wear", "motor_excessive_vibration"],
        "possible_motor_bearing_failure",
        "Stop the motor if vibration is severe. Have a qualified technician inspect bearing condition, clearances and mounting.",
        "Reported bearing wear together with excessive motor vibration supports a possible bearing failure.",
        "high"
    ),

    # R104: Bearing lubrication failure
    (
        ["motor_lubrication_failure", "motor_unusual_noise"],
        "possible_motor_bearing_failure",
        "Inspect the bearing lubrication system and use the lubricant specified by the motor manufacturer. Check for bearing damage before restarting.",
        "Insufficient bearing lubrication together with unusual operating noise supports a possible bearing problem.",
        "high"
    ),

    # R105: Winding damage
    (
        ["motor_winding_damage", "motor_smoke_emission"],
        "possible_motor_winding_failure",
        "Disconnect the motor from its power supply. Have a qualified technician inspect the windings and insulation before restarting.",
        "Reported winding damage together with smoke emission supports a possible motor winding failure.",
        "critical"
    ),

    # R106: Insulation failure
    (
        ["motor_insulation_failure", "motor_burning_smell"],
        "possible_motor_winding_failure",
        "Disconnect the motor safely and arrange insulation resistance and winding tests by a qualified technician.",
        "Deteriorated winding insulation together with a burning smell supports a possible winding failure.",
        "critical"
    ),

    # R107: Motor overloading
    (
        ["motor_overloading", "motor_excessive_current"],
        "possible_motor_overload_fault",
        "Reduce the motor load to its rated operating limit. Have a technician check the motor current, load and protection settings.",
        "Reported operation above the rated load together with excessive current supports a possible motor overload.",
        "high"
    ),

    # R108: Three-phase imbalance
    (
        ["motor_phase_imbalance", "motor_abnormal_voltage"],
        "possible_motor_electrical_fault",
        "Have a qualified electrician measure all three-phase voltages and inspect the supply connections and phase balance.",
        "A reported three-phase imbalance together with abnormal supply voltage supports a possible electrical fault.",
        "high"
    ),

    # R109: Loose electrical connections
    (
        ["motor_loose_connections", "motor_intermittent_operation"],
        "possible_motor_electrical_fault",
        "Isolate the motor safely and have a qualified electrician inspect and tighten electrical connections according to manufacturer specifications.",
        "Reported loose electrical connections together with intermittent motor operation support a possible electrical fault.",
        "high"
    )

])

# ============================================================
# KNOWLEDGE BASE VALIDATION
# ============================================================

# Import the 300 assertions
try:
    from knowledge_base.assertions import ASSERTIONS
except ImportError:
    from assertions import ASSERTIONS


# Total rules
TOTAL_RULES = len(RULES)

# Unique rule IDs
RULE_IDS = [rule["id"] for rule in RULES]

# Category-wise rule counts
CATEGORY_COUNTS = {}

for rule in RULES:
    category = rule["category"]
    CATEGORY_COUNTS[category] = CATEGORY_COUNTS.get(category, 0) + 1


# Build assertion lookup
ASSERTION_LOOKUP = {
    assertion["name"]: assertion
    for assertion in ASSERTIONS
}


# Validate rule conditions and conclusions
for rule in RULES:

    # Every condition must exist in assertions.py
    for condition in rule["conditions"]:
        assert condition in ASSERTION_LOOKUP, (
            f"Unknown condition '{condition}' in {rule['id']}"
        )

        # Conditions may be symptoms or technician-confirmed causes
        assert ASSERTION_LOOKUP[condition]["type"] in ["symptom", "cause"], (
            f"Invalid condition type in {rule['id']}"
        )

    # Diagnosis must exist in assertions.py
    assert rule["diagnosis"] in ASSERTION_LOOKUP, (
        f"Unknown diagnosis '{rule['diagnosis']}' in {rule['id']}"
    )

    # Conclusion must have diagnosis type
    assert ASSERTION_LOOKUP[rule["diagnosis"]]["type"] == "diagnosis", (
        f"Invalid diagnosis type in {rule['id']}"
    )

    # Validate severity
    assert rule["severity"] in ["low", "medium", "high", "critical"], (
        f"Invalid severity in {rule['id']}"
    )


# Final checks
assert TOTAL_RULES == 109, "Total rules must equal 109!"
assert len(set(RULE_IDS)) == 109, "Duplicate rule IDs found!"
assert len(CATEGORY_COUNTS) == 10, "There must be 10 categories!"
EXPECTED_CATEGORY_COUNTS = {
    "electric_motors": 18,
    "gearboxes": 10,
    "bearings": 10,
    "conveyor_systems": 10,
    "hydraulic_systems": 10,
    "compressors": 10,
    "electrical_systems": 10,
    "cnc_machines": 10,
    "cooling_systems": 10,
    "general_mechanical_faults": 11,
}
assert CATEGORY_COUNTS == EXPECTED_CATEGORY_COUNTS, (
    f"Unexpected category rule counts: {CATEGORY_COUNTS}"
)

# Every diagnosis assertion must be reachable by at least one rule.
RULE_DIAGNOSES = {rule["diagnosis"] for rule in RULES}
UNUSED_DIAGNOSES = {
    assertion["name"]
    for assertion in ASSERTIONS
    if assertion["type"] == "diagnosis" and assertion["name"] not in RULE_DIAGNOSES
}
assert not UNUSED_DIAGNOSES, f"Diagnoses without rules: {sorted(UNUSED_DIAGNOSES)}"


# ============================================================
# DISPLAY VALIDATION RESULTS
# ============================================================

print("==========================================")
print("INDUSTRIAL MACHINE EXPERT SYSTEM")
print("RULE BASE VALIDATION")
print("==========================================")

print("Total Rules:", TOTAL_RULES)
print("Total Assertions:", len(ASSERTIONS))
print("Total Categories:", len(CATEGORY_COUNTS))

print("\nCategory-wise Rule Count:")

for category, count in CATEGORY_COUNTS.items():
    print(category, ":", count)

print("\nAll rule conditions are valid.")
print("All diagnoses are valid.")
print("All rule IDs are unique.")
print("All category rule counts match the expected distribution.")
print("All diagnosis assertions are covered by at least one rule.")

print("\nKnowledge Base loaded successfully!")
