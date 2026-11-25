# ============================================================
# concept_extensions.py
#
# Drop-in extensions that significantly improve NLP coverage
# for the 100 industrial fault questions (motors, gearboxes,
# bearings, conveyors, hydraulics, compressors, electrical,
# CNC, cooling, general mechanical).
#
# DO NOT modify the original nlp_concepts.py or processor.py.
# Import and call apply_extensions() early in your NLP pipeline
# (before build_concept_clauses / concept_match are used).
#
# Usage:
#   import nlp.nlp_concepts as concepts
#   from nlp.concept_extensions import apply_extensions
#   apply_extensions(concepts)
# ============================================================

from difflib import get_close_matches

# ---------------------------------------------------------------------------
# Additional / expanded CONCEPTS
# (these are merged into the original CONCEPTS lookup)
# ---------------------------------------------------------------------------
EXTRA_CONCEPTS = {
    # Temperature / heat (already strong; add common industrial variants)
    "heat": [
        "temp", "temperature", "overtemp", "thermal", "warm", "warmer",
        "scorching", "searing", "blistering", "redhot", "glowing",
    ],

    # Vibration / shaking
    "vibration": [
        "oscillat", "oscillating", "oscillation", "chatter", "chattering",
        "rocking", "rock", "rocks", "buffet", "buffeting",
    ],

    # Noise family – already good; add more industrial sounds
    "noise": [
        "whine", "whining", "whined", "howl", "howling", "growl", "growling",
        "hiss", "hissing", "clank", "clanking", "thump", "thumping",
        "click", "clicking", "ticking", "screech", "screeching",
        "grinding", "grind", "grinds", "rattle", "rattling",
    ],

    # Smell / burn
    "smell": [
        "odour", "aroma", "reek", "stench", "whiff",
    ],
    "burn": [
        "scorched", "charred", "singed", "smouldering", "smoldering",
        "toasted", "fried",
    ],

    # Leakage
    "leak": [
        "seepage", "weep", "weeping", "escape", "escaping", "escaping",
        "loss of fluid", "fluid loss",
    ],

    # Slip / belt related
    "slip": [
        "slippage", "slipping", "slips", "slipped", "slide", "sliding",
        "skid", "skidding",
    ],

    # Wear / degradation
    "wear": [
        "worn", "wearing", "abrasion", "abraded", "erosion", "eroded",
        "degraded", "degradation", "deteriorated", "deterioration",
        "thinning", "pitting", "scuffed", "scuffing",
    ],

    # Loose / play / clearance
    "loose": [
        "looseness", "play", "excessive play", "slop", "slack", "sloppy",
        "wobbly", "rattly",
    ],
    "clearance": [
        "clearance", "gap", "gaps", "play", "endplay", "radial play",
        "axial play", "loose fit",
    ],

    # Lubrication
    "lubrication": [
        "lubrication", "lubricant", "lube", "grease", "oil", "oiling",
        "greasing", "dry", "unlubricated", "starved",
    ],

    # Contamination / dirty oil / fluid quality
    "contamination": [
        "contaminated", "contamination", "dirty", "dirt", "debris",
        "particles", "sludge", "sludgy", "milky", "cloudy", "discoloured",
        "discolored", "black oil", "dark oil", "metal particles",
    ],

    # Pressure (hydraulic / pneumatic / compressor)
    "pressure": [
        "pressure", "pressures", "psi", "bar", "force", "forceful",
        "build pressure", "building pressure", "pressure build",
        "low pressure", "high pressure", "pressure drop", "pressure loss",
    ],

    # Flow / circulation
    "flow": [
        "flow", "flows", "flowing", "circulation", "circulating",
        "circulate", "throughput", "delivery", "output",
    ],

    # Speed / rotation regularity
    "speed": [
        "speed", "rpm", "rotation", "rotating", "turns", "turning",
        "revolving", "rev", "revs",
    ],
    "inconsistent": [
        "uneven", "unevenly", "irregular", "irregularly", "erratic",
        "unstable", "fluctuating", "fluctuates", "fluctuation",
        "varying", "varies", "surging", "hunting", "jerky", "jerking",
        "jerk", "stuttering", "stutter", "pulsating", "pulsation",
    ],

    # Start / stop / intermittent
    "start": [
        "start", "starts", "starting", "startup", "begin", "begins",
    ],
    "stop": [
        "stop", "stops", "stopped", "stopping", "halt", "halts",
        "shut down", "shutdown", "shutting down", "trip", "trips",
        "tripping", "cut out", "cutout",
    ],
    "intermittent": [
        "intermittent", "intermittently", "repeatedly", "sporadic",
        "occasional", "sometimes", "on and off", "starts and stops",
        "stop and start", "cycling",
    ],

    # Power / load / torque
    "power": [
        "power", "powers", "powered", "force", "output", "drive",
    ],
    "load": [
        "load", "loads", "loaded", "loading", "heavy load", "overload",
        "overloaded", "capacity",
    ],
    "torque": [
        "torque", "turning force", "rotational force",
    ],

    # Current / electrical
    "current": [
        "current", "amperage", "amps", "amp", "draw", "draws", "drawing",
        "consumption", "consumes", "consuming", "electricity",
    ],
    "voltage": [
        "voltage", "volt", "volts", "potential",
    ],
    "phase": [
        "phase", "phases", "threephase", "three-phase", "3phase", "3-phase",
        "imbalance", "unbalance", "unbalanced",
    ],

    # Alignment / centering (conveyor + shafts)
    "alignment": [
        "aligned", "alignment", "misaligned", "misalignment", "skewed",
        "crooked", "offcenter", "off-centre", "off center", "tracking",
        "track", "centered", "centred", "centre", "center", "sideways",
        "toward one side", "one side",
    ],

    # Roughness / surface / feel
    "rough": [
        "rough", "roughness", "gritty", "grainy", "not smooth",
        "feels rough", "rough feel", "abrasive",
    ],

    # Friction
    "friction": [
        "friction", "frictional", "drag", "dragging", "resistance",
        "stiff", "binding", "seizing", "seize", "seized",
    ],

    # Accuracy / positioning (CNC)
    "accuracy": [
        "accuracy", "accurate", "inaccurate", "precision", "precise",
        "dimension", "dimensions", "tolerance", "positioning", "position",
        "positional", "axis error", "axis movement", "lost position",
    ],

    # Moisture / water in air
    "moisture": [
        "moisture", "moist", "wet", "water", "condensation", "humid",
        "humidity", "damp", "liquid",
    ],

    # Air / gas related (compressors)
    "air": [
        "air", "compressed air", "airflow", "air flow", "delivery",
        "output air", "cfm",
    ],

    # Blockage / restriction
    "blockage": [
        "block", "blocked", "blocking", "blockage", "clog", "clogged",
        "restriction", "restricted", "obstruction", "obstructed",
        "filter blocked", "filters blocked",
    ],

    # Cracks / structural damage
    "crack": [
        "crack", "cracks", "cracked", "fracture", "fractured", "split",
        "splitting", "tear", "torn",
    ],

    # Falling material / spillage (conveyor)
    "spill": [
        "falling", "fall", "falls", "spilling", "spill", "spillage",
        "dropping", "drop", "material falling",
    ],

    # Tension (belts)
    "tension": [
        "tension", "tense", "tight", "tightness", "slack", "loose tension",
        "belt tension",
    ],

    # Jerk / irregular motion (hydraulics / actuators)
    "jerk": [
        "jerk", "jerks", "jerking", "jerky", "stutter", "stuttering",
        "hesitation", "hesitating", "stick-slip", "stick slip",
    ],

    # Performance degradation
    "performance": [
        "performance", "efficiency", "output", "capacity", "ability",
        "unable", "cannot", "can't", "fails to", "not enough",
        "insufficient", "decreased", "reduced", "poor",
    ],

    # Smoke / fumes already present; keep
    "smoke": [
        "smoke", "smokes", "smoking", "fume", "fumes", "vapour", "vapor",
    ],

    # Winding / electrical insulation related
    "winding": [
        "winding", "windings", "coil", "coils", "stator winding",
        "rotor winding",
    ],

    # Housing / casing
    "housing": [
        "housing", "casing", "case", "enclosure", "cover",
    ],

    # Shaft
    "shaft": [
        "shaft", "shafts", "spindle", "arbor",
    ],

    # Tool (CNC)
    "tool": [
        "tool", "tools", "cutter", "cutting tool", "insert", "bit",
    ],

    # Surface finish
    "finish": [
        "finish", "surface finish", "surface", "rough finish",
        "poor finish", "finish quality",
    ],

    # Filter / airflow (cooling)
    "filter": [
        "filter", "filters", "strainer", "screen",
    ],
    "airflow": [
        "airflow", "air flow", "airflow", "ventilation", "cooling air",
    ],

    # Coolant / fluid
    "coolant": [
        "coolant", "cooling fluid", "cooling liquid", "refrigerant",
        "fluid", "liquid",
    ],

    # Pump / actuator (hydraulics / cooling)
    "pump": [
        "pump", "pumps", "pumping",
    ],
    "actuator": [
        "actuator", "cylinder", "ram", "piston",
    ],

    # Panel / electrical enclosure
    "panel": [
        "panel", "control panel", "cabinet", "enclosure", "switchgear",
    ],

    # Fuse / breaker
    "breaker": [
        "breaker", "circuit breaker", "mcb", "mccb", "fuse", "fuses",
        "protective device",
    ],

    # Warning / fault indication
    "warning": [
        "warning", "fault", "alarm", "error", "fault warning",
        "error message", "fault code",
    ],

    # Difficult to turn / high resistance
    "stiff": [
        "difficult to turn", "hard to turn", "stiff", "binding",
        "seizing", "locked", "seized", "won't turn", "cannot turn",
    ],

    # Contaminated oil already under contamination
}

# ---------------------------------------------------------------------------
# Extra phrase rewrites (applied on normalized text)
# Order matters – more specific first.
# ---------------------------------------------------------------------------
EXTRA_PHRASE_REWRITES = [
    # Temperature rising / increasing
    (r"\b(?:temperature|temp)\b(?:\s+\w+){0,3}?\s+(?:is\s+)?(?:increasing|rising|climbing|elevated|high|higher|excessive)\b",
     " heat "),
    (r"\b(?:increasing|rising|climbing)\s+(?:temperature|temp)\b", " heat "),
    (r"\bbecomes?\s+(?:very\s+)?(?:hot|warm)\b", " heat "),
    (r"\bgetting\s+(?:extremely\s+)?hot\b", " heat "),
    (r"\brunning\s+(?:hot|warm)\b", " heat "),

    # Vibration / shaking
    (r"\bshakes?\s+heavily\b", " vibration "),
    (r"\bproducing\s+excessive\s+vibration\b", " vibration "),
    (r"\bexcessive\s+(?:mechanical\s+)?vibration\b", " vibration "),
    (r"\bvibrates?\s+excessively\b", " vibration "),

    # Noise variants
    (r"\b(?:loud\s+)?whining\s+noise\b", " noise "),
    (r"\bgrinding\s+(?:noise|sound)\b", " noise "),
    (r"\bsquealing\s+(?:sound|noise)\b", " noise "),
    (r"\bknocking\s+(?:sound|noise)s?\b", " noise "),
    (r"\bunusual\s+(?:noise|sound)\b", " noise "),
    (r"\bstrange\s+(?:noise|sound|grinding)\b", " noise "),
    (r"\bcontinuous\s+grinding\s+noise\b", " noise "),

    # Burning smell
    (r"\bburning\s+smell\b", " burn smell "),
    (r"\bsmell\s+of\s+burning\b", " burn smell "),
    (r"\bburnt\s+(?:smell|odor|odour)\b", " burn smell "),

    # Smoke near winding
    (r"\bsmoke\s+near\s+(?:its\s+)?winding\b", " smoke wind "),
    (r"\bsmoke\s+(?:from|near)\s+(?:the\s+)?(?:motor\s+)?winding\b", " smoke wind "),

    # Current draw
    (r"\bdrawing\s+more\s+(?:electrical\s+)?current\b", " current high "),
    (r"\b(?:more|excessive|high)\s+(?:electrical\s+)?current\b", " current high "),
    (r"\bcurrent\s+(?:is\s+)?(?:higher|more|excessive)\b", " current high "),

    # Loose connections
    (r"\bloose\s+(?:electrical\s+)?connections?\b", " loose connection "),
    (r"\belectrical\s+connections?\s+(?:seem\s+)?loose\b", " loose connection "),

    # Start / stop repeatedly
    (r"\bstarts?\s+and\s+stops?\s+repeatedly\b", " intermittent start stop "),
    (r"\bstart\s+and\s+stop\s+repeatedly\b", " intermittent start stop "),
    (r"\brepeatedly\s+(?:starts?\s+and\s+stops?|stops?\s+and\s+starts?)\b",
     " intermittent "),

    # Uneven running (3-phase)
    (r"\brunning\s+unevenly\b", " inconsistent "),
    (r"\buneven\s+(?:running|operation|rotation)\b", " inconsistent "),
    (r"\bthree[\s\-]?phase\b", " phase "),

    # Power loss
    (r"\bloses?\s+power\b", " power low "),
    (r"\blosing\s+power\b", " power low "),
    (r"\bpower\s+loss\b", " power low "),

    # Gearbox specific
    (r"\boil\s+leaking\s+from\b", " leak oil "),
    (r"\bleaking\s+(?:from\s+)?(?:the\s+)?gearbox\b", " leak oil "),
    (r"\binsufficient\s+lubrication\b", " low lubrication "),
    (r"\boil\s+looks?\s+contaminated\b", " contamination oil "),
    (r"\bcontaminated\s+oil\b", " contamination oil "),
    (r"\brott?ating\s+irregularly\b", " inconsistent shaft "),
    (r"\bnot\s+transferring\s+power\s+smoothly\b", " power inconsistent "),

    # Bearing
    (r"\bfeels?\s+rough\b", " rough "),
    (r"\bexcessive\s+clearance\b", " clearance high "),
    (r"\bwearing\s+out\s+(?:faster|quickly|prematurely)\b", " wear high "),
    (r"\bworn\s+out\b", " wear "),

    # Conveyor
    (r"\bkeep[s]?\s+slipping\b", " slip "),
    (r"\bbelt\s+(?:is\s+)?slipping\b", " slip "),
    (r"\bmoving\s+toward\s+one\s+side\b", " alignment "),
    (r"\bstaying\s+centered\b", " alignment "),
    (r"\bnot\s+(?:staying\s+)?centered\b", " alignment "),
    (r"\bbelt\s+tension\s+(?:seems?\s+)?(?:too\s+)?loose\b", " tension low "),
    (r"\bmaterial\s+falling\b", " spill "),
    (r"\bvisible\s+cracks\b", " crack "),
    (r"\bexcessive\s+wear\b", " wear high "),
    (r"\bmoving\s+slower\s+than\b", " speed low "),

    # Hydraulic
    (r"\bunable\s+to\s+generate\s+enough\s+pressure\b", " pressure low "),
    (r"\bnot\s+enough\s+pressure\b", " pressure low "),
    (r"\blosing\s+pressure\b", " pressure low "),
    (r"\bpressure\s+(?:is\s+)?(?:low|dropping|lost)\b", " pressure low "),
    (r"\bmoves?\s+very\s+slowly\b", " speed low "),
    (r"\bjerking\b", " jerk "),
    (r"\bmoving\s+irregularly\b", " inconsistent jerk "),
    (r"\bunable\s+to\s+lift\b", " load performance low "),
    (r"\boil\s+looks?\s+dirty\b", " contamination "),
    (r"\bperformance\s+has\s+decreased\b", " performance low "),

    # Compressor
    (r"\btaking\s+too\s+long\s+to\s+build\s+pressure\b", " pressure slow "),
    (r"\bbuild\s+pressure\b", " pressure "),
    (r"\bshutting\s+down\s+automatically\b", " stop "),
    (r"\bair\s+leakage\b", " leak air "),
    (r"\bproducing\s+less\s+air\b", " air low "),
    (r"\bless\s+air\s+than\s+usual\b", " air low "),
    (r"\bconsume[s]?\s+more\s+electricity\b", " current high "),
    (r"\bproducing\s+moisture\b", " moisture "),
    (r"\bmoisture\s+in\s+(?:the\s+)?compressed\s+air\b", " moisture "),
    (r"\boil\s+level\s+is\s+low\b", " low oil "),

    # Electrical
    (r"\bcontrol\s+panel\b", " panel "),
    (r"\bcircuit\s+breaker\s+trips?\b", " breaker trip "),
    (r"\bfuse\s+keep[s]?\s+blowing\b", " breaker trip "),
    (r"\bblowing\s+repeatedly\b", " breaker trip "),
    (r"\bvoltage\s+fluctuating\b", " voltage inconsistent "),
    (r"\bfluctuating\s+(?:supply\s+)?voltage\b", " voltage inconsistent "),
    (r"\bintermittent\s+power\b", " intermittent power "),
    (r"\bnot\s+receiving\s+power\b", " power low "),
    (r"\bcables?\s+(?:are\s+)?overheating\b", " heat connection "),
    (r"\babnormal\s+voltage\s+difference\b", " voltage phase "),
    (r"\bvoltage\s+difference\s+between\s+(?:the\s+)?(?:three\s+)?phases?\b",
     " voltage phase "),
    (r"\bburning\s+smell\s+near\s+(?:the\s+)?wiring\b", " burn smell connection "),

    # CNC
    (r"\binaccurate\s+dimensions?\b", " accuracy low "),
    (r"\bproducing\s+inaccurate\b", " accuracy low "),
    (r"\brough\s+surface\s+finish\b", " finish rough "),
    (r"\bsurface\s+finish\b", " finish "),
    (r"\bcutting\s+tool\s+breaking\b", " tool defect "),
    (r"\btool\s+breaking\s+frequently\b", " tool defect "),
    (r"\bspindle\s+speed\s+fluctuating\b", " speed inconsistent "),
    (r"\baxis\s+movement\s+error\b", " accuracy "),
    (r"\blose[s]?\s+(?:its\s+)?positioning\s+accuracy\b", " accuracy low "),
    (r"\bpositioning\s+accuracy\b", " accuracy "),

    # Cooling
    (r"\bunable\s+to\s+maintain\s+(?:the\s+)?(?:required\s+)?temperature\b",
     " heat performance low "),
    (r"\btemperature\s+keeps?\s+increasing\b", " heat "),
    (r"\bcoolant\s+leaking\b", " leak coolant "),
    (r"\bcirculating\s+less\s+fluid\b", " flow low "),
    (r"\bless\s+fluid\s+than\s+normal\b", " flow low "),
    (r"\btaking\s+too\s+long\s+to\s+reduce\s+(?:the\s+)?temperature\b",
     " heat performance low "),
    (r"\bblocked\s+filters?\b", " blockage filter "),
    (r"\breduced\s+airflow\b", " airflow low "),
    (r"\bfrequently\s+stops?\s+and\s+restarts?\b", " intermittent stop "),

    # General mechanical
    (r"\bloose\s+bolts?\b", " loose "),
    (r"\bdifficult\s+to\s+turn\b", " stiff "),
    (r"\bexcessive\s+friction\b", " friction high "),
    (r"\bunusual\s+movement\s+between\b", " loose misalignment "),
    (r"\bmisaligned\s+shaft\b", " misalignment shaft "),
    (r"\bcomponents?\s+wearing\s+out\s+(?:much\s+)?faster\b", " wear high "),
    (r"\bsuddenly\s+stopped\b", " stop "),
    (r"\bburning\s+smell\s+and\s+unusual\s+noise\b", " burn smell noise "),
]

# ---------------------------------------------------------------------------
# Extra component aliases
# ---------------------------------------------------------------------------
EXTRA_COMPONENT_ALIASES = {
    "motor": [
        "electric motor", "induction motor", "ac motor", "dc motor",
        "drive motor", "main motor", "pump motor", "fan motor", "motors",
        "three phase motor", "three-phase motor", "3-phase motor",
    ],
    "gearbox": [
        "gear box", "gearboxes", "gear case", "gear unit", "gear drive",
        "speed reducer", "reducer", "transmission", "gear housing",
    ],
    "bearing": [
        "bearings", "industrial bearing", "ball bearing", "roller bearing",
        "bearing housing",
    ],
    "conveyor": [
        "conveyor belt", "conveyer", "conveyors", "belt conveyor",
        "conveyor system", "belt", "belts",
    ],
    "hydraulic": [
        "hydraulic system", "hydraulic circuit", "hydraulics",
        "hydraulic pump", "hydraulic cylinder", "hydraulic actuator",
        "hydraulic oil",
    ],
    "compressor": [
        "air compressor", "compressors", "compressor unit",
    ],
    "cnc": [
        "cnc machine", "machining center", "machining centre", "lathe",
        "milling machine", "cnc spindle", "spindle",
    ],
    "cooling_system": [
        "cooling system", "coolant system", "chiller", "radiator",
        "cooling unit", "cooling pump", "cooling fan",
    ],
    "electrical_system": [
        "electrical system", "control panel", "switchgear",
        "electrical panel", "electrical cables", "wiring",
    ],
    "machine": [
        "machines", "equipment", "machinery", "industrial machine",
    ],
}

# ---------------------------------------------------------------------------
# Extra implied components (word -> component)
# ---------------------------------------------------------------------------
EXTRA_IMPLIED = {
    "rotor": "motor",
    "stator": "motor",
    "winding": "motor",
    "armature": "motor",
    "spindle": "cnc",
    "cutter": "cnc",
    "tool": "cnc",
    "axis": "cnc",
    "roller": "conveyor",
    "belt": "conveyor",
    "cylinder": "hydraulic",
    "actuator": "hydraulic",
    "piston": "hydraulic",
    "pump": "hydraulic",          # context dependent, but useful default
    "valve": "hydraulic",
    "breaker": "electrical_system",
    "fuse": "electrical_system",
    "panel": "electrical_system",
    "cable": "electrical_system",
    "wiring": "electrical_system",
    "filter": "cooling_system",
    "coolant": "cooling_system",
    "fan": "cooling_system",
    "housing": "gearbox",
    "gear": "gearbox",
}

# ---------------------------------------------------------------------------
# Extra stopwords / neutral words that should not force matches
# ---------------------------------------------------------------------------
EXTRA_STOPWORDS = {
    "why", "what", "how", "when", "where", "which", "who",
    "could", "would", "should", "might", "may", "can",
    "please", "help", "inspect", "check", "investigate",
    "possible", "reason", "cause", "problem", "issue",
    "during", "after", "before", "while", "under", "over",
    "normal", "normally", "usual", "usually", "expected",
    "short", "time", "operation", "operating", "production",
    "materials", "material", "heavy", "continuous", "frequently",
    "repeatedly", "sometimes", "suddenly", "unexpectedly",
    "visible", "signs", "of", "the", "a", "an", "my", "its",
    "this", "that", "these", "those", "and", "or", "but",
    "even", "though", "although", "because", "since",
    "seems", "seem", "looks", "looking", "noticed", "notice",
    "producing", "produce", "makes", "making", "becomes",
    "become", "getting", "gets", "running", "works", "working",
}

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def apply_extensions(concepts_module):
    """
    Mutate the given nlp_concepts module in-place to add the extra
    vocabulary, rewrites, aliases and implied components.
    Call this once at startup before any matching occurs.
    """
    # 1. Merge CONCEPTS
    for canon, words in EXTRA_CONCEPTS.items():
        existing = concepts_module.CONCEPTS.setdefault(canon, [])
        for w in words:
            if w not in existing:
                existing.append(w)
            # also register in the lookup tables
            concepts_module._add_lookup(w, canon)

    # 2. Extra phrase rewrites (prepend so they take priority)
    # Rebuild the compiled list
    concepts_module.PHRASE_REWRITES = (
        EXTRA_PHRASE_REWRITES + list(concepts_module.PHRASE_REWRITES)
    )
    concepts_module._COMPILED_REWRITES = [
        (re.compile(pat, re.IGNORECASE), repl)
        for pat, repl in concepts_module.PHRASE_REWRITES
    ]

    # 3. Component aliases
    for comp, aliases in EXTRA_COMPONENT_ALIASES.items():
        existing = concepts_module.COMPONENT_ALIASES.setdefault(comp, [])
        for a in aliases:
            if a not in existing:
                existing.append(a)
    # rebuild alias regex pairs
    concepts_module._ALIAS_PAIRS = []
    for canon, aliases in concepts_module.COMPONENT_ALIASES.items():
        for a in aliases:
            if " " in a:
                concepts_module._ALIAS_PAIRS.append(
                    (re.compile(r"\b" + re.escape(a) + r"\b", re.I), canon)
                )
        concepts_module._ALIAS_PAIRS.append(
            (re.compile(r"\b" + re.escape(canon) + r"\b", re.I), canon)
        )
    concepts_module._ALIAS_RE = concepts_module._ALIAS_PAIRS

    # 4. Implied components
    concepts_module.IMPLIED_COMPONENTS.update(EXTRA_IMPLIED)

    # 5. Stopwords
    concepts_module.STOPWORDS.update(EXTRA_STOPWORDS)

    # 6. Rebuild vocabulary used by typo fixer
    concepts_module._VOCAB = concepts_module._build_vocab()
    concepts_module._VOCAB_LIST = sorted(concepts_module._VOCAB)
    concepts_module._COMPONENT_WORDS = sorted(
        concepts_module.COMPONENT_TOKENS |
        {a for al in concepts_module.COMPONENT_ALIASES.values()
         for a in al if " " not in a}
    )

    # Clear compiled assertions cache so new concepts are used
    concepts_module._COMPILED_ASSERTIONS.clear()

    print("[concept_extensions] Applied successfully – "
          f"{len(EXTRA_CONCEPTS)} concept groups, "
          f"{len(EXTRA_PHRASE_REWRITES)} extra rewrites, "
          f"{len(EXTRA_IMPLIED)} implied components.")


# need re for the compile step
import re
