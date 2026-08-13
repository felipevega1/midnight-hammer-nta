# Concept clusters for actor-concept network construction.
#
# HYBRID MATCHING (see notebook 04, tag_concepts) — each entry is matched in
# one of two ways, decided by its shape:
#
#   * LEMMA-MATCHED — single-word entries (no space, no hyphen). Compared for
#     equality against the sentence's lemma list produced by notebook 03
#     (en_core_web_trf lemmatizer, lowercased). One lemma entry covers its
#     whole inflection family: "strike" matches strike/strikes/striking/struck,
#     "negotiate" matches negotiates/negotiated/negotiating.
#
#   * RAW-MATCHED — entries containing a space or hyphen. Case-insensitive
#     substring match on the raw sentence text, as before. Used for multi-word
#     phrases ("bunker buster", "red line") and hyphenated terms that spaCy
#     splits into several tokens ("cease-fire", "de-escalation").
#
# NOTE: spaCy lemmatization is inflectional, not derivational — "negotiations"
# lemmatizes to "negotiation", NOT to "negotiate". Where a family has distinct
# noun and verb lemmas (negotiate/negotiation, obliterate/obliteration,
# destroy/destruction), BOTH appear below; each is one entry covering all of
# its own inflections. concept_log records the matched dictionary entry as the
# trigger plus whether it was a lemma or raw match.
#
# Within each cluster, raw phrases are listed first (most-specific) and lemma
# entries after, because tag_concepts breaks on the first match per cluster —
# the logged trigger is then the most informative one.

CONCEPT_DICT = {
    "military_action": [
        # -- raw-matched phrases --
        "carrier strike group", "aircraft carrier",
        "massive ordnance penetrator", "bunker buster", "air campaign",
        "cruise missile", "preemptive strike", "surgical strike",
        "military strike", "military action", "military force",
        "B-2 Spirit", "B-2", "GBU-57",
        # -- lemma-matched single words --
        "airstrike", "bombing", "bomb", "strike", "sortie", "munition",
        "tomahawk", "mop", "attacker", "attack",
    ],
    "nuclear_program": [
        # -- raw-matched phrases --
        "highly enriched uranium", "nuclear facility", "nuclear site",
        "nuclear program", "nuclear weapon", "nuclear bomb", "nuclear arsenal",
        "atomic bomb", "atomic weapon", "nuclear threshold", "nuclear breakout",
        "uranium stockpile", "nuclear capability",
        # -- lemma-matched single words --
        # nonproliferation is its own single token/lemma; the old substring
        # match on "proliferation" covered it implicitly.
        # fordo = common alternate spelling of Fordow in wire copy.
        "enrichment", "centrifuge", "uranium", "fordow", "fordo", "natanz",
        "isfahan", "iaea", "nonproliferation", "proliferation", "warhead",
        "fissile", "heu",
    ],
    "deterrence": [
        # -- raw-matched phrases --
        "existential threat", "military option", "all options", "red line",
        # -- lemma-matched single words --
        # threaten is the verb lemma: "threatened/threatening" do NOT
        # lemmatize to "threat", so both entries are needed (the old
        # substring match on "threat" covered the verb forms implicitly).
        "deterrence", "retaliation", "escalation", "provocation", "coercion",
        "ultimatum", "threaten", "threat",
    ],
    "diplomacy": [
        # -- raw-matched phrases --
        "sanctions relief", "enrichment freeze", "maximum pressure",
        "diplomatic breakdown", "failed negotiations", "diplomatic channel",
        "diplomatic effort", "nuclear deal", "nuclear agreement",
        "nuclear talks", "peace talks", "nuclear diplomacy",
        "cease-fire", "de-escalation",
        # -- lemma-matched single words --
        # negotiate covers negotiated/negotiating; negotiation covers
        # negotiation(s) — distinct lemmas, both needed.
        "ceasefire", "jcpoa", "negotiate", "negotiation", "sanction",
        "dismantle",
    ],
    # Renamed from "legitimacy" (2026-08-13). The 20 terms are unchanged, but
    # the old name described only half of them: the trigger logs show the
    # cluster fires on damage claims (destroy, obliterate, destruction) far
    # more often than on legal status, and in opposite proportions in the two
    # corpora. "strike_claims" covers both halves: what was destroyed and
    # whether the strike was lawful.
    "strike_claims": [
        # -- raw-matched phrases --
        "nuclear capability degraded", "months of setback", "damage assessment",
        "regime change", "regime survival", "international law",
        "preemptive war", "bomb damage", "nuclear setback", "war crime",
        "violation of",
        # -- lemma-matched single words --
        # Outcome-claim families: verb and noun lemmas listed separately
        # (spaCy will not map "obliteration" onto "obliterate").
        "sovereignty",
        "obliteration", "obliterate",
        "annihilation", "annihilate",
        "destruction", "destructive", "destroyer", "destroy",
    ]
}

# ── Concept polarity (edge colouring; notebooks 06 & 07) ───────────────────
# Polarity of the CONCEPT itself — NOT sentence-level sentiment or stance.
# Used to set the `polarity` attribute on actor–concept edges and to profile
# actor–actor projection edges. An actor "rejecting escalation" still yields a
# negative (deterrence) edge, because the negative concept was invoked.
# strike_claims is neutral rather than positive: it carries the vocabulary of
# claimed destruction alongside the vocabulary of legality, so counting it as
# cooperative attributed "obliterated" to the cooperative share.
CONCEPT_POLARITY = {
    "diplomacy":       "positive",
    "strike_claims":   "neutral",
    "nuclear_program": "neutral",
    "deterrence":      "negative",
    "military_action": "negative",
}

# Shared edge-polarity colour palette (notebooks 06 & 07). "mixed" is used only
# for actor–actor projection edges whose shared concepts tie across polarities.
POLARITY_COLOR = {
    "positive": "#2E9E5B",  # green
    "neutral":  "#9AA0A6",  # grey
    "negative": "#D64545",  # red
    "mixed":    "#5A5A5A",  # dark grey (projected edges only)
}
