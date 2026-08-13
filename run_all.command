#!/bin/bash
# ===========================================================================
# run_all.command — execute the full Midnight Hammer notebook pipeline.
#
#   Double-click in Finder, or run from a terminal:
#
#     ./run_all.command            # run every notebook, in order 01 -> 07
#     ./run_all.command 03         # run only notebook 03
#     ./run_all.command 03 04 05   # run a subset (still in on-disk order)
#     ./run_all.command -n         # dry run: list what WOULD run, execute nothing
#
# Each notebook is executed *in place* — its saved outputs are refreshed.
# Execution stops at the first notebook that errors, so a failure in an early
# stage never cascades into later ones. Resume from a stage with its number,
# e.g.  ./run_all.command 04
#
# Note: running 01–06 reparses and reprocesses the whole corpus (spaCy
# transformer NER in 03/04 is the slow part — minutes, not seconds).
# ===========================================================================
set -o pipefail
shopt -s nullglob

# Work from this script's own folder (matters when double-clicked from Finder,
# where the initial working directory is the user's home).
cd "$(dirname "${BASH_SOURCE[0]}")" || exit 1

JUPYTER=".venv311/bin/jupyter"
# Note: do NOT force MPLBACKEND. The notebooks rely on ipykernel's default
# inline backend, which renders correctly under nbconvert AND embeds the
# figures into the notebook. Forcing Agg would drop the inline figure outputs.

# Pause so a double-clicked Terminal window stays readable. Only waits when a
# controlling terminal exists (i.e. launched from Finder); headless/CI runs
# skip it silently and never hang.
pause() {
    if ( exec </dev/tty ) 2>/dev/null; then
        read -n 1 -s -r -p "Press any key to close..." </dev/tty
        echo
    fi
}

# --- parse args ------------------------------------------------------------
DRY=0
if [ "${1:-}" = "-n" ] || [ "${1:-}" = "--dry-run" ]; then
    DRY=1; shift
fi

if [ ! -x "$JUPYTER" ]; then
    echo "ERROR: '$JUPYTER' not found."
    echo "Expected the project virtualenv at .venv311/. Create/activate it first,"
    echo "or edit the JUPYTER path near the top of this script."
    pause; exit 1
fi

# --- select notebooks ------------------------------------------------------
# [0-9][0-9]* (not ..._*) so lettered stages like 03b_coref are included;
# lexical sort places 03_preprocess before 03b_coref before 04_extract.
all_nbs=(notebooks/[0-9][0-9]*.ipynb)
if [ $# -gt 0 ]; then
    nbs=()
    for nb in "${all_nbs[@]}"; do
        base="$(basename "$nb")"
        for want in "$@"; do
            case "$base" in
                "$want"*) nbs+=("$nb"); break ;;
            esac
        done
    done
else
    nbs=("${all_nbs[@]}")
fi

if [ ${#nbs[@]} -eq 0 ]; then
    echo "No notebooks matched: $*"
    echo "Available:"; printf '  %s\n' "${all_nbs[@]}"
    pause; exit 1
fi

total=${#nbs[@]}
echo "============================================================"
echo " Midnight Hammer pipeline"
echo " $(date '+%Y-%m-%d %H:%M:%S')  |  $total notebook(s)"
echo "============================================================"
printf '  %s\n' "${nbs[@]}"

if [ $DRY -eq 1 ]; then
    echo ""
    echo "(dry run — nothing executed)"
    exit 0
fi

# --- run -------------------------------------------------------------------
pipeline_start=$SECONDS
i=0
for nb in "${nbs[@]}"; do
    i=$((i + 1))
    echo ""
    echo "------------------------------------------------------------"
    echo "[$i/$total] executing  $nb"
    echo "------------------------------------------------------------"
    nb_start=$SECONDS
    if ! "$JUPYTER" nbconvert --to notebook --execute --inplace \
            --ExecutePreprocessor.timeout=-1 "$nb"; then
        num="$(basename "$nb")"; num="${num:0:2}"
        echo ""
        echo "############################################################"
        echo " FAILED at [$i/$total]  $nb"
        echo " Pipeline stopped. Fix the error above, then resume with:"
        echo "     ./run_all.command $num"
        echo "############################################################"
        pause; exit 1
    fi
    echo "    ok — $((SECONDS - nb_start))s"
done

echo ""
echo "============================================================"
echo " DONE — $total notebook(s) in $((SECONDS - pipeline_start))s"
echo " Figures refreshed in:  data/output/figures/"
echo "============================================================"
pause
