# S003 evidence hashes (SHA-256)

Lines of the form `hash` `repo-path` are re-verified by `validation/validate_governance.py` in CI. Paths prefixed `scratch:` were local-only (not committed) and are recorded for provenance.

Environment: Python 3.13.16, gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0, Linux 6.18.44-fc-v114 x86_64, 4 cores, 15 GiB. Execution 2026-10-12 13:07–14:18 UTC; wall-clock budget used ≈ 71 min of 180.

## Preregistration and tools (repository)
- `8e8bc65d0cf3a0392ebb19dba4176975dfc14ae3d6a96196bb128c1765afe084` `sessions/S003/PLAN.md`
- `6ce55071e5f9a75b323a76a8517e7b1245ceaf61ab31a3a19a9e57d5590433c2` `sessions/S003/PLAN_AMENDMENT_1.md`
- `b6d431c460620efeab348b7d2b07078ea86f2e0138124cfe922f25015e0e63f6` `tools/cam_s003_fwd.c`
- `ba7309895bcf133777abe3c8ffa61c43981c740450e199114065d42c655e8252` `tools/cam_s003_rev.c`
- `b57ccf320cd66f57381a5c33b865ab6cb10efcd38010825a21e3b820807e2cbb` `tools/cam_s003_pyrev.py`
- `2f2b474d1ed474f1c310a42f5f43e134e2d696ce261553452330e408baa98f65` `tools/cam_s003_as.c`
- `af4d1cca25b12c52aa154cef037cef220037953a685cd7145e77d77a90e7765f` `tools/cam_s003_cert.py`
- `45f32196342999d97320f53be8745459fe400ae275b76d7e239fb200af8147be` `tools/cam_s003_graphs.py`
- `caed12fcc952276071a379aa2fc41029c7276a78b04789c2165b7d6a4c8e96b7` `tools/cam_s003_run.py`
- `95c7ea5b2239ec4c0dbebd415396cbbe30d10ea4ae8647b8bd351651c18e9b25` `tools/cam_s003_trees.py`

## Evidence (repository)
- `5520c5e434b5ed501b13306fb6487c0930b85a0136264f986829032fc5a5055e` `evidence/S003/cert_P4_stack_t12.json`
- `2e2853e52e074205730cbea3bf1ef47d4451bef8ca407ad7cd39b98326f7b95c` `evidence/S003/cert_bull_clear_t12.json`
- `0dc46fcbeb406d52c440e074fe228a102a96625228b7941f2a5a398726531307` `evidence/S003/cert_bull_stack_t12.json`
- `e96d2cb5cd40d2571df833fb4dee5f4123fcf5c564324e61391db704724adfc9` `evidence/S003/T1_analysis.json`
- `d1c71dbaf9204313d7cccb7b0e620d76d81178745d05cd0366a6ba249da6077d` `evidence/S003/T2_analysis.json`
- `afd2dd39a5bf63f3591b771b6702f77944dc984ac1a85f53de533e31e6117805` `evidence/S003/T2b_analysis.json`
- `70857964146e8b5751e2ff39f8c52708509faa698f289afef08bcfc26dbef33c` `evidence/S003/T3_trees.json`
- `44326102ab3d75625b98c6fff418128bf1f7dfb5829b85c216a4799a7eda08b7` `evidence/S003/T4_analysis.json`
- `5ab02048b072ea5757449d191696188c8c8a0a494fb277a14438d7e89b9dd6a6` `evidence/S003/A3_n8_analysis.json.xz`
- `91abf6fd016da2ea64178b65c857e9ddadd96c2ca4206be508df527db2c5568a` `evidence/S003/raw_summaries.tar.xz`

## Local-only provenance (not committed)
- `cbc9877b3ce37e720f2305333a21d0078ac2e31f57991c03baedcb4683c27313` `scratch:arXiv 2610.09650v1 PDF`
- `ab34962a77a7caa4126d07430e48ba47b04c57f5ef71c21f85803cf959cbabed` `scratch:arXiv 2604.22341v1 PDF`
- `24c2d4fda8473ed7782226d6530fd76a6ed5050bea07c933e0d1c8346d14af09` `scratch:A3 full per-layer rows and fingerprints (A3_raw.tar.xz, 5.0 MB)`
- authors' atlas repository read-only clone: `lajossoukup/pebbling` commit `701cdd93dd19869a9b90947edd6361efd81cfc1f`

## Pre-run tool hashes (13:11:42Z, before the T1 run) and later edits
- pre-run `b6d431c460620efeab348b7d2b07078ea86f2e0138124cfe922f25015e0e63f6` tools/cam_s003_fwd.c
- pre-run `ba7309895bcf133777abe3c8ffa61c43981c740450e199114065d42c655e8252` tools/cam_s003_rev.c
- pre-run `ae80ffe69e790a8aa0a6eefda751fd63e968bf905ede676a796fad1209227224` tools/cam_s003_graphs.py
- pre-run `b57ccf320cd66f57381a5c33b865ab6cb10efcd38010825a21e3b820807e2cbb` tools/cam_s003_pyrev.py
- pre-run `3e7355f39044cd0e52abfe57c90b476ff886aca5f24df6b5cd8a969f5682c6a2` tools/cam_s003_run.py

The following edits were made after those hashes; none changes any computed number:
- `cam_s003_run.py`: added tier A3 and an option to skip the reverse check for graphs above the cap. This was made while T1/T4/T2 were already running (already-loaded code unaffected) and before T2b/A3 started. It applies only to A3.
- `cam_s003_graphs.py`: added the n=8 counts to the assertion tables and the AHU tree generator.
- New tools written after the pre-run hashes, before their first evidential use: `cam_s003_as.c` (one dead line removed before use), `cam_s003_cert.py`, `cam_s003_trees.py` (memory limit added after a first attempt was killed).
