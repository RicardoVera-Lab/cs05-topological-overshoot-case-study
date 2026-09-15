#!/usr/bin/env python3
"""
CS05-EXP001 — frozen charge-resolved polarization accounting pipeline.

Primary purpose:
  Decompose the post-switch-off change in a discrete polarization moment
  into motion, boundary, reaction, unresolved-event, and numerical residual
  terms, separately by topological charge.

This script must not be modified after real data inspection without creating
a new experiment ID.
"""

from __future__ import annotations
import argparse
import json
from pathlib import Path
import math
import pandas as pd
import numpy as np

REQ = [
    "realization_id","t","track_id","charge","x","y",
    "start_event","end_event"
]
ALLOWED_Q = {-0.5, 0.5}
START_EVENTS = {"", "none", "boundary_in", "birth", "unknown"}
END_EVENTS = {"", "none", "boundary_out", "death", "unknown"}

def _clean_event(x):
    if pd.isna(x):
        return "none"
    x = str(x).strip().lower()
    return "none" if x == "" else x

def validate(df: pd.DataFrame):
    missing = [c for c in REQ if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    if df[REQ].isnull().any().any():
        # event columns may be blank/NaN
        non_event = [c for c in REQ if c not in ("start_event","end_event")]
        if df[non_event].isnull().any().any():
            raise ValueError("Null values in required non-event columns")
    qs = set(float(x) for x in df["charge"].unique())
    if not qs.issubset(ALLOWED_Q):
        raise ValueError(f"Invalid charge values: {qs}")
    if (df.groupby(["realization_id","track_id"])["charge"].nunique() > 1).any():
        raise ValueError("A track_id changes charge within a realization")
    if df.duplicated(["realization_id","t","track_id"]).any():
        raise ValueError("Duplicate realization/time/track rows")
    for col, allowed in [("start_event", START_EVENTS), ("end_event", END_EVENTS)]:
        vals = {_clean_event(v) for v in df[col].tolist()}
        bad = vals - allowed
        if bad:
            raise ValueError(f"Invalid {col}: {bad}")

def p_discrete(frame: pd.DataFrame, Z: float) -> float:
    return float((frame["charge"] * frame["x"]).sum() / Z)

def analyze_step(a: pd.DataFrame, b: pd.DataFrame, Z: float):
    """Exact discrete identity from frame a to frame b."""
    A = a.set_index("track_id", drop=False)
    B = b.set_index("track_id", drop=False)
    ids_a, ids_b = set(A.index), set(B.index)
    cont = sorted(ids_a & ids_b)
    gone = sorted(ids_a - ids_b)
    new = sorted(ids_b - ids_a)

    out = {
        "motion_pos":0.0, "motion_neg":0.0,
        "boundary_pos":0.0, "boundary_neg":0.0,
        "reaction_pos":0.0, "reaction_neg":0.0,
        "unresolved_pos":0.0, "unresolved_neg":0.0,
    }

    for tid in cont:
        qa = float(A.at[tid,"charge"])
        qb = float(B.at[tid,"charge"])
        if qa != qb:
            raise ValueError(f"Charge changed for track {tid}")
        dx = float(B.at[tid,"x"] - A.at[tid,"x"])
        key = "motion_pos" if qa > 0 else "motion_neg"
        out[key] += qa * dx / Z

    for tid in new:
        row = B.loc[tid]
        q, x = float(row["charge"]), float(row["x"])
        ev = _clean_event(row["start_event"])
        suffix = "pos" if q > 0 else "neg"
        if ev == "boundary_in":
            key = f"boundary_{suffix}"
        elif ev == "birth":
            key = f"reaction_{suffix}"
        else:
            key = f"unresolved_{suffix}"
        out[key] += q*x/Z

    for tid in gone:
        row = A.loc[tid]
        q, x = float(row["charge"]), float(row["x"])
        ev = _clean_event(row["end_event"])
        suffix = "pos" if q > 0 else "neg"
        if ev == "boundary_out":
            key = f"boundary_{suffix}"
        elif ev == "death":
            key = f"reaction_{suffix}"
        else:
            key = f"unresolved_{suffix}"
        out[key] += -q*x/Z

    p0, p1 = p_discrete(a,Z), p_discrete(b,Z)
    observed = p1-p0
    accounted = sum(out.values())
    out["observed_delta"] = observed
    out["accounted_delta"] = accounted
    out["numeric_residual"] = observed-accounted
    return out

def nearest_time(times, target, tol):
    arr = np.asarray(sorted(times), dtype=float)
    i = int(np.argmin(np.abs(arr-target)))
    if abs(arr[i]-target) > tol:
        raise ValueError(f"No frame within {tol}s of reference {target}; nearest={arr[i]}")
    return float(arr[i])

def analyze_realization(df, rid, cfg):
    sub = df[df["realization_id"].astype(str)==str(rid)].copy()
    if sub.empty:
        raise ValueError(f"No rows for realization {rid}")
    Z = float(cfg["normalization_Z"])
    rcfg = cfg["realizations"][str(rid)]
    t_off = float(rcfg["t_off"])
    p_sigma = rcfg.get("p_sigma", None)
    t0w = t_off + float(cfg["overshoot_window_start_s_after_off"])
    t1w = t_off + float(cfg["overshoot_window_end_s_after_off"])
    tol = float(cfg["reference_time_tolerance_s"])

    times = sorted(sub["t"].astype(float).unique())
    tref = nearest_time(times, t_off, tol)
    frames = {float(t): sub[sub["t"].astype(float)==float(t)].copy() for t in times}
    P = {t:p_discrete(frames[t],Z) for t in times}
    p0 = P[tref]
    sign0 = 1.0 if p0 >= 0 else -1.0

    candidates = [t for t in times if t0w <= t <= t1w]
    if not candidates:
        raise ValueError("No frames in frozen overshoot window")
    O = {t: sign0*(P[t]-p0) for t in candidates}
    tpeak = max(candidates, key=lambda t: O[t])
    peak = float(O[tpeak])

    # Decompose from reference to peak over every consecutive step.
    use_times = [t for t in times if tref <= t <= tpeak]
    totals = {
        "motion_pos":0.0, "motion_neg":0.0,
        "boundary_pos":0.0, "boundary_neg":0.0,
        "reaction_pos":0.0, "reaction_neg":0.0,
        "unresolved_pos":0.0, "unresolved_neg":0.0,
        "observed_delta":0.0, "accounted_delta":0.0, "numeric_residual":0.0
    }
    steps=[]
    for ta,tb in zip(use_times[:-1], use_times[1:]):
        d=analyze_step(frames[ta],frames[tb],Z)
        steps.append({"t0":ta,"t1":tb,**d})
        for k in totals:
            totals[k]+=d[k]

    observed_signed = sign0 * totals["observed_delta"]
    unresolved_signed = sign0 * (totals["unresolved_pos"]+totals["unresolved_neg"])
    motion_pos_signed = sign0 * totals["motion_pos"]
    motion_neg_signed = sign0 * totals["motion_neg"]
    abs_peak = abs(totals["observed_delta"])
    unresolved_frac = abs(totals["unresolved_pos"]+totals["unresolved_neg"]) / max(abs_peak,1e-15)
    numeric_rel = abs(totals["numeric_residual"]) / max(abs_peak,1e-15)

    numeric_ok = (
        abs(totals["numeric_residual"]) <= float(cfg["numeric_abs_tolerance"])
        or numeric_rel <= float(cfg["numeric_rel_tolerance"])
    )
    unresolved_ok = unresolved_frac <= float(cfg["max_unresolved_fraction_of_peak"])

    if p_sigma is None:
        signal_status = "SIGNAL_PRESENT_UNCERTAINTY_MISSING" if peak > 0 else "NO_OVERSHOOT"
        signal_pass = False
    else:
        threshold = float(cfg["uncertainty_sigma_multiplier"]) * float(p_sigma)
        signal_pass = peak > threshold
        signal_status = "PASS" if signal_pass else "FAIL"

    frac_req = float(cfg["dominant_motion_fraction_of_peak"])
    pos_dom = motion_pos_signed > motion_neg_signed and motion_pos_signed >= frac_req*abs_peak
    neg_dom = motion_neg_signed > motion_pos_signed and motion_neg_signed >= frac_req*abs_peak
    dominant = "positive" if pos_dom else ("negative" if neg_dom else "none")

    return {
        "realization_id":str(rid),
        "t_off":t_off,
        "reference_time_used":tref,
        "p_reference":p0,
        "overshoot_window":[t0w,t1w],
        "t_peak":tpeak,
        "overshoot_projected_peak":peak,
        "p_sigma":p_sigma,
        "signal_status":signal_status,
        "signal_pass_robust":bool(signal_pass),
        "numeric_closure_pass":bool(numeric_ok),
        "unresolved_fraction_of_peak":unresolved_frac,
        "unresolved_pass":bool(unresolved_ok),
        "dominant_motion_carrier":dominant,
        "projected_motion_positive":motion_pos_signed,
        "projected_motion_negative":motion_neg_signed,
        "totals_raw":totals,
        "step_accounting":steps,
        "kinematic_gate_pass":bool(signal_pass and numeric_ok and unresolved_ok and dominant!="none")
    }

def summarize(results):
    kin = [r for r in results if r["kinematic_gate_pass"]]
    carriers = [r["dominant_motion_carrier"] for r in kin if r["dominant_motion_carrier"]!="none"]
    robust=False
    if len(results)>=2 and len(carriers)>=2:
        robust = len(set(carriers))==1
    if robust:
        status="ROBUST_KINEMATIC_PASS"
    elif len(kin)>=1:
        status="CASE_SPECIFIC_KINEMATIC_PASS"
    else:
        # distinguish uncertainty-only blockage
        if any(r["signal_status"]=="SIGNAL_PRESENT_UNCERTAINTY_MISSING" for r in results):
            status="INCONCLUSIVE_UNCERTAINTY_OR_GATE_BLOCK"
        else:
            status="NO_KINEMATIC_PASS"
    return {
        "overall_status":status,
        "n_realizations":len(results),
        "n_kinematic_pass":len(kin),
        "dominant_carriers_in_passes":carriers
    }

def run(tracks_path, config_path, out_path):
    df = pd.read_csv(tracks_path, keep_default_na=False)
    validate(df)
    cfg = json.loads(Path(config_path).read_text())
    # Ensure config has every realization in data
    rids = sorted(df["realization_id"].astype(str).unique())
    missing=[r for r in rids if r not in cfg["realizations"]]
    if missing:
        raise ValueError(f"Missing realization configs: {missing}")
    results=[analyze_realization(df,r,cfg) for r in rids]
    payload={"summary":summarize(results),"realizations":results}
    Path(out_path).write_text(json.dumps(payload,indent=2))
    return payload

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--tracks",required=True)
    ap.add_argument("--config",required=True)
    ap.add_argument("--out",required=True)
    args=ap.parse_args()
    payload=run(args.tracks,args.config,args.out)
    print(json.dumps(payload["summary"],indent=2))

if __name__=="__main__":
    main()
