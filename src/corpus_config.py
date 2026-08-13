"""Corpus parameterisation for the UNIFIED pipeline (notebooks_unified/).

The dual pipeline (notebooks/ + notebooks/iran/) does not import this module and
is unaffected by it. This exists so one set of notebooks can serve both corpora,
selected by environment variable, and so a verification run can write to a
parallel tree for byte-comparison against the dual pipeline's output.

    MH_CORPUS       'na' (default) | 'iran'
    MH_TREE_SUFFIX  appended to the interim/ and output/ directory names, e.g.
                    '_unified' -> data/interim_unified, data/output_unified.
                    Empty (default) writes to the canonical trees.

RAW_DIR never takes the suffix: raw exports are read-only inputs shared by both.

Every path below is the exact path the corresponding dual-pipeline notebook
uses, so with MH_TREE_SUFFIX unset the two pipelines are interchangeable.
"""
import os
import sys
from pathlib import Path

CORPUS = os.environ.get('MH_CORPUS', 'na').strip().lower()
if CORPUS not in ('na', 'iran'):
    raise ValueError(
        f"MH_CORPUS must be 'na' or 'iran', got {CORPUS!r}. "
        "Unset it to default to 'na'."
    )

_SUFFIX = os.environ.get('MH_TREE_SUFFIX', '')

_cwd = Path().resolve()
ROOT = next((p for p in [_cwd] + list(_cwd.parents) if (p / 'src').is_dir()), _cwd)
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

_DATA = ROOT / 'data'

# ── inputs (never suffixed) ────────────────────────────────────────────────
RAW_DIR = _DATA / ('raw' if CORPUS == 'na' else 'iran_raw')

# ── working + output trees ─────────────────────────────────────────────────
_INTERIM_BASE = _DATA / f'interim{_SUFFIX}'
_OUTPUT_BASE = _DATA / f'output{_SUFFIX}'

INTERIM_DIR = _INTERIM_BASE if CORPUS == 'na' else _INTERIM_BASE / 'iran'
OUTPUT_DIR = _OUTPUT_BASE if CORPUS == 'na' else _OUTPUT_BASE / 'iran'

EDGES_DIR = OUTPUT_DIR / 'edges'
NETWORKS_DIR = OUTPUT_DIR / 'networks'
FIGURES_DIR = OUTPUT_DIR / 'analysis' / 'corpus'
REPORTS_DIR = OUTPUT_DIR / 'reports'

# ── dictionaries ───────────────────────────────────────────────────────────
# The whitelist and entity types are SHARED by design: the cross-corpus
# comparison is on the same actors. Only the surface-form map differs, since
# state media uses markedly different designators.
from src.alias_map import ACTOR_WHITELIST, ACTOR_TYPE  # noqa: E402,F401

if CORPUS == 'na':
    from src.alias_map import ALIAS_MAP  # noqa: E402
else:
    from src.alias_map_iran import ALIAS_MAP  # noqa: E402,F811


def banner() -> str:
    """One-line provenance string for the notebooks to print."""
    name = 'North American press' if CORPUS == 'na' else 'Iranian state media'
    tree = f" (tree suffix {_SUFFIX!r})" if _SUFFIX else ''
    return (f"CORPUS={CORPUS}  [{name}]{tree}\n"
            f"  raw     : {RAW_DIR}\n"
            f"  interim : {INTERIM_DIR}\n"
            f"  output  : {OUTPUT_DIR}\n"
            f"  aliases : {len(ALIAS_MAP)} entries, {len(ACTOR_WHITELIST)} actors")
