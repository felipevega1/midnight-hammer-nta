#!/bin/bash
# ===========================================================================
# run_all_compare.command — run the Iranian pipeline, then the cross-corpus
# comparison notebook (English vs Islamic Republic).
#
# Assumes the English pipeline outputs already exist (the frozen baseline). It
# does NOT re-run the English pipeline — run ./run_all.command yourself if the
# English outputs are missing or stale.
# ===========================================================================
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")" || exit 1

JUPYTER=".venv311/bin/jupyter"
pause() {
    if ( exec </dev/tty ) 2>/dev/null; then
        read -n 1 -s -r -p "Press any key to close..." </dev/tty; echo
    fi
}

if [ ! -f data/interim/corpus_clean.jsonl ]; then
    echo "ERROR: English outputs missing (data/interim/corpus_clean.jsonl)."
    echo "Run ./run_all.command first — the comparison needs both corpora."
    pause; exit 1
fi

echo "=== Step 1/2: Islamic Republic pipeline ==="
if ! ./run_all_iran.command; then
    echo "Iranian pipeline failed — see above."; pause; exit 1
fi

echo ""
echo "=== Step 2/2: cross-corpus comparison ==="
if ! "$JUPYTER" nbconvert --to notebook --execute --inplace \
        --ExecutePreprocessor.timeout=-1 notebooks/compare_sources.ipynb; then
    echo "Comparison notebook failed — see above."; pause; exit 1
fi

echo ""
echo "Done — comparison outputs in data/output/compare/"
pause
