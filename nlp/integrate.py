# ============================================================
# integrate.py  –  one-call helper to apply both extensions
# ============================================================

def enhance_nlp(concepts_module=None, synonyms_dict=None):
    """
    Apply concept_extensions and extra_synonyms.

    Parameters
    ----------
    concepts_module : module, optional
        The nlp_concepts module object.  If None, tries
        ``from nlp import nlp_concepts`` and then
        ``import nlp_concepts``.
    synonyms_dict : dict, optional
        The SYNONYMS dictionary from processor.py.  If None,
        tries to import it automatically.

    Returns
    -------
    dict with keys ``concepts_ok``, ``synonyms_added``, ``messages``.
    """
    messages = []
    result = {"concepts_ok": False, "synonyms_added": 0, "messages": messages}

    # ---- concepts ----
    if concepts_module is None:
        try:
            from nlp import nlp_concepts as concepts_module
        except ImportError:
            try:
                import nlp_concepts as concepts_module
            except ImportError:
                messages.append(
                    "Could not import nlp_concepts. "
                    "Pass the module explicitly: enhance_nlp(concepts_module=...)"
                )
                return result

    try:
        from .concept_extensions import apply_extensions
    except ImportError:
        from concept_extensions import apply_extensions

    try:
        apply_extensions(concepts_module)
        result["concepts_ok"] = True
        messages.append("Concept extensions applied.")
    except Exception as e:
        messages.append(f"Concept extensions failed: {e}")
        return result

    # ---- synonyms ----
    if synonyms_dict is None:
        try:
            from nlp.processor import SYNONYMS as synonyms_dict
        except ImportError:
            try:
                from processor import SYNONYMS as synonyms_dict
            except ImportError:
                messages.append(
                    "Could not import SYNONYMS. "
                    "Pass the dict explicitly: enhance_nlp(synonyms_dict=...)"
                )
                return result

    try:
        from .extra_synonyms import merge_synonyms
    except ImportError:
        from extra_synonyms import merge_synonyms

    try:
        added = merge_synonyms(synonyms_dict)
        result["synonyms_added"] = added
        messages.append(f"Added {added} extra synonym phrases.")
    except Exception as e:
        messages.append(f"Synonym merge failed: {e}")

    return result


if __name__ == "__main__":
    # Self-test when run directly (will fail gracefully if packages missing)
    r = enhance_nlp()
    for m in r["messages"]:
        print(m)
