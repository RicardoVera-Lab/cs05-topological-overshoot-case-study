# PORTFOLIO CASE STUDY — CS05

## Investigating a Post-Drive Topological Polarization Overshoot

### Subtitle
An AI-assisted scientific research case in prior-art attack, hypothesis competition, preregistration, reproducible analytics and evidence-gated stopping.

## Challenge
A published active-liquid-crystal experiment reported a short-lived increase in topological polarization immediately after activity was switched off, before ordinary discharge.

The source work described the phenomenon but did not fully resolve its underlying mechanism.

## Objective
Discriminate among:

1. ordinary passive defect relaxation;
2. a transient contribution from stored elastic/director relaxation;
3. measurement/accounting artifacts.

## Role
Directed an AI-assisted research workflow that discovered and narrowed the frontier question, attacked prior art, separated broad absorbed claims from the remaining differential, formalized competing hypotheses, preregistered a discriminating experiment, implemented the analysis before real-data access, froze the software and gates, validated the pipeline with adversarial synthetic cases, and stopped the investigation when the required external evidence could not be obtained.

## Technical work
Implemented a Python accounting pipeline for:

`ΔP = motion + boundary + reaction + unresolved`.

The pipeline separately accounts for +1/2 and -1/2 defects.

Synthetic tests verified that it accepts a genuine motion-carried overshoot, identifies boundary-driven apparent overshoot and blocks unexplained-track artifacts.

## Outcome
**Unresolved due to unavailable external raw data. No mechanism claim made.**

## Why the case matters
The project demonstrates a research process that does not force a discovery. It reached the evidentiary boundary, preserved the preregistration and software freeze, and stopped rather than replacing missing evidence with post-hoc explanation.

## Skills demonstrated
- scientific research;
- prior-art intelligence;
- data-analysis design;
- Python;
- falsifiable hypothesis construction;
- preregistration;
- reproducibility;
- software validation;
- AI-assisted research direction;
- uncertainty management;
- negative-result preservation;
- evidence-based stopping.
