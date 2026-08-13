# Iranian-state-media alias map (IRNA / Tasnim).
#
# SEPARATE from the English src/alias_map.py by design (A5): changes here must
# never propagate back to the English pipeline. This module is imported ONLY by
# the Iranian-corpus notebooks (notebooks/iran/03b_coref_iran, 04_extract_iran).
#
# WHAT IS SHARED (source-invariant): the actor whitelist and entity types — the
# comparison is on the *same* actors — plus the English base surface forms, which
# are valid for both corpora ("tehran"->IRAN, "washington"->USA, etc.). We build
# a NEW dict from them; the shared English ALIAS_MAP is never mutated.
#
# WHAT IS IRANIAN-SPECIFIC: the surface forms below. State-aligned outlets use
# markedly different language — "the Zionist regime" for Israel, "the Great Satan"
# for the US, revolutionary honorifics for Khamenei. This divergence is itself a
# framing finding, so the additions are kept in their OWN dict and logged.
#
# STARTING POINT, NOT FINAL: per the A5 spec the comparative output must NOT be
# trusted until an empirical audit of 30-50 IRNA/Tasnim sentences extends this
# list. 04_extract_iran prints the top alias misses to drive that audit; promote
# high-frequency unresolved surface forms into ALIAS_MAP_IRAN_ADDITIONS below.

from src.alias_map import ALIAS_MAP as _EN_ALIAS_MAP  # source-invariant base
from src.alias_map import ACTOR_WHITELIST, ACTOR_TYPE  # shared: same actors compared  # noqa: F401

# Iranian-state-media-specific surface forms (the divergence — logged separately).
ALIAS_MAP_IRAN_ADDITIONS = {
    # ── ISRAEL — "Zionist regime/entity", occupation framing ───────────────
    "the zionist regime":  "ISRAEL", "zionist regime":  "ISRAEL",
    "the zionist entity":  "ISRAEL", "zionist entity":  "ISRAEL",
    "the zionists":        "ISRAEL", "zionists":        "ISRAEL",
    "the occupying regime": "ISRAEL", "occupying regime": "ISRAEL",
    "the israeli regime":  "ISRAEL", "israeli regime":  "ISRAEL",
    "the apartheid regime": "ISRAEL",

    # ── USA — "Great Satan", "global arrogance" ────────────────────────────
    "the great satan":     "USA", "great satan":     "USA",
    "the global arrogance": "USA", "global arrogance": "USA",

    # ── KHAMENEI — revolutionary honorifics ────────────────────────────────
    "supreme leader":                  "KHAMENEI",
    "the supreme leader":              "KHAMENEI",
    "leader of the islamic revolution": "KHAMENEI",
    "leader of the revolution":        "KHAMENEI",
    "imam khamenei":                   "KHAMENEI",

    # ── IRAN — self-reference + armed forces ───────────────────────────────
    "the islamic republic of iran": "IRAN",
    "irgc":                         "IRAN", "the irgc": "IRAN",
    "revolutionary guards":         "IRAN", "the revolutionary guards": "IRAN",
    "islamic revolution guards corps": "IRAN",

    # ── AUDIT PASS 1 — driven by 04_extract_iran's top alias misses ─────────
    # (frequency in parentheses; only high-confidence actor forms promoted).
    # Transliteration divergence: IRNA/Tasnim spell "Araghchi" as "Araqchi".
    "araqchi": "ARAGHCHI", "abbas araqchi": "ARAGHCHI",            # (518 / 175)
    # "Zionist" as a bare NER surface = Israel in state-media framing.
    "zionist": "ISRAEL", "the zionist": "ISRAEL",                  # (782)
    "tel aviv": "ISRAEL",                                          # (69)
    # NOTE: "us", "i.a.e.a.", "international atomic energy agency" (+"the ...")
    # were first caught by this audit but are source-INVARIANT orthography —
    # they also top the English miss log — so they were promoted to the shared
    # English base map (src/alias_map.py) and removed from here. The Iranian
    # dict is unchanged by that move (identical key -> value pairs).
    # UN Security Council (bare "UN"/"United Nations" left — maps imprecisely).
    "security council": "UN_SECURITY_COUNCIL",                     # (120)
    "the security council": "UN_SECURITY_COUNCIL",
    # Iranian MFA spokesman — the institutional Iranian voice (cf. pentagon->USA).
    "baqaei": "IRAN", "esmaeil baqaei": "IRAN",                    # (?/75)
    # NOTE: still-open forms for a deeper audit — "E3" (197, UK/FR/DE trio),
    # bare "UN"/"United Nations", "Foreign Ministry" (ambiguous owner), "the Agency".
}

# Full Iranian alias map = source-invariant English base + Iranian additions.
# (A NEW dict — the shared English ALIAS_MAP object is never modified.)
ALIAS_MAP = {**_EN_ALIAS_MAP, **ALIAS_MAP_IRAN_ADDITIONS}
