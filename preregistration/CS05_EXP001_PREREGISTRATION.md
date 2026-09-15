# CS05-EXP001 — FROZEN PREREGISTRATION SUMMARY

## Experiment
POST-SWITCH-OFF DEFECT-CURRENT ACCOUNTING

## Objective
Determine whether the published polarization overshoot can be reconstructed kinematically from charge-resolved defect trajectories plus explicit boundary and reaction terms.

## Discrete accounting backbone
`P_d(t) = (1/Z) * sum_i q_i x_i(t)` with `q_i` in `{-1/2,+1/2}`.

## Frozen example timing
Switch-off: `t_off = 68 s`.

Primary overshoot interval: `[t_off + 2, t_off + 12]`.

The window may not be moved post hoc to maximize effect size.

## Accounting identity
`ΔP = ΔP_motion + ΔP_boundary + ΔP_birth/death + ΔP_unresolved + ε_numeric`.

Positive and negative defect contributions are reported independently.

## Gates
- G0 — data adequacy.
- G1 — direct unsmoothed reconstruction.
- G2 — accounting closure.
- G3 — carrier identification.
- G4 — robustness across switch-offs when available.

## Possible outputs
- ARTIFACT / ACCOUNTING KILL
- DATA-SURFACE INSUFFICIENT
- CASE-SPECIFIC KINEMATIC PASS
- ROBUST KINEMATIC PASS
- INCONCLUSIVE

## Promotion constraint
EXP001 alone cannot establish H0 or H1.

Only a kinematic PASS would authorize `CS05-EXP002 — PASSIVE-NULL REPLAY`.

EXP002 was never authorized because EXP001 was not executed on real data.
