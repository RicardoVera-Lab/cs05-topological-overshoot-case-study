# CS05 — Post-Drive Topological Polarization Overshoot

> **CIEC® LAB CASE STUDY — preregistered mechanism discrimination under external-data constraints.**

## What this case proves about CIEC LAB

CS05 demonstrates that CIEC LAB can take a published physical anomaly, turn it into competing explanations, define a discriminating experiment **before seeing the desired raw data**, freeze the analysis, validate the software against adversarial synthetic cases, and stop when the evidence requirement cannot be met without changing the rules.

That is the capability being demonstrated here:

> **not “AI that invents a mechanism,” but a research system that forces mechanism claims to survive preregistration, falsification pressure, reproducibility and evidence-access reality.**

### Public performance signals

| Verification signal | Result |
|---|---:|
| Competing physical/accounting explanations retained | **3** |
| Preregistered primary experiment | **1** |
| Frozen analysis core before real-data access | **YES** |
| Adversarial synthetic scenarios executed | **3 / 3 PASS** |
| Analysis core SHA-256 frozen | **YES** |
| GitHub Actions validation workflow | **INCLUDED** |
| Endpoint changed after evidence failure | **0 times** |
| Figure-only data promoted as raw trajectories | **0 times** |
| Post-hoc simulation substituted for the frozen experiment | **0 times** |
| Unsupported mechanism claims emitted | **0** |

The laboratory preserved a complete stopping condition instead of weakening the scientific question to manufacture a result.

---

## Executive signal

For an executive, founder, investor or R&D leader, the important point is not active liquid crystals.

The important question is:

> **Can a research system lock the test before the desired data arrive, detect when the available evidence is the wrong kind of evidence, and prevent a weak substitute from becoming a confident technical claim?**

CS05 demonstrates that behavior.

This capability transfers to:

- deep-tech due diligence;
- scientific R&D;
- model validation;
- experimental design;
- AI-assisted technical research;
- analytics integrity;
- data-access risk;
- decision intelligence.

See [Executive Signal](report/EXECUTIVE_SIGNAL.md).

---

## The scientific challenge

A published active-liquid-crystal experiment reported a short-lived increase in topological polarization immediately after acoustic activity was switched off, before ordinary discharge.

The research question was:

> **What quantitatively carries that overshoot?**

Three rival explanations were retained:

| Rival | Public status |
|---|---|
| Standard passive post-drive defect relaxation | Unresolved |
| Stored elastic/director relaxation contribution | Hypothesis only / unresolved |
| Measurement or trajectory-accounting effects | Unresolved |

The first objective was deliberately narrower than “discover a new mechanism”:

**reconstruct the polarization change from charge-resolved defect trajectories and determine what physical/accounting contribution actually carries the overshoot.**

---

## The preregistered test

The accounting model was frozen as:

```text
ΔP = ΔP_motion
   + ΔP_boundary
   + ΔP_birth/death
   + ΔP_unresolved
   + ε_numeric
```

with `+1/2` and `-1/2` defect contributions tracked separately.

The test was designed to ask:

1. Does the overshoot survive direct reconstruction from trajectories?
2. Which charge class carries it?
3. Can field boundaries or track birth/death explain it?
4. Does the same carrier reproduce across independent switch-offs?

See [Preregistration](preregistration/CS05_EXP001_PREREGISTRATION.md).

---

## What was actually executed

The required external charge-resolved trajectory dataset was not obtained.

So the real-data mechanism test was **not** executed.

What was executed was the frozen analysis software against three adversarial synthetic scenarios:

1. genuine motion-carried overshoot;
2. boundary-driven apparent overshoot;
3. unresolved-track apparent overshoot.

Result:

> **3 / 3 adversarial synthetic scenarios passed.**

This validates the accounting logic only. It does not select a real physical mechanism.

See [Synthetic Validation Report](results/synthetic_validation_report.md).

---

## Reproducibility and integrity

The primary analysis implementation was frozen before real-data access.

Frozen core SHA-256:

```text
1bbd0f67adb3c5f5f71160b4318e6a85411c9056921e3193929ea1e092a3bf0a
```

Public reproduction path:

```bash
python -m pip install -r requirements.txt
python tests/validate_synthetic.py
```

A GitHub Actions workflow is included to run the validation automatically.

See [Reproducibility Report](reproducibility/reproducibility_report.md).

---

## Why the stop is a result

When the required trajectory-level evidence could not be obtained, the project did **not**:

- replace raw trajectories with figure-only digitization;
- move the analysis window;
- weaken the endpoint;
- substitute a post-hoc simulation under the same experiment identity;
- promote one rival simply because another became difficult to test.

That is the commercially important behavior.

> **CIEC LAB preserved the value of the decision by refusing to convert evidence scarcity into technical certainty.**

The case can be reopened if suitable charge-resolved trajectory data become available.

---

## Public evidence, private machinery

This repository exposes:

- the research question;
- competing hypotheses;
- preregistration;
- frozen code;
- public synthetic validation;
- hashes;
- limitations;
- claim boundaries;
- reproducibility material;
- final research status.

CIEC LAB internal operating methods remain proprietary.

> **Public evidence. Private machinery.**

See [Public Disclosure Boundary](PUBLIC_DISCLOSURE_BOUNDARY.md).

---

## Agents involved

FORGE Ω · ALETHEIA Ω · OSINTEGA Ω · INVENTOR · SEDA Ω

No operational details are disclosed.

---

## Scientific status

| Question | Status |
|---|---|
| Is the published overshoot supported by the source publication? | **Yes** |
| Was it independently reconstructed here from raw trajectories? | **No** |
| Was a physical mechanism selected? | **No** |
| Was the primary test preregistered before real-data access? | **Yes** |
| Was the analysis core frozen? | **Yes** |
| Did adversarial synthetic software tests pass? | **Yes — 3/3** |
| Was a novelty claim made? | **No** |

**Final state:** `CLOSED — EXTERNAL DATA ACCESS BLOCK`

This is an evidence-access conclusion, not a negative physical result.

---

# CIEC® LAB

### High-reliability AI research for problems where the cost of a false technical claim is higher than the cost of stopping.

**Frame. Freeze. Attack. Verify. Decide.**
