#!/bin/bash
# ===========================================================================
# run_all_iran.command — execute the Islamic Republic (IRNA / Tasnim) pipeline.
#
# Parallel to and INDEPENDENT of run_all.command. The English pipeline and its
# outputs are untouched. Notebooks live in notebooks/iran/ and read
# data/iran_raw/, writing data/interim/iran/ and data/output/iran/.
#
#   ./run_all_iran.command            # all Iranian notebooks, 01 -> 07b
#   ./run_all_iran.command 04         # only 04_extract_iran
#   ./run_all_iran.command -n         # dry run
# ===========================================================================
set -o pipefail
shopt -s nullglob
cd "$(dirname "${BASH_SOURCE[0]}")" || exit 1

JUPYTER=".venv311/bin/jupyter"
pause() {
    if ( exec </dev/tty ) 2>/dev/null; then
        read -n 1 -s -r -p "Press any key to close..." </dev/tty; echo
    fi
}

DRY=0
if [ "${1:-}" = "-n" ] || [ "${1:-}" = "--dry-run" ]; then DRY=1; shift; fi
if [ ! -x "$JUPYTER" ]; then
    echo "ERROR: '$JUPYTER' not found. Create/activate the .venv311 venv first."
    pause; exit 1
fi

all_nbs=(notebooks/iran/[0-9][0-9]*.ipynb)
if [ $# -gt 0 ]; then
    nbs=()
    for nb in "${all_nbs[@]}"; do
        base="$(basename "$nb")"
        for want in "$@"; do
            case "$base" in "$want"*) nbs+=("$nb"); break ;; esac
        done
    done
else
    nbs=("${all_nbs[@]}")
fi
if [ ${#nbs[@]} -eq 0 ]; then
    echo "No Iranian notebooks matched: $*"
    echo "Available:"; printf '  %s\n' "${all_nbs[@]}"
    pause; exit 1
fi

total=${#nbs[@]}
echo "============================================================"
echo " Islamic Republic (IRNA / Tasnim) pipeline"
echo " $(date '+%Y-%m-%d %H:%M:%S')  |  $total notebook(s)"
echo "============================================================"
printf '  %s\n' "${nbs[@]}"
if [ $DRY -eq 1 ]; then echo; echo "(dry run — nothing executed)"; exit 0; fi

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
        base="$(basename "$nb")"
        echo ""
        echo "############################################################"
        echo " FAILED at [$i/$total]  $nb"
        echo " Fix the error above, then resume with: ./run_all_iran.command ${base:0:2}"
        echo "############################################################"
        pause; exit 1
    fi
    echo "    ok — $((SECONDS - nb_start))s"
done

echo ""
echo "============================================================"
echo " DONE — $total notebook(s) in $((SECONDS - pipeline_start))s"
echo " Iranian outputs in:  data/output/iran/"
echo "============================================================"
pause
