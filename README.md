# ChaoSSM

Code, notebooks, and results for **"Chaos helps until it is trained: an edge-of-chaos reservoir
succeeds where end-to-end training of the same dynamics fails."**

Submitted to *Chaos, Solitons & Fractals*. This repository covers the code and experimental
results; the manuscript itself is not included while it is under journal consideration.

## TL;DR

The edge-of-chaos hypothesis says recurrent systems poised near criticality should have richer
memory and computational capacity than ordered (non-chaotic) ones. We test this directly with a
gain-tunable chaotic recurrent cell, and find the answer is two-sided:

- **Trained end-to-end**, the hypothesis fails. A chaotic recurrence performs no better than a
  matched non-chaotic control, and a validated Lyapunov analysis shows *why*: training drives the
  recurrence into a contracting regime, via a learned gate (and, independently, via input-driven
  synchronization when only the input projection is trained).
- **Preserved untrained**, in the canonical reservoir-computing configuration (recurrence and
  input weights both fixed and random, only the readout trained), an edge-of-chaos reservoir
  substantially outperforms a linear one -- exactly as classical theory predicts. This benefit
  generalizes across six chaotic systems, including two continuous ODE flows (the Lorenz and
  Rossler attractors) that show the *largest* benefits of all.

So chaos itself is not the obstacle to its usefulness in these models -- training is.

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
│   ├── ChaoSSM_Phase13_Map_Generality_v2.ipynb            # generality across 6 chaotic systems (incl. Lorenz, Rossler)
│   └── superseded_pilots/  # early pilot notebooks (Phase 0-2, plus early Phase 3a/3b attempts), not used in the reported results -- see note below
├── results/                # CSVs and JSON verdicts, also saved inline in each notebook's outputs
└── figures/                # the 7 figures embedded in the manuscript, as rendered PNGs
    ├── fig1.png ... fig7.png    # fig1 = architecture schematic, fig7 = six-system generality chart;
                                  # figs 2-6 are also produced inline by their corresponding notebook
```

Notebooks are provided **executed**, with real outputs, printed results tables, and inline
figures, so the paper's numbers can be inspected without rerunning anything. Each notebook is
self-contained (no checkpoint files required); reproducing a run from scratch just means clearing
outputs and re-executing on Google Colab with a T4 GPU (or CPU at reduced scale, by setting
`SMOKE_TEST=True` in the config cell).

### About `notebooks/superseded_pilots/`

Before the results reported in the paper, we ran a longer arc of earlier pilot work: Phase 0
(a-d, chaotic-map and regularizer mechanism validation and correction), Phase 1 (+1b-1d, an early
synthetic-task comparison against a linear-SSM baseline), Phase 2 (a-e, representational
similarity analysis and robustness characterization), early Phase 3a attempts at a real Mamba-2
baseline, and an abandoned Phase 3b confirmatory battery. Phase 1's harness had a bug that
inflated the apparent difficulty of the comparison; this was found and fixed, and Phase 3b'
("harness fix"), in the main `notebooks/` folder, is the corrected replacement that the paper
actually reports. We include all of the original pilot notebooks here for transparency into the
project's full history -- see `notebooks/superseded_pilots/NOTE.md` for what each one covers --
but **none of their numbers appear in the manuscript**; only Phase 3b' onward is part of the
reported evidence.

## Key results (summary)

| Experiment | Finding |
|---|---|
| Main battery (Phase 3b') | GRU reaches 0.995 accuracy on copy; chaotic/linear arms plateau at 0.10-0.16 |
| Periodic-regime ablation (Phase 4) | Confining the map to periodic dynamics matches or beats the chaotic variant -- chaos is not the causal variable in the trained setting |
| Lyapunov estimator validation (Phase 6) | Recovers ln 2 on the logistic map at r=4 to an error of 2x10^-4 |
| Gate dose-response (Phase 6b) | Forcing the trained gate open restores positive Lyapunov exponents (lambda: -0.12 learned to +0.37 fully open) |
| Canonical reservoir control (Phase 10) | Edge-of-chaos reservoir: 0.462 vs. linear 0.251 under random input (5/5 seeds); reverses to a loss under trained input, revealing input-driven synchronization |
| Ungated end-to-end training (Phase 11) | Without a gate, chaos is not suppressed but training also fails to solve the task (chance-floor accuracy, 20% divergence) -- a second, complementary failure mode |
| Gamma-projected training (Phase 12) | Chaos held genuinely positive by direct measurement still does not beat its matched periodic-regime twin |
| Map-family generality (Phase 13) | The canonical-protocol benefit holds across six chaotic systems; the Lorenz and Rossler ODE flows show the largest benefits of all |

## Citation

If you use this code, please cite:

```bibtex
@article{alhawarat2026chaossm,
  title   = {Chaos helps until it is trained: an edge-of-chaos reservoir succeeds
             where end-to-end training of the same dynamics fails},
  author  = {Alhawarat, Mohammad and Elsimary, Hamed and Aburrub, Khalid Rafi},
  journal = {Chaos, Solitons \& Fractals},
  year    = {2026},
  note    = {Submitted}
}
```

## License

MIT License, see `LICENSE`.

## Contact

Mohammad Alhawarat -- m.hawarat@ammanu.edu.jo -- Faculty of Information Technology,
Al-Ahliyya Amman University
