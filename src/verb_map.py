# CAMEO-grounded verb filter for SVO extraction.
# Keys are verb LEMMAS; values are CAMEO quadrant labels.
VERB_MAP = {
    # Material conflict
    "strike": "material_conflict", "bomb": "material_conflict",
    "attack": "material_conflict", "destroy": "material_conflict",
    "hit": "material_conflict", "shoot": "material_conflict",
    "target": "material_conflict", "launch": "material_conflict",
    "fire": "material_conflict", "retaliate": "material_conflict",
    # Verbal conflict
    "threaten": "verbal_conflict", "warn": "verbal_conflict",
    "condemn": "verbal_conflict", "reject": "verbal_conflict",
    "accuse": "verbal_conflict", "denounce": "verbal_conflict",
    "sanction": "verbal_conflict", "demand": "verbal_conflict",
    # Verbal cooperation
    "negotiate": "verbal_cooperation", "agree": "verbal_cooperation",
    "propose": "verbal_cooperation", "offer": "verbal_cooperation",
    "support": "verbal_cooperation", "endorse": "verbal_cooperation",
    # Material cooperation
    "verify": "material_cooperation", "inspect": "material_cooperation",
    "confirm": "material_cooperation", "allow": "material_cooperation",
}
STOP_VERBS = {
    "be", "have", "do", "will", "say", "make", "get", "go", "come",
    "take", "give", "know", "think", "see", "look", "want", "use",
    "become", "include", "continue", "add", "show", "follow", "need",
    "tell", "seem", "feel", "put", "keep", "let", "begin", "hold",
}

# CAMEO quadrant -> polarity, mirroring src/concept_dict.CONCEPT_POLARITY so the
# SVO track can reuse the shared POLARITY_COLOR palette (notebooks 06b/07b).
# CAMEO has no neutral quadrant: conflict = negative, cooperation = positive.
CAMEO_POLARITY = {
    "material_conflict":    "negative",
    "verbal_conflict":      "negative",
    "verbal_cooperation":   "positive",
    "material_cooperation": "positive",
}
