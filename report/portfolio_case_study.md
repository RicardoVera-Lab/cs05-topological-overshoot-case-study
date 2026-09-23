# CS05 — Portfolio Case Study

**CIEC® LAB — Public Evidence Portfolio**

## Investigating a Post-Drive Topological Polarization Overshoot

**Independent AI-assisted research case in hypothesis competition, preregistration, reproducible analytics, and evidence-gated stopping.**

> **Final outcome:** Unresolved due to unavailable external raw data. **No mechanism claim made.**

## 1. The challenge

A published active-liquid-crystal experiment reported a short-lived increase in topological polarization immediately after acoustic activity was switched off, before ordinary discharge.

The professional problem was not simply to propose an explanation. It was to determine what evidence would actually discriminate among plausible explanations without retrofitting a story to the observed result.

## 2. Research objective

The investigation retained three competing explanations:

- standard passive post-drive defect relaxation;
- an additional transient contribution from stored elastic/director relaxation;
- measurement or trajectory-accounting effects.

The first objective was deliberately narrower than mechanism discovery: reconstruct the polarization change from charge-resolved defect trajectories and determine which physical/accounting contribution actually carries the overshoot.

## 3. Work performed

I directed the research process from a published anomaly to a frozen, reproducible experimental test. The work included:

- prior-art review and claim narrowing;
- explicit hypothesis competition;
- preregistration of `CS05-EXP001`;
- implementation of the analysis before access to real external trajectories;
- SHA-256 freeze of the core analysis implementation;
- adversarial synthetic validation;
- external-data access assessment;
- formal stop when the evidence requirement could not be met.

The project intentionally did **not** weaken the endpoint, move the analysis window, invent missing data, or replace the missing experiment with a post-hoc simulation under the same experiment identity.

## 4. Technical asset

A Python accounting pipeline was implemented around the decomposition:

`ΔP = ΔP_motion + ΔP_boundary + ΔP_birth/death + ΔP_unresolved + ε_numeric`

with `+1/2` and `-1/2` topological-defect contributions reported separately.

The public validation suite tested three adversarial scenarios:

1. a genuine motion-carried overshoot;
2. a boundary-driven apparent overshoot;
3. an apparent overshoot caused by an unresolved new track.

The frozen software-validation assertions passed.

This validates the analysis logic only. It does not constitute physical evidence for any of the three mechanisms.

## 5. Outcome

The required charge-resolved external trajectories were not obtained at the evidentiary quality required by the preregistration.

The real-data experiment therefore was not executed and the mechanism remained unresolved.

**No physical-discovery claim and no novelty claim were made.**

## 6. Why this case matters professionally

The value of this case is not a forced discovery. It demonstrates the ability to:

- structure an ambiguous technical problem;
- reduce broad claims to a testable differential;
- distinguish competing explanations;
- design a reproducible data-analysis workflow;
- freeze criteria before seeing the desired data;
- validate software against adversarial cases;
- preserve negative and blocked results;
- stop when evidence is insufficient instead of manufacturing certainty.

These capabilities transfer directly to data analysis, decision intelligence, research analysis, technical due diligence, experimentation, model evaluation, and AI-assisted investigation.

## 7. Public evidence

- Repository: `https://github.com/RicardoVera-Lab/cs05-topological-overshoot-case-study`
- Public release: `v1.0.0`
- Technical report: available as PDF/DOCX in the GitHub release
- Reproducibility: preregistration, frozen code, synthetic tests, hashes, and claim ledger are public

## 8. Proprietary boundary

This case was conducted through the proprietary research architecture of **CIEC® LAB**.

The public case discloses evidence, methods, code, validation, limitations, and claim boundaries. Internal prompts, orchestration, role assignments, routing logic, decision gates, thresholds, handoff formats, and governance remain private.

## Skills demonstrated

**Data & technical:** Python, analytical decomposition, reproducibility, validation, structured data requirements, integrity hashing.

**Research:** prior-art review, hypothesis construction, falsification, preregistration, evidence auditing, technical writing.

**Decision quality:** uncertainty management, scope control, negative-result preservation, evidence-based stopping.

**AI-assisted work:** human-directed research orchestration without delegating claim authority to the AI systems involved.
