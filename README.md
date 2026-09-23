# CS05 — Investigating a Post-Drive Topological Polarization Overshoot

**CIEC® LAB — Public Evidence Portfolio · Case CS05**

**An AI-assisted scientific research case study in prior-art analysis, hypothesis competition, preregistration, reproducible analytics, and evidence-gated stopping.**

> **Final outcome:** Unresolved due to unavailable external raw data. **No mechanism claim made.**

## Why this repository exists

This repository documents a complete research workflow around a published anomaly in active liquid crystals: after acoustic activity is switched off, the reported magnitude of topological polarization briefly increases before the system proceeds into ordinary discharge.

The project did **not** begin by inventing a new mechanism. It began by asking what evidence would be required to distinguish among competing explanations, then froze that test before access to the desired external trajectories.

The investigation closed when the required charge-resolved raw data could not be obtained at the evidentiary standard specified in the preregistration.

That stopping decision is part of the result.

## Research question

**What quantitatively causes the short-lived increase in topological polarization immediately after activity is switched off?**

Three rival explanations were retained:

| ID | Rival explanation | Final status |
|---|---|---|
| H0 | Standard passive post-drive defect relaxation is sufficient | Unresolved |
| H1 | Stored elastic/director stress produces an additional charge-selective transient current | Hypothesis only / unresolved |
| H2 | Measurement/accounting effects materially create or amplify the overshoot | Unresolved |

## Research path

```text
Observed published anomaly
        ↓
Prior-art review and claim narrowing
        ↓
Three competing hypotheses
        ↓
CS05-EXP001 preregistration
        ↓
Analysis code frozen before real-data access
        ↓
Adversarial synthetic validation
        ↓
External trajectory-data dependency
        ↓
STOP — evidence access insufficient
```

## The preregistered experiment

The first test was deliberately kinematic rather than mechanistic. The planned charge-resolved accounting was:

```text
ΔP = ΔP_motion
   + ΔP_boundary
   + ΔP_birth/death
   + ΔP_unresolved
   + ε_numeric
```

with `+1/2` and `-1/2` contributions reported separately.

The test was designed to answer four questions before any new physical model was introduced:

1. Does the overshoot survive direct, unsmoothed reconstruction from tracks?
2. Which charge class physically carries it?
3. Can field boundaries or track birth/death account for it?
4. Does the same carrier reproduce across independent switch-offs?

See [`preregistration/CS05_EXP001_PREREGISTRATION.md`](preregistration/CS05_EXP001_PREREGISTRATION.md).

## What was actually executed

The **real-data** experiment was not executed because the required trajectory-level dataset was not obtained.

The **analysis software** was executed against adversarial synthetic cases before closure:

- a genuine motion-carried overshoot;
- a boundary-driven apparent overshoot;
- an unexplained-track artifact.

All frozen software-validation assertions passed.

```text
ALL_SYNTHETIC_TESTS_PASS
```

This validates the accounting logic only. It is **not physical evidence** for H0, H1, or H2.

## Reproducibility

The core analysis file in [`src/cs05_exp001_pipeline.py`](src/cs05_exp001_pipeline.py) is byte-identical to the pre-real-data frozen version.

Frozen SHA-256:

```text
1bbd0f67adb3c5f5f71160b4318e6a85411c9056921e3193929ea1e092a3bf0a
```

To run the public synthetic validation:

```bash
python -m pip install -r requirements.txt
python tests/validate_synthetic.py
```

PowerShell:

```powershell
./run_validation.ps1
```

A GitHub Actions workflow is included to execute the same validation on push and pull request.

## Final scientific status

| Question | Status |
|---|---|
| Does the published overshoot exist? | Supported by the source publication |
| Did this project independently reproduce it from raw tracks? | No |
| Does passive defect dynamics explain it? | Unresolved |
| Does stored elastic/director relaxation explain it? | Unresolved |
| Is it an accounting artifact? | Unresolved |
| Was a new physical mechanism discovered here? | **No** |
| Was a novelty claim made? | **No** |
| Was the analysis preregistered and frozen before real-data access? | **Yes** |
| Did adversarial synthetic software tests pass? | **Yes** |

See [`docs/claim_ledger.csv`](docs/claim_ledger.csv) and [`docs/final_status.md`](docs/final_status.md).

## Why the stop matters

The project intentionally did **not** replace missing evidence with:

- figure-only digitization presented as equivalent to raw trajectories;
- post-hoc simulation under the same experiment ID;
- a shifted analysis window;
- a weaker endpoint;
- a newly invented mechanism.

The investigation therefore demonstrates an evidence-gated workflow that can stop without manufacturing a discovery.

## CIEC® LAB research architecture

This case was conducted through the proprietary research architecture of **CIEC® LAB**.

The public repository exposes the evidence needed to audit the case — research question, competing hypotheses, preregistration, analysis code, validation, limitations, claim boundaries, hashes, and final status — while internal prompts, orchestration logic, decision gates, routing rules, handoff formats, thresholds, and governance remain private.

## Repository map

```text
docs/              research logic, timeline, claims, limitations
preregistration/   frozen experiment definition and schema
src/               frozen accounting pipeline
tests/             public synthetic validation harness
results/           synthetic validation outputs
reproducibility/   hashes, runbook, integrity records
evidence/          source map and public evidence index
report/            technical report and portfolio case study
```

## Source publication

The primary published phenomenon is from:

**Sokolov, A., Emersic, T., Nealey, P., de Pablo, J., & Snezhko, A. (2026). _Evidence of topological charge polarization at active-passive interfaces in acoustically powered active liquid crystals_. Physical Review Research, 8, 023060.** DOI: `10.1103/nzfb-3cps`.

This repository does not redistribute the authors' experimental data or supplementary media.

**Independence note:** This is an independent research case study and is not affiliated with, endorsed by, or presented as work of the source-paper authors, Argonne National Laboratory, the University of Chicago, the American Physical Society, or the other institutions cited here.

See [`evidence/external_sources.md`](evidence/external_sources.md).

## AI assistance disclosure

This was a human-directed, AI-assisted research project. AI systems supported literature-oriented research, hypothesis analysis, drafting, and code assistance. The internal research architecture used to organize that work is proprietary and is not disclosed in this repository.

See [`docs/ai_assistance_disclosure.md`](docs/ai_assistance_disclosure.md).

## License

This public repository is **source-visible but not open-source licensed** in this release. Copyright is retained by Ricardo Vera. See [`LICENSE`](LICENSE).

Third-party publications remain under their own licenses.

## Citation

Citation metadata are provided in [`CITATION.cff`](CITATION.cff).
