# Superseded pilot notebooks -- not part of the paper's reported results

This folder contains the project's early pilot notebooks, kept here for full transparency into
the project's history. **None of their numbers appear in the manuscript** -- the paper's reported
results begin at Phase 3b' ("harness fix"), in the parent `notebooks/` folder. Do not cite results
from this folder as evidence for any claim in the paper.

## Phase 0 (a-d) -- mechanism validation and correction

Before any task comparisons were run, these notebooks validated and corrected the core chaotic-map
construction:

- `Phase0_Premise_Test.ipynb` -- tested the originally specified sigmoid-bounded logistic map and
  proved it is analytically incapable of positive Lyapunov exponents at any parameter setting.
- `Phase0b_Map_Redesign.ipynb` -- introduced the gain-tunable triangle-fold map used throughout
  the rest of the project in its place.
- `Phase0c_Constraint_And_Sweep.ipynb` -- corrected the Lyapunov regularizer from a fixed-coefficient
  hinge on the map's own Jacobian to dual ascent on the full recurrence's Jacobian.
- `Phase0d_Tunable_Gain.ipynb` -- found and corrected a systematic bias in the single-step
  power-iteration Lyapunov estimator, replacing it with a windowed finite-time estimator.

## Phase 1 (+ 1b-1d) -- early synthetic-task comparison (superseded)

- `Phase1_Synthetic_Tasks.ipynb` -- the first four-task comparison (copying, selective copying,
  associative recall, long-range parity) against a linear-SSM baseline. Its training harness had a
  bug that inflated the apparent difficulty of the comparison; this is what Phase 3b' fixes.
- `Phase1b_Parity_Curriculum.ipynb`, `Phase1c_LR_Schedule.ipynb`,
  `Phase1d_Selective_Copy_Variance.ipynb` -- follow-up investigations within the same (later
  superseded) harness.

## Phase 2 (a-e) -- representational analysis and robustness characterization (superseded)

- `Phase2a_Recall_RSA.ipynb` -- representational similarity analysis confirming the recall
  mechanism.
- `Phase2b_Robustness.ipynb` -- characterized robustness costs on three axes.
- `Phase2c_Finetune_Scaling.ipynb` -- found the copying advantage collapsed at 4x scale.
- `Phase2d_Retuning_At_Scale.ipynb` -- traced the scale collapse to an untuned hyperparameter
  artifact.
- `Phase2e_Finetune_Retuned.ipynb` -- resolved it via retuning.

## Other early / abandoned notebooks

- `Phase3a_Selective_SSM_Baseline.ipynb`, `Phase3a_Corrected_Baseline.ipynb`,
  `Phase3a_ii_Mamba2_Diagnostic.ipynb` -- early attempts at a real Mamba-2-style selective-SSM
  baseline, from the same pre-harness-fix arc; superseded by the `mamba2` arm used in Phase 3b'
  onward.
- `Phase3b_Confirmatory_Battery.ipynb` -- an n=15 confirmatory battery, stopped before completion
  when the project's framing pivoted to the fork-in-the-road fair test (Phase 9); not run to
  completion and not part of the reported results.
