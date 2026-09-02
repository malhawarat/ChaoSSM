import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11})

systems = ["Cubic\n(map)","Tent\n(map)","Sine\n(map)","Logistic\n(map)","R\u00f6ssler\n(ODE flow)","Lorenz\n(ODE flow)"]
chaos_vals = [None, 0.40, 0.62, 0.65, 0.68, 0.70]  # cubic inconclusive
linear = 0.32
chance = 0.10

fig, ax = plt.subplots(figsize=(8.5, 4.8), dpi=300)
x = np.arange(len(systems))
colors = ["#B0B0B0" if v is None else ("#2E7D32" if "flow" in systems[i] else "#4C8BF5") for i,v in enumerate(chaos_vals)]
heights = [0.0 if v is None else v for v in chaos_vals]

bars = ax.bar(x, heights, color=colors, width=0.6, zorder=3, edgecolor="white", linewidth=0.5)
for i,v in enumerate(chaos_vals):
    if v is None:
        ax.text(x[i], 0.02, "inconclusive", ha="center", va="bottom", fontsize=8.5, rotation=90, color="#555555")
    else:
        ax.text(x[i], v+0.015, f"{v:.2f}", ha="center", va="bottom", fontsize=9.5, fontweight="bold")

ax.axhline(linear, color="#C0392B", ls="--", lw=1.6, zorder=2, label=f"linear reservoir ({linear:.2f})")
ax.axhline(chance, color="gray", ls=":", lw=1.2, zorder=1, label=f"chance ({chance:.2f})")

ax.set_xticks(x); ax.set_xticklabels(systems, fontsize=9.5)
ax.set_ylabel("forecasting accuracy\n(frozen edge-of-chaos reservoir, canonical protocol)", fontsize=10)
ax.set_ylim(0, 0.82)
ax.set_title("Generality of the reservoir benefit across six chaotic systems", fontsize=12, fontweight="bold")
ax.legend(loc="upper left", fontsize=9, frameon=True)
ax.grid(axis="y", alpha=0.25, zorder=0)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)

fig.text(0.5, -0.02,
    "Green bars: continuous ODE flows (mathematically unrelated to the logistic family), shown to have the largest benefits of all.",
    ha="center", fontsize=8.5, style="italic", color="#444444")

fig.tight_layout()
fig.savefig("/home/claude/paper/fig7_generality.png", dpi=300, bbox_inches="tight", facecolor="white")
print("saved fig7_generality.png")
from PIL import Image
print(Image.open("/home/claude/paper/fig7_generality.png").size)
