# ChaoSSM

Code, notebooks, and results for **"Neither chaos nor criticality: training suppresses chaos,
and task-matched memory decides which frozen reservoir helps."**

Under review at *Chaos, Solitons & Fractals* (CHAOS-D-26-09018, revised submission). This
repository covers the code and experimental results; the manuscript itself is not included while
it is under journal consideration.

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
- **Criticality does pay on one task**, and that resolves the rest. On Mackey–Glass (τ = 17) the
  critical reservoir leads the ordered one by +0.061 (95% CI [+0.047, +0.075], 5 of 5 seeds).
  Delay-resolved memory measurement explains both outcomes with one mechanism: the ordered
  reservoir retains more at lags 1–3, the critical one two to three times more at lags 4–12, and
  across three targets the critical arm's margin tracks how far back the target reaches —
  monotonically, with disjoint intervals, changing sign.

This yields a **two-factor account**: bounded nonlinearity under contraction is the necessary
condition, and among reservoirs that have it, task-matched memory decides which regime wins.
Chaos proper never helps; criticality helps only when the task remembers further back than the
ordered regime holds. We state this as a falsifiable mechanism resting on three targets, not as
an established law.

We also report what fails. Scoring reservoirs by the overlap between what they retain and what the
target needs does **not** rank them (Spearman −0.20), because the linear reservoir maximizes memory
— more than twice that of any nonlinear arm — and still performs at chance.

## Repository structure

```
ChaoSSM/
├── README.md
├── requirements.txt
├── notebooks/              # one executed Colab notebook per experimental phase (with outputs)
│   ├── ChaoSSM_Phase3b_Prime_Harness_Fix_GRU.ipynb        # harness-fix battery: GRU/linear/mamba2/chaotic, copy task
│   ├── ChaoSSM_Phase4_HB_Gate_PeriodicR_Ablation.ipynb    # periodic-regime causal ablation
│   ├── ChaoSSM_Phase6_Dynamics_Validation.ipynb           # Lyapunov estimator validation + conditional-vs-autonomous split
│   ├── ChaoSSM_Phase6b_Mechanism_Check.ipynb              # gate dose-response mechanism experiment
│   ├── ChaoSSM_Phase9_Fork_FairTest.ipynb                 # fork-in-the-road fair test (frozen reservoir, first version)
│   ├── ChaoSSM_Phase10_RC_Control.ipynb                   # canonical reservoir-computing control (random vs. trained input)
│   ├── ChaoSSM_Phase11_Ungated_EndToEnd.ipynb             # ungated end-to-end training control
│   ├── ChaoSSM_Phase12_Gamma_Projected_Training.ipynb     # gamma-projected training (proxy-free Lyapunov control)
│   ├── ChaoSSM_Phase13d_Ordered_Control_Canonical.ipynb   # generality across 6 reservoir constructions, canonical protocol
│   ├── ChaoSSM_Phase14_Regime_Controls.ipynb              # regime-pure control: ordered / edge / deep / linear, n=20
│   ├── ChaoSSM_Phase15_Lambda_Sweep.ipynb                 # seven-point Lyapunov sweep, lambda = -0.60 to +0.30
│   ├── ChaoSSM_Phase16_MackeyGlass_Canonical.ipynb        # Mackey-Glass and non-chaotic control, canonical protocol
│   ├── ChaoSSM_Phase17_Memory_Demand.ipynb                # delay-resolved memory capacity + per-target memory demand
│   └── superseded_pilots/  # earlier runs not used in the reported results -- see note below
├── results/                # per-run CSVs, also saved inline in each notebook's outputs
└── figures/                # the 11 figures in the manuscript, as rendered PNGs (see map below)
```

File names in `figures/` are the LaTeX source names, which do **not** match the figure numbers in
the paper. The correspondence is:

| File | Figure | Shows |
|---|---|---|
| `fig1.png`  | Figure 1  | Chaotic cell and pre-norm residual block (architecture schematic) |
| `fig6.png`  | Figure 2  | Fair test, both input conditions |
| `fig10.png` | Figure 3  | Frozen reservoir along the Lyapunov axis (seven-point sweep) |
| `fig8.png`  | Figure 4  | Regime-pure reservoir control (ordered / edge / deep / linear) |
| `fig11.png` | Figure 5  | Frozen reservoirs on Mackey–Glass and the non-chaotic control |
| `fig12.png` | Figure 6  | Why the ordering depends on the target (memory by delay, demand, margin) |
| `fig3.png`  | Figure 7  | Held-out accuracy across arms on the fixed harness (copy task) |
| `fig4.png`  | Figure 8  | Periodic-regime ablation |
| `fig2.png`  | Figure 9  | Windowed training proxy overestimates the conditional Lyapunov exponent |
| `fig5.png`  | Figure 10 | Gate dose-response (the central mechanism figure) |
| `fig7.png`  | Figure 11 | Regime-pure control across six chaotic reservoir constructions |

Notebooks are provided **executed**, with real outputs, printed results tables, and inline
figures, so the paper's numbers can be inspected without rerunning anything. Each notebook is
self-contained (no checkpoint files required); reproducing a run from scratch just means clearing
outputs and re-executing on Google Colab (a T4 or L4 GPU is sufficient; several phases run faster
on CPU, as noted in their config cells).

### About `notebooks/superseded_pilots/`

This folder holds runs that are **not** part of the paper's reported evidence, kept for full
transparency into the project's history. **None of their numbers appear in the manuscript.** Do not
cite results from this folder as evidence for any claim in the paper. See
`notebooks/superseded_pilots/NOTE.md` for what each one covers.

It contains the early Phase 0–2 pilot work, early Phase 3a/3b attempts, and — added in this
revision — the three generality runs that preceded the corrected one: `Phase13_Map_Generality_v2`,
`Phase13b_Ordered_Control`, and `Phase13c_Ordered_Control_n5`. Those three trained the input
encoder alongside the readout, which departs from the canonical reservoir-computing protocol and
let the optimizer find degenerate input embeddings; the cubic and sine "collapses" they reported
were an artifact of that, and vanish entirely when the encoder is frozen.
`Phase13d_Ordered_Control_Canonical` is the corrected replacement that the paper reports.

## Key results (summary)

| Experiment | Finding |
|---|---|
| Main battery (Phase 3b') | GRU reaches 0.995 accuracy on copy; chaotic/linear arms plateau at 0.10–0.16 |
| Periodic-regime ablation (Phase 4) | Confining the map to periodic dynamics matches or beats the chaotic variant — chaos is not the causal variable in the trained setting |
| Lyapunov estimator validation (Phase 6) | Recovers ln 2 on the logistic map at r=4 to an error of 2×10⁻⁴ |
| Gate dose-response (Phase 6b) | Forcing the trained gate open restores positive Lyapunov exponents (λ: −0.12 learned → +0.37 fully open) |
| Canonical reservoir control (Phase 10) | Frozen nonlinear reservoir 0.462 vs. linear 0.251 under random input, winning on all 20 of 20 seeds; reverses under trained input, revealing input-driven synchronization |
| Ungated end-to-end training (Phase 11) | Without a gate, chaos is not suppressed but training also fails (chance-floor accuracy, 20% divergence) — a second, complementary failure mode |
| Gamma-projected training (Phase 12) | Chaos held genuinely positive by direct measurement still does not beat its matched periodic-regime twin |
| Generality, canonical protocol (Phase 13d) | Across six chaotic reservoir constructions the ordered arm is at or above the edge arm on every one; pooled edge − ordered = −0.024 (95% CI [−0.038, −0.012]), ordered better on 21 of 30 seeds; no run falls below its linear control |
| Regime-pure control (Phase 14) | Ordered 0.476, edge 0.465, deep chaos 0.254, linear 0.251 (n=20). Criticality holds no privileged position; deep chaos is indistinguishable from linear. Neither memory capacity nor separation tracks accuracy |
| Lyapunov sweep (Phase 15) | Flat accuracy plateau from λ = −0.60 to ≈ 0 (0.481 → 0.462), collapsing to the linear level only past the onset; the collapse coincides with a discontinuous loss of the echo state property, not with criticality |
| Mackey–Glass (Phase 16) | The ordering reverses: critical 0.392 vs. ordered 0.331, paired +0.061 (95% CI [+0.047, +0.075]) on 5 of 5 seeds. On a non-chaotic control all arms compress toward linear |
| Memory demand (Phase 17) | Ordered retains more at lags 1–3 (−0.125), critical two to three times more at lags 4–12 (+0.317), both 5 of 5 seeds. Mackey–Glass shows a second mutual-information peak of 1.15 nats at lag ≈ 22 (its τ = 17 signature) where the logistic target has collapsed to 0.09 nats |

## Citation

If you use this code, please cite:

```bibtex
@article{alhawarat2026chaossm,
  title   = {Neither chaos nor criticality: training suppresses chaos, and
             task-matched memory decides which frozen reservoir helps},
  author  = {Alhawarat, Mohammad and Elsimary, Hamed and Aburrub, Khalid Rafi},
  journal = {Chaos, Solitons \& Fractals},
  year    = {2026},
  note    = {Under review}
}
```

## License

MIT License, see `LICENSE`.

## Contact

Mohammad Alhawarat — m.hawarat@ammanu.edu.jo — Faculty of Information Technology,
Al-Ahliyya Amman University
