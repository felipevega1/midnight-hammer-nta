# Midnight Hammer: Network Text Analysis pipeline

Reproducible pipeline for the temporal bipartite actor-concept networks reported
in *Network Text Analysis of Geopolitical Framing Shifts in Public Text Corpora*
(B.Sc. thesis, TUM School of Social Sciences and Technology).

It builds, for each of two independent news corpora, eight temporal bipartite
graphs of 44 actors and 5 concept clusters, plus a directed actor-actor layer
derived from subject-verb-object triples filtered through a CAMEO verb map.

## The corpora are not in this repository

The articles were retrieved from Nexis Uni and are licensed material that cannot
be redistributed. Nothing under `data/` is included.

To rebuild the corpora, run the verbatim query given in Appendix A.2 of the
thesis over the period 1 March to 31 August 2025, export the results as RTF, and
place the files as follows:

- `data/raw/` for the North American press export
- `data/iran_raw/` for the IRNA and Tasnim export

Notebook `01_parse` reads the RTF directly; no manual preprocessing is needed.

## Environment

Python 3.11, in a virtual environment named `.venv311` at the repository root.

```bash
python3.11 -m venv .venv311
.venv311/bin/pip install -r requirements.txt
```

The spaCy transformer model is a separate download:

```bash
.venv311/bin/python -m spacy download en_core_web_trf
```

The f-coref model is fetched from the HuggingFace hub on first use of notebook
`03b`. Versions in `requirements.txt` are pinned, because the NER model version
changes the actor mention counts.

## Running

```bash
./run_all.command          # North American corpus, notebooks 01 to 09
./run_all_iran.command     # Iranian corpus, same chain
./run_all_compare.command  # cross-corpus comparison, after both of the above
```

Each script executes the notebooks in filename order and stops at the first
error, so a failure in an early stage never cascades. Resume from a stage by
passing its number, for example `./run_all.command 04`.

Notebooks are stored without outputs. Running them populates `data/interim/` and
`data/output/`, including every figure and CSV table that appears in the thesis.

`data/output/` is published here, so the results can be inspected without
rebuilding the corpora: the per-window edge lists, the GraphML, GEXF and
interactive HTML exports of all thirty networks, every analysis table and every
figure. Two files are withheld, `edges/svo_triples.jsonl` and its Iranian
counterpart, because they store the subject and object spans verbatim as they
appear in the articles. Notebook `05b` regenerates them from a rebuilt corpus.

## Layout

```
notebooks/        North American chain, 13 stages plus compare_sources
notebooks/iran/   Iranian chain, the same 13 stages
src/              the dictionaries and configuration the notebooks import
data/output/      the published derived output; corpora are not included
```

The two chains are deliberate duplicates rather than one parameterised
pipeline. Each corpus keeps its own copy of every stage and its own data tree,
so a change made for one corpus cannot silently alter the results of the other.

### `src/`

| Module | Contents |
| --- | --- |
| `actor_groups.py` | actor whitelist, entity types, coalition alignment |
| `alias_map.py` | surface form to canonical actor, North American corpus |
| `alias_map_iran.py` | additional aliases for the Iranian corpus |
| `concept_dict.py` | the five concept clusters, their terms and polarity |
| `verb_map.py` | CAMEO verb map and stop verbs for the directed layer |
| `time_windows.py` | the eight asymmetric windows and their date bounds |
| `corpus_config.py` | per-corpus paths and settings |

## Pipeline stages

| Stage | Does |
| --- | --- |
| `01_parse` | RTF to structured articles |
| `02_clean` | deduplication, source filtering, metadata footer removal |
| `03_preprocess` | sentence splitting, lemmatisation |
| `03b_coref` | coreference resolution |
| `04_extract` | actor mentions by NER plus alias map, concept matches by dictionary |
| `05_edges` | actor-concept co-occurrence edges per sentence |
| `05b_svo_edges` | subject-verb-object triples, filtered by the CAMEO verb map |
| `06_networks` | the eight bipartite graphs per corpus |
| `06b_svo_networks` | the directed actor-actor layer |
| `07_analysis` | graph, node, group and dyad level metrics |
| `07b_svo_analysis` | agent ratio, reciprocity, CAMEO composition |
| `08_significance` | the pre-specified one-sided test on the buildup to climax shift |
| `09_windowing` | effective window sizes, against Diesner's SemEval benchmark |
| `compare_sources` | cross-corpus comparison, run after both chains |

Every stage reads the output of the previous one and writes its own, and prints
a checkpoint with its input and output counts before the next stage may run. No
stage modifies its predecessor's output.

## Randomness

Three places draw random numbers, and all three are seeded. Two are validation
checkpoints, where the seed only fixes which examples get printed: `03b_coref`
shows a sample of coreference rewrites before and after, and `04_extract` shows
a sample of concept matches per cluster. The third is the permutation test and
bootstrap in `08_significance`, where resampling is part of the computation and
the seed makes the reported p-value and confidence interval reproducible. No
value that reaches the networks depends on a random draw.

## Licence

Code and dictionaries are released for academic reuse. The corpora are not
included and remain subject to the Nexis Uni terms of service.
