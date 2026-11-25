# ============================================================
# nlp_concepts.py  -  CONCEPT LAYER (v6)
#
# Complements the v5 phrase matcher. Instead of needing an exact
# phrase per assertion, it:
#   1. rewrites common phrasings ("won't start", "above rated load")
#   2. collapses component aliases (gear box / reducer -> gearbox)
#   3. fixes small typos (vibrashun, moter)
#   4. maps words to concepts (shaking/shudders -> vibration)
#   5. matches an assertion when its component + concept tokens
#      appear together in one clause
# It only runs for assertions the v5 phrase matcher did NOT find.
# ============================================================

import re
from difflib import get_close_matches

SUBJECT_BY_CATEGORY = {
    "electric_motors": "motor",
    "gearboxes": "gearbox",
    "bearings": "bearing",
    "conveyor_systems": "conveyor",
    "hydraulic_systems": "hydraulic",
    "compressors": "compressor",
    "electrical_systems": "electrical_system",
    "cnc_machines": "cnc",
    "cooling_systems": "cooling_system",
    "general_mechanical_faults": "machine",
}

# canonical component -> alternative ways users refer to it
COMPONENT_ALIASES = {
    "motor": ["electric motor", "induction motor", "ac motor", "dc motor",
              "drive motor", "main motor", "pump motor", "fan motor", "motors"],
    "gearbox": ["gear box", "gearboxes", "gear case", "gear unit", "gear drive",
                "speed reducer", "reducer", "transmission"],
    "bearing": ["bearings"],
    "conveyor": ["conveyor belt", "conveyer", "conveyors", "belts", "belt"],
    "hydraulic": ["hydraulic system", "hydraulic circuit", "hydraulics"],
    "compressor": ["air compressor", "compressors"],
    "cnc": ["cnc machine", "machining center", "machining centre", "lathe",
            "milling machine"],
    "cooling_system": ["cooling system", "coolant", "chiller", "radiator"],
    "electrical_system": ["electrical system", "control panel", "switchgear",
                          "electrical panel"],
    "machine": ["machines", "equipment", "machinery"],
}
COMPONENT_TOKENS = set(COMPONENT_ALIASES)

# parts that imply a component even if the component is not named
IMPLIED_COMPONENTS = {"rotor": "motor", "stator": "motor",
                      "wind": "motor", "armature": "motor"}

LOW_WORDS = ["low", "lower", "lowered", "slow", "slowly", "slower", "sluggish",
             "lagging", "weak", "weaker", "poor", "reduced", "reduce",
             "decreased", "decrease", "decreasing", "dropping", "drop", "drops",
             "dropped", "falling", "fell", "deficient"]
LOW_AND_DEFECT_WORDS = ["insufficient", "inadequate", "lack", "lacks",
                        "lacking", "lacked"]

# canonical concept -> words that express it (add more here to extend coverage)
CONCEPTS = {
    "heat": ["hot", "hotter", "heat", "heating", "heated", "heats", "overheat",
             "overheats", "overheating", "overheated", "boiling", "scorching"],
    "vibration": ["vibrate", "vibrates", "vibrated", "vibrating", "vibration",
                  "vibrations", "shake", "shakes", "shaking", "shaken", "shaky",
                  "shudder", "shudders", "shuddering", "tremble", "trembling",
                  "wobble", "wobbles", "wobbling", "judder", "juddering"],
    "noise": ["noise", "noises", "noisy", "sound", "sounds", "grinding", "grind",
              "grinds", "rattle", "rattles", "rattling", "knock", "knocks",
              "knocking", "squeal", "squealing", "squeak", "squeaking",
              "screech", "screeching", "whine", "whining", "clunk", "clunking",
              "bang", "banging", "rumble", "rumbling", "growl", "growling",
              "clatter", "clattering"],
    "hum": ["hum", "hums", "humming", "buzz", "buzzes", "buzzing"],
    "smoke": ["smoke", "smokes", "smoking", "smoky", "fumes", "fume"],
    "smell": ["smell", "smells", "smelling", "smelly", "odor", "odour", "odors",
              "stench", "stink", "stinks", "reek", "reeks", "whiff", "scent"],
    "burn": ["burn", "burns", "burnt", "burned", "burning", "scorched",
             "charred", "singed"],
    "spark": ["spark", "sparks", "sparking", "sparked", "arc", "arcs", "arcing"],
    "leak": ["leak", "leaks", "leaking", "leaked", "leakage", "drip", "drips",
             "dripping", "seep", "seeping", "ooze", "oozing", "weeping"],
    "start": ["start", "starts", "starting", "started", "startup"],
    "defect": ["damage", "damaged", "damages", "defect", "defective", "faulty",
               "fault", "broken", "break", "broke", "cracked", "crack", "failed",
               "fail", "fails", "failing", "failure", "failures", "deteriorated",
               "deteriorate", "deterioration", "breakdown", "malfunction",
               "malfunctioning", "bad", "shorted", "burnt", "burned"],
    "wear": ["wear", "worn", "wearing", "wears", "wornout"],
    "slip": ["slip", "slips", "slipping", "slipped", "slippage"],
    "overload": ["overload", "overloaded", "overloading", "overloads",
                 "overcurrent"],
    "loose": ["loose", "loosely", "loosen", "loosened", "loosening"],
    "connection": ["connection", "connections", "terminal", "terminals", "wire",
                   "wires", "wiring", "lead", "leads", "connector", "connectors"],
    "insulation": ["insulation", "insulating", "insulator"],
    "lubrication": ["lubrication", "lubricant", "lubricate", "lubricated",
                    "lubricating", "grease", "greased", "greasing"],
    "block": ["block", "blocked", "blocking", "blockage", "clog", "clogged",
              "clogging", "obstruct", "obstructed", "obstruction", "choked",
              "plugged", "restricted", "restriction"],
    "cool": ["cooling", "ventilation", "vents", "vent", "airflow", "duct",
             "ducts", "passage", "passages"],
    "phase": ["phase", "phases"],
    "imbalance": ["imbalance", "imbalanced", "unbalanced", "unbalance",
                  "unequal", "uneven", "asymmetric", "asymmetrical",
                  "mismatch", "mismatched", "different", "differs", "differing"],
    "voltage": ["voltage", "voltages", "volt", "volts"],
    "current": ["current", "currents", "amp", "amps", "amperage", "ampere",
                "overcurrent"],
    "torque": ["torque"],
    "speed": ["speed", "speeds", "rpm", "rotation", "rotate", "rotates",
              "rotated", "rotating", "spin", "spins", "spinning", "turn",
              "turns", "turning"],
    "pressure": ["pressure", "psi"],
    "inconsistent": ["inconsistent", "fluctuate", "fluctuates", "fluctuating",
                     "fluctuation", "unstable", "instability", "varying", "vary",
                     "varies", "variable", "erratic", "unsteady", "surging",
                     "hunting", "irregular", "irregularities", "irregularity",
                     "change", "changes", "changing"],
    "intermittent": ["intermittent", "intermittently", "sporadic",
                     "sporadically", "occasional", "occasionally", "sometimes",
                     "irregularly"],
    "trip": ["trip", "trips", "tripping", "tripped"],
    "wind": ["winding", "windings", "coil", "coils", "wind"],
    "misalignment": ["misaligned", "misalignment", "misalign", "skewed",
                     "crooked", "drifting"],
    "shaft": ["shaft", "shafts"],
    "rotor": ["rotor", "rotors"],
    "oil": ["oil", "oils", "oily"],
}


def _stem(w):
    """Very light stemmer (applied identically to names and user text)."""
    if "_" in w or len(w) <= 3:
        return w
    if w.endswith(("sses", "xes", "ches", "shes", "zes")):
        w = w[:-2]
    elif w.endswith("s") and not w.endswith("ss"):
        w = w[:-1]
    for suf in ("ingly", "edly", "ing", "ed", "ly"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            w = w[:-len(suf)]
            break
    if len(w) >= 4 and w[-1] == w[-2] and w[-1] not in "ls":
        w = w[:-1]
    return w


_LOOKUP = {}


def _add_lookup(word, canon):
    for key in {word, _stem(word)}:
        lst = _LOOKUP.setdefault(key, [])
        if canon not in lst:
            lst.append(canon)


for _canon, _words in CONCEPTS.items():
    for _w in _words:
        _add_lookup(_w, _canon)
for _w in LOW_WORDS:
    _add_lookup(_w, "low")
    _add_lookup(_w, "slow")
for _w in LOW_AND_DEFECT_WORDS:
    for _c in ("low", "slow", "defect"):
        _add_lookup(_w, _c)

# words that carry no diagnostic meaning (intensifiers, fillers, question words)
STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being", "am",
    "has", "have", "had", "to", "of", "with", "in", "on", "at", "from", "by",
    "for", "into", "near", "around", "about", "my", "our", "its", "it", "this",
    "that", "there", "these", "those", "which", "what", "why", "how", "when",
    "can", "could", "would", "should", "does", "do", "did", "will", "may",
    "might", "some", "any", "also", "still", "keeps", "keep", "kept", "getting",
    "gets", "get", "got", "seems", "seem", "appears", "looks", "like", "just",
    "really", "quite", "pretty", "rather", "often", "again", "constantly",
    "always", "frequent", "frequently", "repeatedly", "repeated", "regularly",
    "excessive", "excessively", "excess", "abnormal", "abnormally", "unusual",
    "unusually", "strange", "strangely", "weird", "odd", "loud", "loudly",
    "severe", "severely", "heavy", "heavily", "extreme", "extremely", "high",
    "higher", "too", "very", "much", "more", "than", "unexpectedly", "strong",
    "strongly", "visible", "continuous", "continuously", "three", "mechanical",
    "mechanically", "properly", "correctly", "having", "experiencing", "there",
    "i", "we", "you", "me", "us", "please", "help", "notice", "noticed",
    "observe", "observed", "see", "saw", "think", "problem", "issue", "issues",
    "supply", "supplied", "out", "up", "down", "make", "makes", "making",
    "produce", "produces", "producing", "give", "gives", "giving", "emit",
    "emits", "emitting", "show", "shows", "showing", "come", "comes", "coming",
    "run", "runs", "running", "work", "works", "working", "operate", "operates",
    "operating", "operation", "occur", "occurs", "level", "levels", "time",
    "times", "being", "become", "becomes", "turned", "ever", "only", "even",
    "overall", "general", "normal", "normally", "not", "no", "never", "without",
    "neither", "nor", "isnt", "arent", "cannot", "cant", "wont", "dont",
    "doesnt", "didnt", "wasnt", "werent", "hasnt", "havent",
}

NEGATION = {"not", "no", "never", "without", "neither", "nor", "isnt", "arent",
            "wasnt", "werent", "hasnt", "havent", "doesnt", "dont", "didnt",
            "cannot", "cant", "couldnt", "wont", "wouldnt"}

# "motor is running normally" etc. => the symptom is absent
SAFE_WORDS = {"normal", "normally", "healthy", "steady", "stable", "fine"}

# neutral nouns need an "abnormal" signal (motor voltage alone is not a fault)
NEUTRAL_NOUNS = {"voltage", "current", "torque", "speed", "pressure"}
ABNORMAL_RAW = {"high", "higher", "too", "excessive", "excessively", "abnormal",
                "abnormally", "unusual", "unusually", "irregular", "incorrect",
                "wrong", "unstable", "insufficient", "unbalanced", "exceeds",
                "exceeding", "above", "excess", "extra", "strong", "weak",
                "more", "much", "greater", "overheating"}
ABNORMAL_TOKENS = {"low", "defect", "inconsistent", "imbalance", "overload"}

# assertion names that describe a "failure to do X" (negation is the fault)
NEGATIVE_FAULT_ASSERTIONS = {"motor_fails_to_start"}

# assertion name words that mean "too much": a clause saying "low" vetoes them
HIGH_NAME_WORDS = {"excessive", "high", "overheating", "overloading",
                   "overload", "overloaded", "overcurrent"}

# ordered phrase rewrites, applied to normalized (lowercase, no punctuation) text
PHRASE_REWRITES = [
    # temperature
    (r"\b(?:temperature|temp)\b(?:\s+\w+){0,2}?\s+(?:high|higher|rising|rise|risen|elevated|excessive|increased|increasing|exceeds?|climbing)\b", " heat "),
    (r"\b(?:high|higher|rising|elevated|excessive|increased|abnormal)\s+(?:operating\s+)?(?:temperature|temp)s?\b", " heat "),
    # "below normal" / "above normal"
    (r"\b(?:below|under|less than|lower than)(?: the)? normal\b", " low "),
    (r"\b(?:than|above|beyond|over|exceeds?|exceeding|outside)(?: the)?(?: its| their)? normal(?: range| level| limits?| values?)?\b", " "),
    # overload
    (r"\b(?:above|beyond|over|exceeds?|exceeding|more than)(?: its| the| their)? (?:rated|rating|design|maximum|capacity|limit)\b(?: load| capacity| limit)?", " overload "),
    (r"\b(?:too much|excess(?:ive)?|heavy|high|extra)\s+(?:mechanical\s+)?load\b", " overload "),
    # intermittent / unsteady
    (r"\b(?:does not|do not|not)\s+(?:run|operate|work)\s+continuous(?:ly)?\b", " intermittent "),
    (r"\b(?:on and off|off and on|starts and stops|stops and starts|starting and stopping|stopping and starting|stopping and restarting|stops and restarts|stops and re ?starts?|comes and goes|come and go|now and then|every now and again|stops randomly|cuts in and out)\b", " intermittent "),
    (r"\b(?:does not|do not|fails? to|unable to|cannot|can not)\s+(?:maintain|hold|keep)(?: a)? (?:steady|constant|stable|consistent)\s+(?:speed|rpm)\b", " inconsistent speed "),
    # failure to start
    (r"\bfail(?:s|ed|ing)?\s+(?:during|at|on)\s+(?:start ?up|startup|starting)\b", " defect start "),
    (r"\b(?:will not|does not|do not|did not|cannot|can not|unable to|refuses? to|fails? to|failed to|is not able to|not able to|never)\s+(?:start(?:ing)?|turn on|power up|come on|begin(?: to)?(?: run(?:ning)?| operat(?:e|ing))?|run|operate)\b", " defect start "),
    # power / torque
    (r"\b(?:no|zero|reduced|insufficient|lack of)\s+(?:mechanical\s+)?power\b", " power loss "),
    (r"\b(?:cannot|can not|unable to|fails? to|not able to)\s+(?:provide|produce|deliver|generate|develop|give)\s+(?:enough|sufficient|adequate)\b", " insufficient "),
    (r"\b(?:not enough|too little|not sufficient)\b", " insufficient "),
    (r"\b(?:turning|twisting|rotational|rotating|pulling)\s+(?:force|power)\b", " torque "),
    # protection / trip
    (r"\bprotect\w*\s+(?:\w+\s+){0,2}shut\w*(?:\s+\w+){0,2}\s+down\b", " trip "),
    # misalignment
    (r"\b(?:not|improperly|incorrectly|badly|poorly)\s+(?:properly\s+|correctly\s+)?(?:aligned|centered|centred)\b", " misalignment "),
    (r"\bout of (?:alignment|line|true)\b", " misalignment "),
    (r"\b(?:off|out of) (?:center|centre|track)\b", " misalignment "),
    (r"\b(?:tracking|moves?|moving|drifts?|drifting|running) (?:to )?(?:one|the) side\b", " misalignment "),
    (r"\balignment (?:is |being )?(?:incorrect|faulty|off|wrong|bad|poor)\b", " misalignment "),
    (r"\b(?:incorrect|faulty|wrong|bad|poor) alignment\b", " misalignment "),
    # lubrication
    (r"\b(?:running|run) dry\b", " lubrication defect "),
    (r"\b(?:not|never|poorly|improperly|inadequately|insufficiently)\s+(?:properly\s+|adequately\s+|sufficiently\s+|well\s+)?(?:lubricated|greased)\b", " lubrication defect "),
    (r"\b(?:no|without|lost|lack of|out of|short of)\s+(?:the\s+)?(?:grease|lubricant|lubrication)\b", " lubrication defect "),
    # insulation / connections
    (r"\binsulation resistance (?:is |being )?(?:low|poor|weak|reduced|decreased)\b", " insulation defect "),
    (r"\b(?:not|isnt)\s+(?:properly\s+|fully\s+)?(?:tight|tightened|secure|secured|fastened)\b", " loose "),
    (r"\b(?:come|came|working|worked)\s+loose\b", " loose "),
    # loudness as noise
    (r"\b(?:is|are|gets?|getting|too|very|really) loud\b", " noise "),
]
_COMPILED_REWRITES = [(re.compile(p), r) for p, r in PHRASE_REWRITES]

_ALIAS_PAIRS = sorted(
    [(alias, canon) for canon, aliases in COMPONENT_ALIASES.items()
     for alias in aliases],
    key=lambda pair: -len(pair[0]))
_ALIAS_RE = [(re.compile(r"(?<![a-z0-9_])" + re.escape(a) + r"(?![a-z0-9_])"), c)
             for a, c in _ALIAS_PAIRS]

CLAUSE_SPLIT_RE = re.compile(
    r"\b(?:and|but|however|yet|whereas|although|though|because|since|while|"
    r"also|plus|then|so)\b")

# Words the typo-fixer must never "correct" (real words that look like others).
KNOWN_WORDS = {"rated", "rating", "load", "loads", "power", "system", "shut",
               "shuts", "after", "before", "during", "start", "stop", "stops",
               "stopped", "stopping", "restart", "restarts", "restarting",
               "supply", "motor", "gearbox", "bearing", "conveyor", "temperature",
               "temp", "enough", "sufficient", "lubricated", "tight", "secure",
               "secured", "fastened", "aligned", "alignment", "centered",
               "centre", "center", "track", "side", "protection", "breaker",
               "relay", "circuit", "resistance", "internal", "external"}


def _build_vocab():
    vocab = set(_LOOKUP) | STOPWORDS | KNOWN_WORDS | COMPONENT_TOKENS
    vocab |= {a for aliases in COMPONENT_ALIASES.values() for a in aliases
              if " " not in a}
    vocab |= {w for words in CONCEPTS.values() for w in words}
    return vocab


_VOCAB = _build_vocab()
_VOCAB_LIST = sorted(_VOCAB)
_COMPONENT_WORDS = sorted(COMPONENT_TOKENS | {a for al in COMPONENT_ALIASES.values()
                                              for a in al if " " not in a})


def _fix_typos(words):
    fixed = []
    for w in words:
        if len(w) < 4 or w in _VOCAB or w.isdigit() or "_" in w:
            fixed.append(w)
            continue
        guess = get_close_matches(w, _COMPONENT_WORDS, n=1, cutoff=0.8)
        if not guess and len(w) >= 5:
            cutoff = 0.78 if len(w) >= 8 else 0.86
            guess = get_close_matches(w, _VOCAB_LIST, n=1, cutoff=cutoff)
        fixed.append(guess[0] if guess else w)
    return fixed


def _collapse_aliases(text):
    for pattern, canon in _ALIAS_RE:
        text = pattern.sub(canon, text)
    return text


def _to_tokens(word):
    if word in COMPONENT_TOKENS:
        return [word]
    if word in _LOOKUP:
        return _LOOKUP[word]
    stem = _stem(word)
    return _LOOKUP.get(stem, [stem])


def _make_clause(words):
    tokens = []
    for i, w in enumerate(words):
        if w in STOPWORDS:
            continue
        for tok in _to_tokens(w):
            tokens.append((tok, i))
    comps = {t for t, _ in tokens if t in COMPONENT_TOKENS}
    comps |= {IMPLIED_COMPONENTS[t] for t, _ in tokens if t in IMPLIED_COMPONENTS}
    return {"words": words, "tokens": tokens, "comps": comps}


def build_concept_clauses(user_text, normalize_fn, category=None):
    """Turn free text into clauses of canonical tokens, carrying the subject."""
    category_comp = SUBJECT_BY_CATEGORY.get(category)
    clauses, last_comps, pending = [], set(), set()

    for piece in re.split(r"[.,;:!?\n()]+", user_text.replace("\u2019", "'")):
        text = normalize_fn(piece)
        if not text:
            continue
        for pattern, repl in _COMPILED_REWRITES:
            text = pattern.sub(repl, text)
        text = _collapse_aliases(text)

        for sub in CLAUSE_SPLIT_RE.split(text):
            words = _fix_typos(sub.split())
            if not words:
                continue
            clause = _make_clause(words)
            has_symptom = any(t not in COMPONENT_TOKENS for t, _ in clause["tokens"])

            if clause["comps"] and not has_symptom:
                # "the motor and gearbox are hot": hold subjects for next clause
                pending |= clause["comps"]
                last_comps = set(pending)
                continue
            if clause["comps"]:
                clause["comps"] |= pending
                pending = set()
                last_comps = set(clause["comps"])
            else:
                clause["comps"] = set(pending or last_comps or
                                      ({category_comp} if category_comp else set()))
                pending = set()
            clauses.append(clause)
    return clauses


_COMPILED_ASSERTIONS = {}


def _compile_assertion(assertion):
    name = assertion["name"]
    if name in _COMPILED_ASSERTIONS:
        return _COMPILED_ASSERTIONS[name]
    spec = None
    comp = SUBJECT_BY_CATEGORY.get(assertion.get("category"))
    if comp:
        text = _collapse_aliases(name.replace("_", " ").lower())
        required = set()
        for w in text.split():
            if w in STOPWORDS:
                continue
            required.update(_to_tokens(w))
        required.discard(comp)
        if required:
            wants_high = bool(set(name.split("_")) & HIGH_NAME_WORDS)
            spec = (comp, frozenset(required), wants_high)
    _COMPILED_ASSERTIONS[name] = spec
    return spec


def _polarity(words, first_index, name):
    if SAFE_WORDS & set(words):
        return "negated"
    if name in NEGATIVE_FAULT_ASSERTIONS:
        return "positive"
    window = words[max(0, first_index - 3): first_index + 1]
    return "negated" if any(w in NEGATION for w in window) else "positive"


def concept_match(assertion, clauses):
    """Return [{'clause', 'polarity', 'matched_phrase'}] for one assertion."""
    spec = _compile_assertion(assertion)
    if not spec:
        return []
    comp, required, wants_high = spec
    hits = []
    for clause in clauses:
        if comp not in clause["comps"]:
            continue
        present = {}
        for tok, idx in clause["tokens"]:
            present.setdefault(tok, idx)
        if not required <= present.keys():
            continue
        tokens = set(present)
        if wants_high and "low" in tokens:
            continue
        if required <= NEUTRAL_NOUNS and not (
                set(clause["words"]) & ABNORMAL_RAW or tokens & ABNORMAL_TOKENS):
            continue
        first = min(present[t] for t in required)
        hits.append({
            "clause": " ".join(clause["words"]),
            "polarity": _polarity(clause["words"], first, assertion["name"]),
            "matched_phrase": "concepts: " + " + ".join(sorted(required)),
        })
    return hits


def explain(user_text, normalize_fn, category=None):
    """Debug helper: show what the concept layer understood."""
    for c in build_concept_clauses(user_text, normalize_fn, category):
        print(" ".join(c["words"]), "->", sorted({t for t, _ in c["tokens"]}),
              "| components:", sorted(c["comps"]))
