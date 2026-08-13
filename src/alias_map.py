# Maps surface forms (lowercased, stripped) to canonical actor IDs.
# Built up iteratively by inspecting the "Top alias misses" output of
# notebook 04 — high-frequency unresolved surface forms get promoted here.

ALIAS_MAP = {
    # ── USA ───────────────────────────────────────────────────────
    "washington":             "USA",
    "the us":                 "USA",
    # Bare "US" — only NER-tagged surfaces reach this lookup, so the pronoun
    # "us" is never consulted here. Top alias miss in both corpora (EN: 1558).
    "us":                     "USA",
    "u.s.":                   "USA",
    "u.s":                    "USA",
    "the u.s.":               "USA",
    "the u.s":                "USA",
    "u.s.a.":                 "USA",
    "u.s.a":                  "USA",
    "united states":          "USA",
    "the united states":      "USA",
    "america":                "USA",
    "american":               "USA",
    "americans":              "USA",
    "the white house":        "USA",
    "white house":            "USA",
    "the administration":     "USA",
    "trump administration":   "USA",
    "the trump administration": "USA",
    "us administration":      "USA",
    "u.s. administration":    "USA",
    "the pentagon":           "USA",
    "pentagon":               "USA",
    # US combatant commands -> USA (institutional voice, cf. pentagon).
    # Lookup is exact on the lowercased NER span, so the bare acronym alone
    # caught only 41 of ~125 Western mentions; the spelled-out spans below are
    # the actual NER surfaces observed in data/interim/sentences.jsonl.
    "centcom":                "USA",
    "uscentcom":              "USA",
    "central command":        "USA",
    "the central command":    "USA",
    "us central command":     "USA",
    "u.s. central command":   "USA",
    "the us central command": "USA",
    "the u.s. central command": "USA",
    "united states central command":     "USA",
    "the united states central command": "USA",
    "us air forces central command":     "USA",
    "u.s. air forces central command":   "USA",
    "united states air forces central command":     "USA",
    "the united states air forces central command": "USA",
    "cyber command":          "USA",
    "the cyber command":      "USA",
    "us cyber command":       "USA",
    "u.s. cyber command":     "USA",
    "indo-pacific command":   "USA",
    "the indo-pacific command": "USA",
    "us indo-pacific command":  "USA",
    "u.s. indo-pacific command":     "USA",
    "the u.s. indo-pacific command": "USA",
    "naval special warfare command":     "USA",
    "the naval special warfare command": "USA",
    "air force global strike command":     "USA",
    "the air force global strike command": "USA",
    "european command":       "USA",
    "the european command":   "USA",
    "us military":            "USA",
    "u.s. military":          "USA",
    "american forces":        "USA",
    "american military":      "USA",
    "u.s. forces":            "USA",
    "us forces":              "USA",

    # ── IRAN ──────────────────────────────────────────────────────
    "the regime":             "IRAN",
    "islamic republic":       "IRAN",
    "the islamic republic":   "IRAN",
    "tehran":                 "IRAN",
    "iranian":                "IRAN",
    "iranians":               "IRAN",
    "iran's leadership":      "IRAN",
    "iranian leadership":     "IRAN",
    "iranian government":     "IRAN",
    "iranian regime":         "IRAN",

    # ── ISRAEL ────────────────────────────────────────────────────
    "idf":                    "ISRAEL",
    # IDF Home Front Command (civil defence) — Israeli, NOT a US command.
    "home front command":     "ISRAEL",
    "the home front command": "ISRAEL",
    "israeli air force":      "ISRAEL",
    "iaf":                    "ISRAEL",
    "israeli military":       "ISRAEL",
    "israeli forces":         "ISRAEL",
    "israeli":                "ISRAEL",
    "israelis":               "ISRAEL",
    "jerusalem":              "ISRAEL",
    "israeli government":     "ISRAEL",

    # ── RUSSIA ────────────────────────────────────────────────────
    "russian":                "RUSSIA",
    "russians":               "RUSSIA",
    "moscow":                 "RUSSIA",
    "the kremlin":            "RUSSIA",
    "kremlin":                "RUSSIA",
    "russian government":     "RUSSIA",

    # ── CHINA ─────────────────────────────────────────────────────
    "chinese":                "CHINA",
    "beijing":                "CHINA",
    "the chinese government": "CHINA",

    # ── UK (added 2026-08 per supervisor decision) ────────────────
    # Exact-match lookup on the lowercased NER span, so the many non-state
    # spans observed in the corpus are safe and NOT captured here:
    # "Reform UK", "British Columbia", "British Airways", "British Council",
    # "the London School of Economics", "New England", "Gordon R. England".
    # "england" is deliberately NOT mapped: it is a constituent country whose
    # standalone use in this corpus is mostly non-governmental, and the risk of
    # picking up "New England" / surnames outweighs the ~24 legitimate hits.
    # Consistent with FRANCE/GERMANY, the head of government (Starmer, 98
    # mentions) is NOT mapped -- their leaders are not mapped either, and doing
    # it only for the UK would inflate one member of the neutral coalition.
    "uk":                     "UK",
    "u.k.":                   "UK",
    "u.k":                    "UK",
    "the uk":                 "UK",
    "the u.k.":               "UK",
    "the u.k":                "UK",
    "britain":                "UK",
    "great britain":          "UK",
    "united kingdom":         "UK",
    "the united kingdom":     "UK",
    "british":                "UK",
    "the british":            "UK",
    "london":                 "UK",          # metonym, cf. "washington" -> USA
    "downing street":         "UK",
    "10 downing street":      "UK",
    "uk government":          "UK",
    "the uk government":      "UK",
    "british government":     "UK",
    "the british government": "UK",

    # ── EU ────────────────────────────────────────────────────────
    "european":               "EU",
    "europeans":              "EU",
    "european union":         "EU",
    "the european union":     "EU",

    # ── SAUDI_ARABIA (new) ────────────────────────────────────────
    "saudi arabia":           "SAUDI_ARABIA",
    "saudis":                 "SAUDI_ARABIA",
    "saudi":                  "SAUDI_ARABIA",
    "kingdom of saudi arabia": "SAUDI_ARABIA",
    "riyadh":                 "SAUDI_ARABIA",

    # ── UAE (new) ─────────────────────────────────────────────────
    "uae":                    "UAE",
    "u.a.e.":                 "UAE",
    "emirates":               "UAE",
    "the emirates":           "UAE",
    "united arab emirates":   "UAE",
    "the united arab emirates": "UAE",
    "emirati":                "UAE",
    "abu dhabi":              "UAE",
    "dubai":                  "UAE",

    # ── OMAN (new) ────────────────────────────────────────────────
    "oman":                   "OMAN",
    "omani":                  "OMAN",
    "muscat":                 "OMAN",

    # ── BAHRAIN (new) ─────────────────────────────────────────────
    "bahrain":                "BAHRAIN",
    "bahraini":               "BAHRAIN",
    "manama":                 "BAHRAIN",

    # ── GULF_STATES (new — regional aggregate) ────────────────────
    # The phrase appears separately from individual countries; we keep
    # both so sentences referencing the group are not lost.
    "gulf states":            "GULF_STATES",
    "the gulf states":        "GULF_STATES",
    "the gulf":               "GULF_STATES",
    "persian gulf":           "GULF_STATES",
    "the persian gulf":       "GULF_STATES",
    "gulf countries":         "GULF_STATES",
    "arabian gulf":           "GULF_STATES",

    # ── US_CONGRESS / US_SENATE (new) ─────────────────────────────
    "congress":               "US_CONGRESS",
    "the congress":           "US_CONGRESS",
    "u.s. congress":          "US_CONGRESS",
    "us congress":            "US_CONGRESS",
    "senate":                 "US_SENATE",
    "the senate":             "US_SENATE",
    "u.s. senate":            "US_SENATE",
    "us senate":              "US_SENATE",

    # ── IAEA — full-name / punctuated forms (bare "IAEA" resolves via
    # the upper-snake fallback; these variants do not) ────────────
    "i.a.e.a.":                               "IAEA",
    "international atomic energy agency":     "IAEA",
    "the international atomic energy agency": "IAEA",

    # ── NATO — long forms (bare "NATO" resolves via the upper-snake
    # fallback; these do not) ─────────────────────────────────────
    "supreme allied command europe":     "NATO",
    "the supreme allied command europe": "NATO",
    "north atlantic treaty organization":     "NATO",
    "the north atlantic treaty organization": "NATO",

    # ── PEOPLE — long-form / titled variants ──────────────────────
    "donald trump":           "TRUMP",
    "president trump":        "TRUMP",
    "president donald trump": "TRUMP",
    "mr. trump":              "TRUMP",

    "ali khamenei":              "KHAMENEI",
    "ayatollah khamenei":        "KHAMENEI",
    "ayatollah ali khamenei":    "KHAMENEI",
    "supreme leader khamenei":   "KHAMENEI",
    "supreme leader ali khamenei": "KHAMENEI",

    "masoud pezeshkian":      "PEZESHKIAN",
    "president pezeshkian":   "PEZESHKIAN",

    "benjamin netanyahu":     "NETANYAHU",
    "prime minister netanyahu": "NETANYAHU",

    "abbas araghchi":         "ARAGHCHI",
    "foreign minister araghchi": "ARAGHCHI",

    "steve witkoff":          "WITKOFF",
    "mr. witkoff":            "WITKOFF",

    "vladimir putin":         "PUTIN",
    "president putin":        "PUTIN",
    "putin":                  "PUTIN",
    "mr. putin":              "PUTIN",

    "rafael grossi":          "GROSSI",
    "rafael mariano grossi":  "GROSSI",

    "pete hegseth":           "HEGSETH",

    # ── RUBIO (new — Secretary of State) ──────────────────────────
    "marco rubio":            "RUBIO",
    "rubio":                  "RUBIO",
    "secretary rubio":        "RUBIO",
    "secretary of state rubio": "RUBIO",

    # ── VANCE (new — Vice President) ──────────────────────────────
    "j.d. vance":             "VANCE",
    "j.d vance":              "VANCE",
    "jd vance":               "VANCE",
    "vance":                  "VANCE",
    "vice president vance":   "VANCE",

    # ── Whitelist expansion (2026-07): regional theater states ────
    # Bare country names resolve via the upper-snake fallback; these
    # cover demonym / capital / variant surfaces.
    "ukrainian":              "UKRAINE",
    "ukrainians":             "UKRAINE",
    "kyiv":                   "UKRAINE",
    "gaza strip":             "GAZA",
    "the gaza strip":         "GAZA",
    "gazans":                 "GAZA",
    "iraqi":                  "IRAQ",
    "iraqis":                 "IRAQ",
    "baghdad":                "IRAQ",
    "syrian":                 "SYRIA",
    "syrians":                "SYRIA",
    "damascus":               "SYRIA",
    "french":                 "FRANCE",
    "paris":                  "FRANCE",
    "german":                 "GERMANY",
    "germans":                "GERMANY",
    "berlin":                 "GERMANY",
    "yemeni":                 "YEMEN",
    "yemenis":                "YEMEN",
    "sanaa":                  "YEMEN",
    "sana'a":                 "YEMEN",
    "lebanese":               "LEBANON",
    "beirut":                 "LEBANON",

    # ── Non-state armed groups ("Axis of Resistance") ─────────────
    "hizbollah":              "HEZBOLLAH",
    "hizbullah":              "HEZBOLLAH",
    "houthi":                 "HOUTHIS",
    "the houthis":            "HOUTHIS",
    "ansar allah":            "HOUTHIS",
    "ansarallah":             "HOUTHIS",

    # ── Former US presidents ──────────────────────────────────────
    "barack obama":           "OBAMA",
    "president obama":        "OBAMA",
    "mr. obama":              "OBAMA",
    "joe biden":              "BIDEN",
    "president biden":        "BIDEN",
    "mr. biden":              "BIDEN",
    # Historical (pre-2025) government -> the person, NOT USA — unlike
    # "trump administration" -> USA, which is the sitting government.
    "biden administration":   "BIDEN",
    "the biden administration": "BIDEN",
    "obama administration":   "OBAMA",
    "the obama administration": "OBAMA",

    # ── US political parties (NER tags these NORP/ORG) ────────────
    "democrat":               "DEMOCRATS",
    "democrats":              "DEMOCRATS",
    "democratic":             "DEMOCRATS",
    "democratic party":       "DEMOCRATS",
    "the democratic party":   "DEMOCRATS",
    "republican":             "REPUBLICANS",
    "republicans":            "REPUBLICANS",
    "republican party":       "REPUBLICANS",
    "the republican party":   "REPUBLICANS",
    "gop":                    "REPUBLICANS",
    "the gop":                "REPUBLICANS",

    # ── EVENT ANCHORS — discarded (not actor nodes) ───────────────
    "midnight hammer":           "EVENT_ANCHOR",
    "operation midnight hammer": "EVENT_ANCHOR",
    "the strikes":               "EVENT_ANCHOR",
    "the attack":                "EVENT_ANCHOR",
    "twelve-day war":            "EVENT_ANCHOR",
    "the war":                   "EVENT_ANCHOR",
}

# Whitelist of canonical actor IDs that become nodes in the network.
ACTOR_WHITELIST = {
    # Countries / regions
    "USA", "IRAN", "ISRAEL", "QATAR", "RUSSIA", "CHINA",
    "SAUDI_ARABIA", "UAE", "OMAN", "BAHRAIN", "GULF_STATES",
    "UKRAINE", "GAZA", "IRAQ", "SYRIA", "FRANCE", "GERMANY",
    "YEMEN", "LEBANON", "UK",
    # People
    "TRUMP", "KHAMENEI", "HEGSETH", "GROSSI", "NETANYAHU",
    "ARAGHCHI", "PEZESHKIAN", "WITKOFF", "PUTIN",
    "RUBIO", "VANCE", "OBAMA", "BIDEN",
    # Institutions / non-state groups / parties
    "IAEA", "UN_SECURITY_COUNCIL", "NATO", "EU",
    "US_CONGRESS", "US_SENATE",
    "HAMAS", "HEZBOLLAH", "HOUTHIS",
    "DEMOCRATS", "REPUBLICANS",
}

# Entity type per whitelisted actor (spaCy NER categories). Stored as the
# `entity_type` node attribute in the GraphML for optional partitioning in
# Gephi. NOT used for node colour/shape in pyvis — too many categories to stay
# readable; nodes there carry only a two-way actor/concept distinction.
ACTOR_TYPE = {
    # GPE — countries / regions
    "USA": "GPE", "IRAN": "GPE", "ISRAEL": "GPE", "QATAR": "GPE",
    "RUSSIA": "GPE", "CHINA": "GPE", "SAUDI_ARABIA": "GPE", "UAE": "GPE",
    "OMAN": "GPE", "BAHRAIN": "GPE", "GULF_STATES": "GPE",
    "UKRAINE": "GPE", "GAZA": "GPE", "IRAQ": "GPE", "SYRIA": "GPE",
    "FRANCE": "GPE", "GERMANY": "GPE", "YEMEN": "GPE", "LEBANON": "GPE",
    "UK": "GPE",
    # PERSON — named individuals
    "TRUMP": "PERSON", "KHAMENEI": "PERSON", "NETANYAHU": "PERSON",
    "ARAGHCHI": "PERSON", "PEZESHKIAN": "PERSON", "WITKOFF": "PERSON",
    "PUTIN": "PERSON", "GROSSI": "PERSON", "HEGSETH": "PERSON",
    "RUBIO": "PERSON", "VANCE": "PERSON", "OBAMA": "PERSON", "BIDEN": "PERSON",
    # ORG — institutions, non-state armed groups, parties
    "IAEA": "ORG", "UN_SECURITY_COUNCIL": "ORG", "NATO": "ORG", "EU": "ORG",
    "US_CONGRESS": "ORG", "US_SENATE": "ORG",
    "HAMAS": "ORG", "HEZBOLLAH": "ORG", "HOUTHIS": "ORG",
    "DEMOCRATS": "ORG", "REPUBLICANS": "ORG",
}
