# Superseded pilot notebooks -- not part of the paper's reported results

This folder contains **Phase 0**, **Phase 1**, and **Phase 2**, the earliest experimental
notebooks in the project, kept here for full transparency into the project's history.

- **Phase 0 (a-d)** validated and corrected the core chaotic-map mechanism: the originally
  specified sigmoid-bounded logistic map was proven analytically incapable of positive Lyapunov
  exponents at any parameter setting; a gain-tunable triangle-fold map was introduced in its
  place; the Lyapunov regularizer was corrected to dual ascent on the full recurrence's Jacobian;
  and the single-step Lyapunov estimator was found to carry a systematic bias and replaced with a
  windowed finite-time estimator.
- **Phase 1** ran a four-task synthetic comparison (copying, selective copying, associative
  recall, long-range parity) against a linear-SSM baseline. Its training harness had a bug that
  inflated the apparent difficulty of the comparison.
- **Phase 2 (a-e)** ran a representational similarity analysis confirming the recall mechanism,
  characterized robustness costs on three axes, found the copying advantage collapsed at 4x scale,
  traced this to an untuned hyperparameter artifact, and resolved it via retuning.

The Phase 1 harness bug was found and fixed; **Phase 3b' ("harness fix")**, in the parent
`notebooks/` folder, is the corrected replacement that the paper actually reports, and everything
from Phase 3b' onward supersedes this folder's results.

**None of the numbers from Phase 0, 1, or 2 appear in the manuscript.** These notebooks are
included only so the full experimental history is visible and nothing is hidden -- do not cite
results from this folder as evidence for any claim in the paper.
