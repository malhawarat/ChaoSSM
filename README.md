# ChaoSSM

Code, notebooks, and results for **"Task-Matched Memory, Not Criticality, Decides Which Frozen
Reservoir Helps."**

Under review at *Entropy* (MDPI). This repository covers the code and experimental results,
including the seven experiments added during the first round of peer review; the manuscript itself
is not included while it is under journal consideration.

> **Note on an earlier version of this README.** An earlier revision of this file reported that
> the frozen edge-of-chaos reservoir's advantage was a benefit of criticality, "exactly as
> classical theory predicts," holding across "five of six chaotic systems." Controls run during
> peer review did not support that claim, and it has been withdrawn. What replaced it is described
> below. The superseded runs remain in this repository, labeled as such.

## Summary

The edge-of-chaos hypothesis says recurrent systems poised near criticality should have richer
memory and computational capacity than ordered (non-chaotic) ones. We test this directly with a
gain-tunable chaotic recurrent cell, instrumented with a validated Lyapunov estimator, and find
the hypothesis wrong on both of its terms.

- **Trained end-to-end**, a chaotic recurrence performs no better than a matched non-chaotic
  control or its own periodic-regime ablation. A validated Lyapunov analysis shows *why*: training
  drives the recurrence into a contracting regime, via a learned gate (and, independently, via
  input-driven synchronization when only the input projection is trained).
- **Frozen, under the canonical reservoir-computing protocol** (recurrence *and* input weights
  both fixed and random, only the readout trained), the nonlinear reservoir decisively beats a
  matched linear one — 0.462 vs. 0.251 on forecasting, winning on all 20 of 20 seeds. But a
  regime-pure control shows this is **not** a benefit of criticality: an *ordered* reservoir
  (λ ≈ −0.30) matches or exceeds the critical one, a seven-point Lyapunov sweep shows a flat
  accuracy plateau across the whole stable regime that collapses only past the chaos onset, and
  across six chaotic reservoir constructions the ordered arm leads on 21 of 30 paired seeds.
- **Criticality does pay on some tasks**, and that resolves the rest. Delay-resolved memory
  measurement explains both outcomes with one mechanism: the ordered reservoir retains more at
  lags 1–3, the critical one two to three times more at lags 4–12, and **across six targets the
  critical arm's margin tracks how far back the target reaches** (Pearson *r* = +0.97, *p* = 0.001),
  monotonically and changing sign.

This yields a **two-factor account**: bounded nonlinearity under contraction is the necessary
condition, and among reservoirs that have it, task-matched memory decides which regime wins.
Chaos proper never helps; criticality helps only when the task remembers further back than the
ordered regime holds.

We also report what fails. Scoring reservoirs by the overlap between what they retain and what the
target needs does **not** rank them (Spearman −0.20), because the linear reservoir maximizes memory
— more than twice that of any nonlinear arm — and still performs at chance.

### Added during peer review (Phases 18–24)

- **The deep-chaos training divergence is now diagnosed.** It is not a loss of boundedness in the
  state: the forward loss is finite at initialization on every seed. It is **exploding
  backpropagation-through-time gradients** through a genuinely expanding recurrence — the driven
  Jacobian's top singular value is 2.98 in the deep-chaos arm against 0.93 at the edge, and
  gradients reach 1.7 × 10¹⁹. Only truncated backpropagation removes it (0 of 8 seeds); smoothing
  the fold does not (0.62), which **excludes the fold kinks** as the cause.
- **The ordering survives architecture changes.** Across seven one-factor-at-a-time variants
  (width 32/64/128, normalization, readout, depth) edge beats linear in every one (+0.040 to
  +0.190) and beats deep chaos in every one (+0.078 to +0.403), with ordered at or above edge
  throughout.
- **The windowed Lyapunov proxy is provably biased upward.** Subadditivity makes the finite-window
  estimate an upper bound at *every* window length; measured bias falls from +0.271 (W=1) to
  +0.006 (W=64). A differentiable long-horizon QR estimator recovers the validated exponent to
  within 0.0022 with a finite gain gradient.
- **At longer dependency, chaos becomes actively harmful.** On a delay-recall task with controlled
  delay, every arm but the linear control is at ceiling through D = 24; at D = 48 the chaotic arm
  falls to 0.224 while its *identical* periodic twin reaches 0.844 (paired +0.620, 95% CI
  [+0.375, +0.864], 5 of 5 seeds).
- **Direct echo-state measurement.** An auxiliary-system (replica) test gives discrepancy exactly
  zero at every stable calibration and positive only past the chaos onset.

## Repository structure

```
ChaoSSM/
├── README.md
├── requirements.txt
├── data/                   # input series needed for reproduction
│   └── santafe_laser.csv   # Santa Fe laser (Weigend & Gershenfeld 1993), 10,093 points
├── notebooks/              # one Colab notebook per experimental phase
│   ├── ChaoSSM_Phase3b_Prime_Harness_Fix_GRU.ipynb        # harness-fix battery, copy task
│   ├── ChaoSSM_Phase4_HB_Gate_PeriodicR_Ablation.ipynb    # periodic-regime causal ablation
│   ├── ChaoSSM_Phase6_Dynamics_Validation.ipynb           # Lyapunov estimator validation
│   ├── ChaoSSM_Phase6b_Mechanism_Check.ipynb              # gate dose-response
│   ├── ChaoSSM_Phase9_Fork_FairTest.ipynb                 # fork-in-the-road fair test
│   ├── ChaoSSM_Phase10_RC_Control.ipynb                   # canonical RC control
│   ├── ChaoSSM_Phase11_Ungated_EndToEnd.ipynb             # ungated end-to-end control
│   ├── ChaoSSM_Phase12_Gamma_Projected_Training.ipynb     # proxy-free Lyapunov control
│   ├── ChaoSSM_Phase13d_Ordered_Control_Canonical.ipynb   # 6 reservoir constructions
│   ├── ChaoSSM_Phase14_Regime_Controls.ipynb              # regime-pure control, n=20
│   ├── ChaoSSM_Phase15_Lambda_Sweep.ipynb                 # seven-point Lyapunov sweep
│   ├── ChaoSSM_Phase16_MackeyGlass_Canonical.ipynb        # Mackey-Glass + non-chaotic control
│   ├── ChaoSSM_Phase17_Memory_Demand.ipynb                # delay-resolved memory + demand
│   ├── ChaoSSM_Phase18_RC_Benchmarks.ipynb                # NARMA10/30, Santa Fe, leaky ESN
│   ├── ChaoSSM_Phase19_Ridge_Readout.ipynb                # closed-form ridge vs GD readout
│   ├── ChaoSSM_Phase20_Synchronization.ipynb              # auxiliary-system echo-state test
│   ├── ChaoSSM_Phase21_Trained_LongDep.ipynb              # delay-recall, D = 4..48 (see note)
│   ├── ChaoSSM_Phase22_Divergence_Forensics.ipynb         # why deep-chaos training diverges
│   ├── ChaoSSM_Phase23_Robustness.ipynb                   # width/norm/readout/depth sweep
│   ├── ChaoSSM_Phase24_Proxy_Dissection.ipynb             # windowed-proxy bias + differentiable QR
│   └── superseded_pilots/  # earlier runs not used in the reported results -- see note below
├── results/                # per-run CSVs, also saved inline in each notebook's outputs
└── figures/                # the 17 figures in the manuscript, as rendered PNGs (see map below)
```

Most notebooks are provided **executed**, with real outputs, printed results tables, and inline
figures, so the paper's numbers can be inspected without rerunning anything. Five are currently
committed **without** outputs — `Phase13d_Ordered_Control_Canonical`, `Phase14_Regime_Controls`,
`Phase15_Lambda_Sweep`, `Phase16_MackeyGlass_Canonical` and `Phase17_Memory_Demand`. Their
per-run result files are complete and are in `results/`, so the numbers those phases contribute
to the manuscript remain fully inspectable; only the executed notebooks are pending. Each notebook is
self-contained; reproducing a run from scratch means clearing outputs and re-executing on Google
Colab (a T4 or L4 GPU is sufficient; several phases run faster on CPU, as noted in their config
cells). Phases 18–24 are resumable: they checkpoint to Google Drive and skip completed runs.

`data/santafe_laser.csv` is the Santa Fe Time Series Prediction Competition laser series
(Weigend & Gershenfeld, 1993), 10,093 native points, included so that Phase 18 reproduces without
relying on an external mirror. The file carries a provenance header.

File names in `figures/` are the LaTeX source names, which do **not** match the figure numbers in
the paper. The correspondence is:

| File | Figure | Shows |
|---|---|---|
| `fig1.png`  | Figure 1  | Chaotic cell and pre-norm residual block (architecture schematic) |
| `fig6.png`  | Figure 2  | Fair test, both input conditions |
| `fig10.png` | Figure 3  | Frozen reservoir along the Lyapunov axis (seven-point sweep) |
| `fig8.png`  | Figure 4  | Regime-pure reservoir control (ordered / edge / deep / linear) |
| `fig15.png` | Figure 5  | **Why the deep-chaos trained-input configuration diverges** |
| `fig7.png`  | Figure 6  | Regime-pure control across six chaotic reservoir constructions |
| `fig11.png` | Figure 7  | Frozen reservoirs on Mackey–Glass and the non-chaotic control |
| `fig12.png` | Figure 8  | Why the ordering depends on the target (memory by delay, demand, margin) |
| `fig13.png` | Figure 9  | **Critical margin tracks measured memory demand across six targets** |
| `fig14.png` | Figure 10 | **Auxiliary-system test of the echo state property** |
| `fig16.png` | Figure 11 | **Robustness to width, normalization, readout and depth** |
| `fig17.png` | Figure 12 | **Windowed Lyapunov proxy overestimates at every window length** |
| `fig3.png`  | Figure 13 | Held-out accuracy across arms on the fixed harness (copy task) |
| `fig4.png`  | Figure 14 | Periodic-regime ablation |
| `fig18.png` | Figure 15 | **Periodic-regime ablation at graded dependency length** |
| `fig2.png`  | Figure 16 | Windowed training proxy overestimates the conditional Lyapunov exponent |
| `fig5.png`  | Figure 17 | Gate dose-response (the central mechanism figure) |

Figures in **bold** were added during peer review.

### About `notebooks/superseded_pilots/`

This folder holds runs that are **not** part of the paper's reported evidence, kept for full
transparency into the project's history. **None of their numbers appear in the manuscript.** Do not
cite results from this folder as evidence for any claim in the paper. See
`notebooks/superseded_pilots/NOTE.md` for what each one covers.

It contains the early Phase 0–2 pilot work, early Phase 3a/3b attempts, and the three generality
runs that preceded the corrected one: `Phase13_Map_Generality_v2`, `Phase13b_Ordered_Control`, and
`Phase13c_Ordered_Control_n5`. Those three trained the input encoder alongside the readout, which
departs from the canonical reservoir-computing protocol and let the optimizer find degenerate input
embeddings; the cubic and sine "collapses" they reported were an artifact of that, and vanish
entirely when the encoder is frozen. `Phase13d_Ordered_Control_Canonical` is the corrected
replacement that the paper reports.

## Key results (summary)

| Experiment | Finding |
|---|---|
| Main battery (Phase 3b') | GRU reaches 0.995 accuracy on copy; chaotic/linear arms plateau at 0.10–0.16 |
| Periodic-regime ablation (Phase 4) | Confining the map to periodic dynamics matches or beats the chaotic variant — chaos is not the causal variable in the trained setting |
| Lyapunov estimator validation (Phase 6) | Recovers ln 2 on the logistic map at r=4 to an error of 2×10⁻⁴ |
| Gate dose-response (Phase 6b) | Forcing the trained gate open restores positive Lyapunov exponents (λ: −0.12 learned → +0.37 fully open) |
| Canonical reservoir control (Phase 10) | Frozen nonlinear reservoir 0.462 vs. linear 0.251 under random input, winning on all 20 of 20 seeds; reverses under trained input, revealing input-driven synchronization |
| Ungated end-to-end training (Phase 11) | Without a gate, chaos is not suppressed but training also fails (chance-floor accuracy, 20% divergence) |
| Gamma-projected training (Phase 12) | Chaos held genuinely positive by direct measurement still does not beat its matched periodic-regime twin |
| Generality, canonical protocol (Phase 13d) | Across six chaotic reservoir constructions the ordered arm is at or above the edge arm on every one; pooled edge − ordered = −0.024 (95% CI [−0.038, −0.012]) |
| Regime-pure control (Phase 14) | Ordered 0.476, edge 0.465, deep chaos 0.254, linear 0.251 (n=20). Criticality holds no privileged position; deep chaos is indistinguishable from linear |
| Lyapunov sweep (Phase 15) | Flat accuracy plateau from λ = −0.60 to ≈ 0 (0.481 → 0.462), collapsing to the linear level only past the onset |
| Mackey–Glass (Phase 16) | The ordering reverses: critical 0.392 vs. ordered 0.331, paired +0.061 (95% CI [+0.047, +0.075]) on 5 of 5 seeds |
| Memory demand (Phase 17) | Ordered retains more at lags 1–3 (−0.125), critical two to three times more at lags 4–12 (+0.317), both 5 of 5 seeds |
| **RC benchmarks (Phase 18)** | Santa Fe laser: edge 0.3588 vs. ordered 0.3306, paired +0.0282 (95% CI [+0.0176, +0.0389]), 5 of 5 seeds. Across six targets, margin vs. measured demand gives Pearson *r* = +0.97 (*p* = 0.001). Both NARMA margins are indistinguishable from zero — NARMA's i.i.d. input keeps input-lag MI low, so *measured* demand, not *designed* depth, is the operative variable |
| **Ridge readout (Phase 19)** | Closed-form ridge reproduces the gradient-descent ordering exactly across the three chaotic arms (Spearman +1.00; +0.90 across all five). Effective rank is *anti*-correlated with accuracy among the chaotic arms (Spearman −1.00): deep chaos has the richest representation (41.6 vs. 5.9) and the lowest accuracy |
| **Synchronization (Phase 20)** | Replica-test discrepancy is exactly 0.0000 at all five stable calibrations (λ = −0.58 to ≈ 0) and positive only past the onset (0.27 at λ = +0.15, 0.35 at λ = +0.29) |
| **Long dependency (Phase 21)** | Delay-recall: all arms but linear at ceiling through D = 24; at D = 48 chaotic 0.224 vs. its identical periodic twin 0.844 (paired +0.620, 5 of 5 seeds) and GRU 1.000. Conditional λ is exactly 0 at D ≤ 24 (gate fully closed) and +0.326 for the chaotic arm at D = 48 |
| **Divergence forensics (Phase 22)** | Deep-chaos trained input fails on 12 of 12 seeds at the *gradient* level, with the forward loss finite at initialization on every seed. Driven-Jacobian top singular value 2.98 (deep) vs. 0.93 (edge); gradients to 1.7 × 10¹⁹. Truncated BPTT fixes it (0.00); smoothed fold does not (0.62) |
| **Robustness (Phase 23)** | Edge > linear and edge > deep in all seven architecture variants; ordered ≥ edge in all seven. Separation *strengthens* with width (at N=128, +0.168 and +0.188); an MLP readout lifts linear to 0.516 but edge still leads by +0.190 |
| **Proxy dissection (Phase 24)** | Windowed proxy is an upper bound at every W (subadditivity); mean bias +0.271 (W=1) → +0.006 (W=64). Differentiable long-horizon QR estimator matches Benettin to 0.0022 with finite dλ/dγ |

## Citation

If you use this code, please cite:

```bibtex
@article{alhawarat2026chaossm,
  title   = {Task-Matched Memory, Not Criticality, Decides Which Frozen
             Reservoir Helps},
  author  = {Alhawarat, Mohammad and Elsimary, Hamed and Shalaldeh, Ahmad and
             Aburrub, Khalid Rafi and Alnsour, Ayman},
  journal = {Entropy},
  year    = {2026},
  note    = {Under review}
}
```

## License

MIT License, see `LICENSE`.

## Contact

Mohammad Alhawarat — m.hawarat@ammanu.edu.jo — Faculty of Information Technology,
Al-Ahliyya Amman University
