# CS05 — One-Page Portfolio Summary

**CIEC® LAB — Public Evidence Portfolio**

## Investigating a Post-Drive Topological Polarization Overshoot

**Independent AI-assisted research case in reproducible analysis and evidence-gated decision making.**

### The challenge

A published active-liquid-crystal experiment reported a brief increase in topological polarization immediately after acoustic activity was switched off, before ordinary discharge.

The task was to determine what evidence would distinguish among ordinary passive defect relaxation, stored elastic/director release, and measurement/accounting effects.

### What I did

- narrowed the broad scientific claim through prior-art review;
- retained three competing explanations;
- preregistered a discriminating experiment before real-data access;
- implemented a charge-resolved Python accounting pipeline;
- froze the core analysis with SHA-256;
- validated the logic against adversarial synthetic cases;
- stopped the investigation when the required external raw trajectories were not obtained.

### Technical core

`ΔP = ΔP_motion + ΔP_boundary + ΔP_birth/death + ΔP_unresolved + ε_numeric`

The pipeline reports `+1/2` and `-1/2` defect contributions separately and is designed to distinguish genuine motion-carried changes from boundary and unresolved-track artifacts.

### Outcome

**Mechanism unresolved. No physical-discovery claim and no novelty claim made.**

The real-data experiment was not executed because the required external trajectory-level evidence was unavailable at the preregistered standard.

### What this demonstrates

- analytical problem framing;
- Python and reproducible analysis;
- hypothesis testing and falsification;
- preregistration and integrity controls;
- technical research and prior-art review;
- uncertainty management;
- evidence-based stopping;
- AI-assisted research direction without delegating claim authority to AI.

### Public evidence

Repository: `https://github.com/RicardoVera-Lab/cs05-topological-overshoot-case-study`

Release: `v1.0.0`

Technical report, code, preregistration, synthetic tests, hashes, claim ledger, and limitations are publicly available.

### Proprietary boundary

This case was executed through the proprietary research architecture of **CIEC® LAB**. Internal prompts, orchestration, routing, thresholds, handoffs, decision gates, and governance are not disclosed.
