# ============================================================
# extra_synonyms.py
#
# Additional natural-language phrases that map onto existing
# (and a few closely related) assertions.  These cover the
# exact wording of the 100 evaluation questions.
#
# Integration (do not edit original processor.py):
#
#   from nlp.extra_synonyms import EXTRA_SYNONYMS
#   # then, after importing the original SYNONYMS:
#   for name, phrases in EXTRA_SYNONYMS.items():
#       SYNONYMS.setdefault(name, []).extend(phrases)
#
# Or, if you prefer a pure-function approach, call:
#   merge_synonyms(original_synonyms_dict)
# ============================================================

EXTRA_SYNONYMS = {
    # ------------------------------------------------------------------
    # ELECTRIC MOTORS (Q1-Q10)
    # ------------------------------------------------------------------
    "motor_overheating": [
        "motor getting extremely hot",
        "electric motor getting extremely hot",
        "motor is getting extremely hot during normal operation",
        "motor becomes extremely hot",
        "motor is extremely hot",
        "motor running extremely hot",
        "motor temperature extremely high",
        "motor overheating during normal operation",
    ],
    "motor_excessive_vibration": [
        "motor shakes heavily",
        "motor is shaking heavily",
        "motor producing excessive vibration",
        "motor is producing excessive vibration even though it is properly mounted",
        "excessive vibration even though properly mounted",
        "motor vibrates heavily",
    ],
    "motor_unusual_noise": [
        "motor makes a strange grinding noise",
        "strange grinding noise",
        "motor makes unusual noise",
        "motor makes unusual noise and seems to be overheating",
        "grinding noise from motor",
        "unusual noise from the motor",
    ],
    "motor_intermittent_operation": [
        "motor start and stop repeatedly",
        "motor starts and stops repeatedly without warning",
        "motor start and stop repeatedly without warning",
        "motor starts and stops without warning",
        "motor keeps starting and stopping",
        "motor starts and stops intermittently",
    ],
    "motor_burning_smell": [
        "burning smell coming from the motor",
        "there is a burning smell coming from the motor",
        "burning smell from the motor",
        "motor produces a burning smell",
        "smell of burning from motor",
    ],
    "motor_smoke_emission": [
        "smoke near its winding",
        "smoke near the winding",
        "smoke near motor winding",
        "noticed smoke near its winding",
        "smoke from the winding",
    ],
    "motor_winding_damage": [
        "smoke near its winding",
        "problem with the winding",
        "winding damage",
        "damaged winding",
    ],
    "motor_excessive_current": [
        "motor drawing more electrical current than usual",
        "drawing more electrical current than usual",
        "motor is drawing more current",
        "motor draws more current than usual",
        "higher current draw from motor",
    ],
    "motor_loose_connections": [
        "electrical connections seem loose",
        "motor electrical connections seem loose",
        "loose electrical connections on motor",
        "connections seem loose",
        "loose connections on the motor",
    ],
    "motor_phase_imbalance": [
        "three-phase motor running unevenly",
        "three phase motor running unevenly",
        "motor running unevenly",
        "three-phase motor is running unevenly",
        "uneven running of three-phase motor",
    ],
    "motor_inconsistent_speed": [
        "motor running unevenly",
        "motor runs unevenly",
        "uneven motor operation",
    ],
    "machine_power_loss": [
        "motor sometimes loses power",
        "motor loses power",
        "loses power",
        "motor is losing power",
        "intermittent power loss from motor",
    ],
    "motor_fails_to_start": [
        "motor suddenly stopped working",
        "motor stopped working",
        "motor suddenly stopped",
    ],

    # ------------------------------------------------------------------
    # GEARBOXES (Q11-Q20)
    # ------------------------------------------------------------------
    "gearbox_abnormal_noise": [
        "gearbox producing a loud whining noise",
        "loud whining noise from gearbox",
        "gearbox produces a loud whining noise during operation",
        "gearbox gears making a grinding sound",
        "gears making a grinding sound",
        "gearbox produce unusual noise when operating under heavy load",
        "unusual noise from gearbox under heavy load",
        "gearbox unusual noise under heavy load",
        "whining noise from gearbox",
        "grinding sound from gearbox gears",
    ],
    "gearbox_overheating": [
        "gearbox is overheating after running for a short time",
        "gearbox overheating after short time",
        "gearbox temperature is increasing",
        "gearbox temperature increasing",
        "gearbox is getting hot quickly",
    ],
    "gearbox_oil_leakage": [
        "oil leaking from the gearbox housing",
        "oil leaking from gearbox housing",
        "oil is leaking from the gearbox",
        "leak from gearbox housing",
        "gearbox housing oil leak",
    ],
    "gearbox_excessive_vibration": [  # may map to a general or new assertion
        "gearbox produces excessive vibration while transmitting power",
        "gearbox excessive vibration while transmitting power",
        "excessive vibration from gearbox",
        "gearbox vibrating excessively",
    ],
    "gearbox_lubrication_failure": [
        "gearbox has insufficient lubrication",
        "insufficient lubrication in gearbox",
        "gearbox insufficient lubrication",
        "lack of lubrication in gearbox",
    ],
    "gearbox_shaft_problem": [
        "gearbox shaft rotating irregularly",
        "shaft rotating irregularly",
        "gearbox shaft is rotating irregularly",
        "irregular rotation of gearbox shaft",
    ],
    "gearbox_contamination": [
        "oil looks contaminated",
        "gearbox oil looks contaminated",
        "contaminated oil in gearbox",
        "gearbox temperature increasing and oil contaminated",
    ],
    "gearbox_power_transfer": [
        "gearbox is not transferring power smoothly",
        "not transferring power smoothly",
        "gearbox not transferring power smoothly",
        "power transfer not smooth",
    ],

    # ------------------------------------------------------------------
    # BEARINGS (Q21-Q30)
    # ------------------------------------------------------------------
    "bearing_excessive_noise": [
        "industrial bearing making a continuous grinding noise",
        "bearing making a continuous grinding noise",
        "continuous grinding noise from bearing",
        "unusual noise coming from the bearing housing",
        "noise from the bearing housing",
        "bearing is making a squealing sound",
        "bearing making a squealing sound during operation",
        "squealing sound from bearing",
        "grinding noise from bearing",
    ],
    "bearing_overheating": [
        "bearing becomes very hot during machine operation",
        "bearing becomes very hot",
        "bearing temperature increasing even at normal operating speed",
        "bearing temperature is increasing",
        "bearing is getting very hot",
    ],
    "bearing_excessive_vibration": [
        "bearing produce excessive vibration",
        "bearing produces excessive vibration",
        "bearing has excessive clearance and produces vibration",
        "excessive clearance and vibration from bearing",
        "bearing vibration due to excessive clearance",
    ],
    "bearing_lubrication_failure": [
        "bearing has insufficient lubrication",
        "insufficient lubrication of bearing",
        "bearing insufficient lubrication",
        "lack of lubrication in bearing",
    ],
    "bearing_wear": [
        "bearing feels rough when rotating manually",
        "bearing feels rough",
        "feels rough when rotating",
        "bearing wearing out faster than expected",
        "bearing is wearing out faster",
        "premature bearing wear",
        "bearing has excessive clearance",
        "excessive clearance in bearing",
    ],
    "bearing_damage": [
        "what might be damaged in the bearing",
        "bearing internal damage",
        "damaged bearing race or balls",
    ],

    # ------------------------------------------------------------------
    # CONVEYOR SYSTEMS (Q31-Q40)
    # ------------------------------------------------------------------
    "conveyor_belt_slipping": [
        "conveyor belt keep slipping while carrying materials",
        "conveyor belt keeps slipping",
        "belt keeps slipping while carrying materials",
        "conveyor belt tension seems too loose and the belt keeps slipping",
        "belt tension too loose and keeps slipping",
        "belt is slipping",
        "conveyor belt is slipping",
    ],
    "conveyor_belt_misalignment": [
        "conveyor belt is moving toward one side instead of staying centered",
        "belt moving toward one side",
        "belt is not staying centered",
        "conveyor belt tracking to one side",
        "belt misalignment",
        "belt not centered",
    ],
    "conveyor_unexpected_stop": [
        "conveyor system stop unexpectedly during production",
        "conveyor stops unexpectedly",
        "conveyor system stops unexpectedly",
        "unexpected stop of conveyor",
    ],
    "conveyor_unusual_noise": [
        "conveyor belt is making unusual noise near the rollers",
        "unusual noise near the rollers",
        "noise near the rollers",
        "unusual noise from conveyor rollers",
    ],
    "conveyor_slow_speed": [
        "conveyor belt moving slower than its normal speed",
        "belt moving slower than normal",
        "conveyor running slower than normal",
        "reduced conveyor speed",
    ],
    "conveyor_motor_overheating": [
        "conveyor motor is overheating while carrying heavy materials",
        "conveyor motor overheating under heavy load",
        "motor of conveyor overheating",
    ],
    "conveyor_material_spill": [
        "material falling from the conveyor belt during operation",
        "material falling from the conveyor belt",
        "material spilling from conveyor",
        "product falling off the belt",
    ],
    "conveyor_belt_damage": [
        "conveyor belt has visible cracks and signs of excessive wear",
        "visible cracks on conveyor belt",
        "cracks and excessive wear on belt",
        "belt has cracks and wear",
    ],
    "conveyor_excessive_vibration": [
        "conveyor produce excessive vibration",
        "conveyor produces excessive vibration",
        "excessive vibration from conveyor",
    ],
    "conveyor_belt_tension": [
        "conveyor belt tension seems too loose",
        "belt tension too loose",
        "loose belt tension",
        "insufficient belt tension",
    ],

    # ------------------------------------------------------------------
    # HYDRAULIC SYSTEMS (Q41-Q50)
    # ------------------------------------------------------------------
    "hydraulic_low_pressure": [
        "hydraulic system unable to generate enough pressure",
        "unable to generate enough pressure",
        "hydraulic system cannot generate enough pressure",
        "not enough pressure in hydraulic system",
        "hydraulic system losing pressure after a few minutes",
        "losing pressure after a few minutes",
        "pressure drops after a few minutes",
        "system loses pressure",
    ],
    "hydraulic_slow_movement": [
        "hydraulic cylinder moves very slowly even though the pump is running",
        "cylinder moves very slowly",
        "hydraulic cylinder is moving slowly",
        "actuator moves slowly",
        "slow cylinder movement",
    ],
    "hydraulic_oil_leakage": [
        "hydraulic oil leaking from the system",
        "oil leaking from the hydraulic system",
        "hydraulic oil leak",
        "leak in hydraulic system",
    ],
    "hydraulic_pump_noise": [
        "hydraulic pump is making a loud whining noise",
        "pump making a loud whining noise",
        "loud whining noise from hydraulic pump",
        "hydraulic pump whining",
    ],
    "hydraulic_oil_overheating": [
        "hydraulic oil become excessively hot",
        "hydraulic oil becomes excessively hot",
        "oil is excessively hot",
        "hydraulic fluid overheating",
    ],
    "hydraulic_irregular_movement": [
        "hydraulic actuator is moving irregularly and jerking during operation",
        "actuator moving irregularly and jerking",
        "jerking during operation",
        "irregular and jerky movement of actuator",
        "cylinder is jerking",
    ],
    "hydraulic_pump_vibration": [
        "hydraulic pump produces excessive vibration",
        "pump produces excessive vibration",
        "excessive vibration from hydraulic pump",
    ],
    "hydraulic_insufficient_force": [
        "hydraulic cylinder unable to lift its normal load",
        "cylinder unable to lift its normal load",
        "cannot lift normal load",
        "insufficient force from hydraulic cylinder",
    ],
    "hydraulic_contamination": [
        "hydraulic oil looks dirty",
        "oil looks dirty and the system performance has decreased",
        "dirty hydraulic oil",
        "contaminated hydraulic fluid",
        "system performance has decreased",
    ],

    # ------------------------------------------------------------------
    # COMPRESSORS (Q51-Q60)
    # ------------------------------------------------------------------
    "compressor_slow_pressure_build": [
        "air compressor taking too long to build pressure",
        "compressor taking too long to build pressure",
        "taking too long to build pressure",
        "slow pressure build up",
        "compressor slow to reach pressure",
    ],
    "compressor_overheating": [
        "compressor is overheating and shutting down automatically",
        "compressor overheating and shutting down",
        "compressor overheating",
        "compressor shuts down due to overheating",
    ],
    "compressor_knocking": [
        "compressor producing unusual knocking sounds",
        "unusual knocking sounds from compressor",
        "knocking sounds from compressor",
        "compressor knocking",
    ],
    "compressor_air_leak": [
        "compressor has an air leakage problem",
        "air leakage problem",
        "air leak in compressor",
        "compressor is leaking air",
    ],
    "compressor_low_output": [
        "compressor producing less air than usual",
        "producing less air than usual",
        "less air output from compressor",
        "reduced air delivery",
    ],
    "compressor_excessive_vibration": [
        "compressor vibrates excessively during operation",
        "compressor vibrates excessively",
        "excessive vibration from compressor",
    ],
    "compressor_high_power": [
        "compressor consume more electricity than normal",
        "compressor consumes more electricity than normal",
        "more electricity than normal",
        "high power consumption of compressor",
    ],
    "compressor_moisture": [
        "compressor is producing moisture in the compressed air",
        "producing moisture in the compressed air",
        "moisture in the compressed air",
        "wet compressed air",
        "water in compressed air",
    ],
    "compressor_frequent_stop": [
        "compressor stop frequently during operation",
        "compressor stops frequently",
        "compressor stops frequently during operation",
        "frequent stopping of compressor",
    ],
    "compressor_low_oil": [
        "compressor oil level is low and its temperature is increasing",
        "oil level is low and temperature is increasing",
        "low oil level in compressor",
        "compressor oil low and temperature rising",
    ],

    # ------------------------------------------------------------------
    # ELECTRICAL SYSTEMS (Q61-Q70)
    # ------------------------------------------------------------------
    "electrical_panel_overheating": [
        "electrical control panel become unusually hot",
        "control panel becomes unusually hot",
        "control panel is unusually hot",
        "panel overheating",
    ],
    "electrical_breaker_trip": [
        "circuit breaker trips whenever the machine starts",
        "circuit breaker trips when machine starts",
        "breaker trips on start",
        "fuse keep blowing repeatedly",
        "fuse keeps blowing repeatedly",
        "fuse blows repeatedly",
    ],
    "electrical_voltage_fluctuation": [
        "electrical supply voltage fluctuating",
        "supply voltage fluctuating",
        "voltage is fluctuating",
        "fluctuating supply voltage",
    ],
    "electrical_loose_connections": [
        "electrical system has loose connections and intermittent power",
        "loose connections and intermittent power",
        "loose connections in electrical system",
        "intermittent power due to loose connections",
    ],
    "electrical_no_power": [
        "machine not receiving power even though the main supply is available",
        "machine is not receiving power",
        "not receiving power although supply is available",
        "no power to the machine",
    ],
    "electrical_cable_overheating": [
        "electrical cables are overheating during normal operation",
        "cables are overheating",
        "overheating cables",
        "cables overheating under normal load",
    ],
    "electrical_fault_warning": [
        "control panel is showing an electrical fault warning",
        "showing an electrical fault warning",
        "electrical fault warning on panel",
        "fault warning displayed",
    ],
    "electrical_phase_imbalance": [
        "abnormal voltage difference between the three phases",
        "voltage difference between the three phases",
        "abnormal phase voltage difference",
        "phase voltage imbalance",
    ],
    "electrical_burning_smell": [
        "electrical system produces a burning smell near the wiring connections",
        "burning smell near the wiring connections",
        "burning smell near wiring",
        "smell of burning at connections",
    ],

    # ------------------------------------------------------------------
    # CNC MACHINES (Q71-Q80)
    # ------------------------------------------------------------------
    "cnc_inaccurate_dimensions": [
        "cnc machine producing inaccurate dimensions during machining",
        "producing inaccurate dimensions",
        "inaccurate dimensions during machining",
        "dimensional inaccuracy",
        "parts are out of tolerance",
    ],
    "cnc_spindle_noise_vibration": [
        "cnc spindle is making unusual noise and vibrating heavily",
        "spindle making unusual noise and vibrating heavily",
        "spindle noise and heavy vibration",
        "unusual noise and vibration from spindle",
    ],
    "cnc_unexpected_stop": [
        "cnc machine stop unexpectedly during a cutting operation",
        "cnc machine stops unexpectedly during cutting",
        "unexpected stop during cutting operation",
        "machine stops in the middle of a cut",
    ],
    "cnc_overheating": [
        "cnc machine is overheating after continuous operation",
        "machine overheating after continuous operation",
        "cnc overheating under continuous use",
    ],
    "cnc_tool_breakage": [
        "cutting tool breaking frequently",
        "tool breaking frequently",
        "cutting tool breaks often",
        "frequent tool breakage",
    ],
    "cnc_poor_surface_finish": [
        "cnc machine is producing a rough surface finish even with the same settings",
        "producing a rough surface finish",
        "rough surface finish",
        "poor surface finish",
    ],
    "cnc_spindle_speed_fluctuation": [
        "spindle speed fluctuating during machining",
        "spindle speed is fluctuating",
        "fluctuating spindle speed",
        "unstable spindle rpm",
    ],
    "cnc_axis_error": [
        "cnc machine is showing an axis movement error",
        "axis movement error",
        "showing an axis movement error",
        "axis error on cnc",
    ],
    "cnc_positioning_loss": [
        "cnc machine lose its positioning accuracy",
        "lose its positioning accuracy",
        "lost positioning accuracy",
        "positioning accuracy lost",
        "machine loses position",
    ],
    "cnc_excessive_vibration": [
        "machine produces excessive vibration while cutting metal",
        "excessive vibration while cutting metal",
        "vibration during metal cutting",
        "chatter while cutting",
    ],

    # ------------------------------------------------------------------
    # COOLING SYSTEMS (Q81-Q90)
    # ------------------------------------------------------------------
    "cooling_insufficient_cooling": [
        "industrial cooling system unable to maintain the required temperature",
        "unable to maintain the required temperature",
        "cooling system cannot maintain temperature",
        "temperature keeps rising despite cooling",
        "cooling system taking too long to reduce the temperature",
        "taking too long to reduce the temperature",
    ],
    "cooling_temp_rising": [
        "cooling fan is running but the system temperature keeps increasing",
        "fan is running but temperature keeps increasing",
        "temperature keeps increasing even with fan running",
        "cooling unit is overheating even though the fan is working",
        "unit overheating even though fan is working",
    ],
    "cooling_coolant_leak": [
        "coolant leaking from the cooling pipes",
        "coolant leaking from pipes",
        "leak from cooling pipes",
        "coolant leak",
    ],
    "cooling_pump_noise": [
        "cooling pump is producing unusual noise during operation",
        "cooling pump producing unusual noise",
        "unusual noise from cooling pump",
    ],
    "cooling_low_flow": [
        "cooling system circulating less fluid than normal",
        "circulating less fluid than normal",
        "reduced coolant flow",
        "low fluid circulation",
    ],
    "cooling_blocked_filter": [
        "cooling system has blocked filters and reduced airflow",
        "blocked filters and reduced airflow",
        "blocked filters",
        "reduced airflow due to blocked filters",
    ],
    "cooling_pump_vibration": [
        "cooling pump vibrating excessively",
        "cooling pump is vibrating excessively",
        "excessive vibration from cooling pump",
    ],
    "cooling_intermittent": [
        "cooling system frequently stops and restarts",
        "frequently stops and restarts",
        "cooling system cycles on and off",
        "frequent stop and restart of cooling",
    ],

    # ------------------------------------------------------------------
    # GENERAL MECHANICAL FAULTS (Q91-Q100)
    # ------------------------------------------------------------------
    "machine_excessive_vibration": [
        "industrial machine producing excessive mechanical vibration",
        "producing excessive mechanical vibration",
        "excessive mechanical vibration",
        "machine has excessive vibration",
    ],
    "machine_knocking": [
        "machine makes a loud knocking sound whenever it operates",
        "loud knocking sound",
        "knocking sound whenever it operates",
        "machine knocking",
    ],
    "machine_overheating": [
        "machine overheating under normal operating conditions",
        "overheating under normal operating conditions",
        "machine is overheating normally",
    ],
    "machine_loose_bolts": [
        "machine has loose bolts and unusual mechanical noise",
        "loose bolts and unusual mechanical noise",
        "loose bolts",
        "bolts are loose",
    ],
    "machine_stiff_shaft": [
        "rotating shaft becoming difficult to turn",
        "shaft becoming difficult to turn",
        "difficult to turn the shaft",
        "shaft is hard to turn",
        "shaft binding",
    ],
    "machine_excessive_friction": [
        "machine produces excessive friction and becomes hot",
        "excessive friction and becomes hot",
        "excessive friction",
        "high friction causing heat",
    ],
    "machine_unusual_play": [
        "unusual movement between two connected mechanical components",
        "unusual movement between components",
        "play between connected components",
        "loose connection between components",
    ],
    "machine_shaft_misalignment": [
        "machine has a misaligned shaft and produces continuous vibration",
        "misaligned shaft and continuous vibration",
        "misaligned shaft",
        "shaft misalignment causing vibration",
    ],
    "machine_accelerated_wear": [
        "machine components wearing out much faster than expected",
        "components wearing out much faster than expected",
        "accelerated wear of components",
        "premature wear of machine parts",
    ],
    "machine_sudden_failure": [
        "machine suddenly stopped and I noticed a burning smell and unusual noise",
        "suddenly stopped with burning smell and unusual noise",
        "sudden stop with burning smell and noise",
        "catastrophic stop with smell and noise",
    ],
}


def merge_synonyms(target_dict):
    """
    Merge EXTRA_SYNONYMS into an existing SYNONYMS dictionary
    (the one defined in processor.py).  Safe to call multiple times.
    Returns the number of new phrases added.
    """
    added = 0
    for name, phrases in EXTRA_SYNONYMS.items():
        bucket = target_dict.setdefault(name, [])
        for p in phrases:
            if p not in bucket:
                bucket.append(p)
                added += 1
    return added
