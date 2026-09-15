# Technical Report

## CS05 — Investigating a Post-Drive Topological Polarization Overshoot

### Abstract

This report documents an independent, AI-assisted investigation of a published post-switch-off transient in acoustically powered active liquid crystals. The research program did not attempt to claim the observed anomaly as novel. Instead, it used prior-art attack to narrow the question to a specific unresolved differential: whether the transient increase in polarization can be accounted for by ordinary post-drive defect evolution, requires an additional elastic/director-release contribution, or is materially affected by trajectory/accounting artifacts. A charge-resolved accounting experiment was preregistered, implemented, and frozen before access to author-supplied raw trajectories. Adversarial synthetic validation confirmed the intended software behavior. The real-data experiment was not executed because the required external trajectory dataset was not obtained. The case therefore closes without a mechanism claim and serves as a reproducible example of evidence-gated AI-assisted research.

## 1. Problem definition

The source experiment reported a polarized layer of topological defects at an active/passive interface and discharge after activity cessation. The narrower CS05 target was the short post-switch-off interval in which the magnitude of polarization reportedly increases before ordinary relaxation.

The investigation asked:

> What quantitatively produces that overshoot?

## 2. Hypothesis competition

The research retained three rival explanations:

- **H0:** ordinary passive defect interactions and transport are sufficient;
- **H1:** stored elastic/director relaxation contributes an extra transient charge-selective current;
- **H2:** measurement/accounting effects materially produce or amplify the apparent overshoot.

The project explicitly rejected broad claims such as “new topological memory” or “new capacitor physics.”

## 3. Why accounting came before mechanism invention

A polarization-like observable constructed from signed defect positions can change through several pathways. Continuous defect motion is only one of them. Boundary entry/exit, birth/death events, unresolved tracks, and numerical processing can produce changes in the same aggregate quantity.

The first experiment was therefore built around the identity:

`ΔP = ΔP_motion + ΔP_boundary + ΔP_birth/death + ΔP_unresolved + ε_numeric`.

Positive and negative charges were required to be reported separately.

## 4. Preregistration and software freeze

The experiment fixed the source-example switch-off reference and a relative overshoot window before access to the desired raw trajectories. It also froze:

- the data schema;
- charge labels;
- accounting rules;
- unresolved-event handling;
- numerical closure tolerances;
- the dominant-carrier criterion;
- robustness logic.

The core implementation was hashed before real-data exposure.

## 5. Synthetic validation

Three adversarial test cases were constructed:

1. a true overshoot carried by negative-defect motion;
2. an apparent overshoot caused by boundary entry;
3. an apparent overshoot caused by an unresolved new track.

The pipeline correctly accepted the first and blocked the artifact cases under the preregistered logic.

Synthetic validation is interpreted strictly as software validation.

## 6. Evidence-access gate

The required trajectory-level dataset was not obtained. The project therefore did not:

- infer raw trajectories from aggregate plots;
- invent missing event labels;
- replace the experiment with a new simulation under the same ID;
- relax the endpoint after the access failure.

## 7. Final outcome

**Mechanism unresolved. No mechanism claim made.**

The research case is complete as a methodological artifact because the question was narrowed, the decisive test was preregistered and implementation-ready, and the investigation stopped at the evidence boundary rather than substituting a weaker evidentiary object.

## 8. Reopening condition

If sufficiently calibrated charge-resolved trajectories become available in the future, the frozen EXP001 pipeline can be executed. Any material change to the primary observable, window, accounting logic, or gates requires a new experiment ID and preregistration.
