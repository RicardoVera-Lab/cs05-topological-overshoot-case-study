# CS05 — REPRODUCIBILITY REPORT

## Completed before real-data access
- real-data lock;
- data schema;
- frozen configuration template;
- accounting pipeline;
- synthetic-test harness;
- synthetic tracks;
- synthetic configuration;
- synthetic result output;
- real-data runbook;
- SHA-256 freeze.

## Frozen core hashes

`01_REAL_DATA_LOCK.md`  
`02def85c25960a9831109fe858db4a98d9b3d883d06b259afee782c0f7d53958`

`02_DATA_SCHEMA.json`  
`ebe82f2aecf166410ab25f5dbf24a6f40be8e7fcc8a071f76dfa4626148bdbdb`

`03_FROZEN_CONFIG_TEMPLATE.json`  
`b47ceb1d2db4f38a48bd87df2abf042f49e12d6510d3db597d879f19f6e3e4ab`

`cs05_exp001_pipeline.py`  
`1bbd0f67adb3c5f5f71160b4318e6a85411c9056921e3193929ea1e092a3bf0a`

`validate_synthetic.py`  
`ea1f4bbd33a966e3633ddaa987c0beec22b1c7ddf07848384f6df6bc4e14eacf`

## Reproducible now
A third party can reproduce the synthetic accounting tests, exact accounting-closure behavior, boundary-artifact discrimination, unresolved-event gating and the frozen software state.

## Not reproducible from this package
The real experimental mechanism analysis cannot be reproduced because the required external trajectories were not obtained.

The package contains no third-party raw experimental data.

## Integrity rule
Any future real-data execution should preserve the frozen analysis core. Material modifications after seeing real data require a new experiment identifier and new freeze.
