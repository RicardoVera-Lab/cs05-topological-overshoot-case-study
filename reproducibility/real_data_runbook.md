# RUNBOOK — WHEN AUTHOR DATA ARRIVE

## Do not edit the frozen analysis first.

1. Preserve the incoming files byte-for-byte.
2. Compute SHA-256 for every received file.
3. Record email/date/source metadata.
4. Determine Tier A / B / C.
5. Create a **data adapter only** that maps author columns into the frozen schema.
6. The adapter may rename/reformat columns but may not:
   - smooth trajectories;
   - impute missing tracks;
   - relabel charge using outcome;
   - shift the overshoot window;
   - discard inconvenient realizations.

7. Validate the adapter on metadata/units.
8. Compute and record the adapter SHA-256.
9. Run the frozen pipeline once.
10. Archive stdout, JSON results and all hashes.
11. Apply the preregistered gate without tuning.

## Allowed pre-analysis clarification

If the authors' exact definition/normalization of P differs from the discrete accounting backbone, document the mapping before running the gate.

Do not choose among multiple definitions based on which gives the stronger effect.
