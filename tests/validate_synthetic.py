#!/usr/bin/env python3
from pathlib import Path
import json
import sys
import tempfile

import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "src"))

from cs05_exp001_pipeline import run


def row(rid, t, tid, q, x, y=0.0, se="none", ee="none"):
    return dict(
        realization_id=rid,
        t=float(t),
        track_id=tid,
        charge=float(q),
        x=float(x),
        y=float(y),
        start_event=se,
        end_event=ee,
    )


def scenario_motion_only():
    rows = []
    for t, xn1, xn2 in [(68, 2.0, 3.0), (70, 2.2, 3.2), (72, 2.8, 3.8), (75, 3.4, 4.4), (80, 3.0, 4.0)]:
        rows += [
            row("motion", t, "n1", -0.5, xn1),
            row("motion", t, "n2", -0.5, xn2),
            row("motion", t, "p1", +0.5, 1.0),
        ]
    return rows


def scenario_boundary():
    rows = []
    for t in [68, 70]:
        rows += [row("boundary", t, "n1", -0.5, 2.0), row("boundary", t, "p1", 0.5, 1.0)]
    rows += [
        row("boundary", 72, "n1", -0.5, 2.0),
        row("boundary", 72, "n2", -0.5, 4.0, se="boundary_in"),
        row("boundary", 72, "p1", 0.5, 1.0),
    ]
    for t in [75, 80]:
        rows += [
            row("boundary", t, "n1", -0.5, 2.0),
            row("boundary", t, "n2", -0.5, 4.0),
            row("boundary", t, "p1", 0.5, 1.0),
        ]
    return rows


def scenario_unknown():
    rows = []
    for t in [68, 70]:
        rows += [row("unknown", t, "n1", -0.5, 2.0), row("unknown", t, "p1", 0.5, 1.0)]
    rows += [
        row("unknown", 72, "n1", -0.5, 2.0),
        row("unknown", 72, "n2", -0.5, 4.0, se="unknown"),
        row("unknown", 72, "p1", 0.5, 1.0),
    ]
    for t in [75, 80]:
        rows += [
            row("unknown", t, "n1", -0.5, 2.0),
            row("unknown", t, "n2", -0.5, 4.0),
            row("unknown", t, "p1", 0.5, 1.0),
        ]
    return rows


def main():
    rows = scenario_motion_only() + scenario_boundary() + scenario_unknown()
    df = pd.DataFrame(rows)

    cfg = {
        "normalization_Z": 1.0,
        "overshoot_window_start_s_after_off": 2.0,
        "overshoot_window_end_s_after_off": 12.0,
        "reference_time_tolerance_s": 0.25,
        "numeric_abs_tolerance": 1e-8,
        "numeric_rel_tolerance": 1e-6,
        "max_unresolved_fraction_of_peak": 0.05,
        "dominant_motion_fraction_of_peak": 0.50,
        "uncertainty_sigma_multiplier": 2.0,
        "realizations": {
            "motion": {"t_off": 68.0, "p_sigma": 0.01},
            "boundary": {"t_off": 68.0, "p_sigma": 0.01},
            "unknown": {"t_off": 68.0, "p_sigma": 0.01},
        },
    }

    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        tracks = td / "synthetic_tracks.csv"
        config = td / "synthetic_config.json"
        out = td / "synthetic_results.json"
        df.to_csv(tracks, index=False)
        config.write_text(json.dumps(cfg, indent=2), encoding="utf-8")
        payload = run(tracks, config, out)

    R = {r["realization_id"]: r for r in payload["realizations"]}

    assert R["motion"]["numeric_closure_pass"]
    assert R["motion"]["unresolved_pass"]
    assert R["motion"]["dominant_motion_carrier"] == "negative"
    assert R["motion"]["kinematic_gate_pass"]

    assert R["boundary"]["numeric_closure_pass"]
    assert R["boundary"]["unresolved_pass"]
    assert R["boundary"]["dominant_motion_carrier"] == "none"
    assert not R["boundary"]["kinematic_gate_pass"]
    assert abs(R["boundary"]["totals_raw"]["boundary_neg"]) > 0

    assert R["unknown"]["numeric_closure_pass"]
    assert not R["unknown"]["unresolved_pass"]
    assert not R["unknown"]["kinematic_gate_pass"]
    assert abs(R["unknown"]["totals_raw"]["unresolved_neg"]) > 0

    print("ALL_SYNTHETIC_TESTS_PASS")
    print(json.dumps(payload["summary"], indent=2))


if __name__ == "__main__":
    main()
