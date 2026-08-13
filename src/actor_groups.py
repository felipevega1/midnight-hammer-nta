# Analytic grouping of whitelisted actors into framing coalitions.
#
# Used by notebook 07 to aggregate framing VOLUME (summed edge weight) per
# coalition per window. The grouping is interpretive and deliberately kept
# separate from the mechanical ACTOR_WHITELIST / ALIAS_MAP, so the coalition
# reading can be revised without touching entity resolution.
#
# Coverage is exhaustive and audited against ACTOR_WHITELIST at import time
# (see the assertions at the bottom): every whitelisted actor belongs to
# exactly one group, and no group contains an actor that is not whitelisted.
ACTOR_ALIGNMENT = {
    # ── us_aligned — the striking coalition and US domestic politics ──────
    "USA": "us_aligned", "ISRAEL": "us_aligned", "NATO": "us_aligned",
    "TRUMP": "us_aligned", "NETANYAHU": "us_aligned", "HEGSETH": "us_aligned",
    "WITKOFF": "us_aligned", "RUBIO": "us_aligned", "VANCE": "us_aligned",
    "OBAMA": "us_aligned", "BIDEN": "us_aligned",
    "US_CONGRESS": "us_aligned", "US_SENATE": "us_aligned",
    "DEMOCRATS": "us_aligned", "REPUBLICANS": "us_aligned",

    # ── iran_aligned — Iran and the "Axis of Resistance" ─────────────────
    "IRAN": "iran_aligned", "KHAMENEI": "iran_aligned",
    "ARAGHCHI": "iran_aligned", "PEZESHKIAN": "iran_aligned",
    "HAMAS": "iran_aligned", "HEZBOLLAH": "iran_aligned",
    "HOUTHIS": "iran_aligned",

    # ── neutral — international institutions and the E3 negotiators ──────
    "IAEA": "neutral", "GROSSI": "neutral",
    "UN_SECURITY_COUNCIL": "neutral", "EU": "neutral",
    "FRANCE": "neutral", "GERMANY": "neutral", "UK": "neutral",

    # ── other — third-party powers, Gulf mediators, regional theatre ─────
    "RUSSIA": "other", "PUTIN": "other", "CHINA": "other",
    "QATAR": "other", "SAUDI_ARABIA": "other", "UAE": "other",
    "OMAN": "other", "BAHRAIN": "other", "GULF_STATES": "other",
    "UKRAINE": "other", "GAZA": "other", "IRAQ": "other",
    "SYRIA": "other", "YEMEN": "other", "LEBANON": "other",
}

GROUP_ORDER = ["us_aligned", "iran_aligned", "neutral", "other"]

# ── completeness audit against the whitelist ─────────────────────────────
# NOTE: "PENTAGON" was previously listed here but is NOT a canonical actor —
# ALIAS_MAP folds "the pentagon" into USA — so it could never receive volume.
from src.alias_map import ACTOR_WHITELIST  # noqa: E402

_missing = ACTOR_WHITELIST - set(ACTOR_ALIGNMENT)
_phantom = set(ACTOR_ALIGNMENT) - ACTOR_WHITELIST
assert not _missing, f"whitelisted actors without a group: {sorted(_missing)}"
assert not _phantom, f"grouped actors that are not whitelisted: {sorted(_phantom)}"
assert set(ACTOR_ALIGNMENT.values()) == set(GROUP_ORDER)
