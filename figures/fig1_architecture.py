import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"mathtext.fontset":"cm"})

fig = plt.figure(figsize=(14.5, 5.4), dpi=300)
axA = fig.add_axes([0.005, 0.09, 0.30, 0.82]); axA.axis("off")
axB = fig.add_axes([0.35, 0.09, 0.32, 0.82]); axB.axis("off")
axR = fig.add_axes([0.72, 0.09, 0.275, 0.82]); axR.axis("off")
for a in (axA,axB,axR): a.set_xlim(0,1); a.set_ylim(0,1)

C_map="#2E5395"; C_gate="#C55A11"; C_state="#548235"; C_block="#7030A0"
C_box="#F2F5FA"; C_edge="#33475B"; GREY="#5A6B7B"

def box(ax,cx,cy,w,h,fc,ec,txt,fs=11,tc="black",bold=False,lw=1.3):
    x=cx-w/2; y=cy-h/2
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.006,rounding_size=0.05",
                 fc=fc,ec=ec,lw=lw,mutation_aspect=1))
    ax.text(cx,cy,txt,ha="center",va="center",fontsize=fs,color=tc,
            fontweight="bold" if bold else "normal",zorder=6)
    return (cx,cy,w,h)

def arr(ax,p0,p1,color=C_edge,lw=1.7,rad=0.0,ls="-"):
    ax.add_patch(FancyArrowPatch(p0,p1,arrowstyle="-|>",mutation_scale=14,lw=lw,color=color,
                 connectionstyle=f"arc3,rad={rad}",ls=ls,zorder=3))

def title(ax,t): ax.text(0.5,1.0,t,ha="center",va="top",fontsize=13,fontweight="bold")

# =========================== PANEL A ===========================
title(axA,"(a) Gain-tunable chaotic map  $\\varphi_\\theta$")
h0 =box(axA,0.5,0.08,0.34,0.085,"#EAEFF6",C_edge,"state  $h_{t-1}$",10.5)
cpl=box(axA,0.28,0.30,0.50,0.10,C_box,C_map,"$W_{\\mathrm{mix}}h + r\\odot h(1{-}h)$",10)
rt =box(axA,0.80,0.30,0.34,0.10,C_box,C_map,"$r=r_{\\max}\\sigma(w_r)$",9,tc=GREY)
gn =box(axA,0.5,0.53,0.60,0.10,"#FDECE1",C_gate,"$\\gamma_\\theta=\\mathrm{softplus}(w_\\gamma)$",10.5,tc="#8A3D0B")
fd =box(axA,0.5,0.74,0.42,0.10,C_box,C_map,"triangle fold",11.5,bold=True,tc=C_map)
out=box(axA,0.5,0.92,0.34,0.075,"#EAEFF6",C_edge,"$\\varphi_\\theta(h)$",10.5)
arr(axA,(0.42,0.123),(0.30,0.25))
arr(axA,(0.6,0.123),(0.78,0.25),rad=-0.1)
arr(axA,(0.28,0.35),(0.42,0.48))
arr(axA,(0.80,0.35),(0.62,0.48),rad=0.08)
arr(axA,(0.5,0.58),(0.5,0.69))
arr(axA,(0.5,0.79),(0.5,0.882))
axA.text(0.5,0.645,"singular values scale $\\propto\\gamma_\\theta$",ha="center",va="center",
         fontsize=8.4,style="italic",color=GREY)

# =========================== PANEL B ===========================
title(axB,"(b) Input-gated recurrence")
# top inputs
xin=box(axB,0.22,0.90,0.30,0.08,"#EAEFF6",C_edge,"input  $x_t$",10)
hin=box(axB,0.78,0.90,0.30,0.08,"#EAEFF6",C_edge,"$h_{t-1}$",10)
# middle row: gate (left), phi (right)
gt =box(axB,0.22,0.66,0.34,0.10,"#FDECE1",C_gate,"gate  $g_t$",10.5,tc="#8A3D0B")
ph =box(axB,0.78,0.66,0.34,0.10,C_box,C_map,"$\\varphi_\\theta(Ah_{t-1})$",9.8)
# Bx below gate
bx =box(axB,0.115,0.50,0.20,0.075,C_box,GREY,"$Bx_t$",10,tc=GREY)
# combine node (centered, lower)
ncx,ncy=0.5,0.30
axB.add_patch(Circle((ncx,ncy),0.05,fc="white",ec=C_edge,lw=1.6,zorder=5))
axB.text(ncx,ncy,"$\\oplus$",ha="center",va="center",fontsize=14,zorder=6)
# fold + output
fld=box(axB,0.5,0.145,0.30,0.075,C_box,C_map,"fold",11,bold=True,tc=C_map)
ht =box(axB,0.5,0.055,0.26,0.062,"#EAEFF6",C_edge,"$h_t$",10.5)

# wiring — kept well separated
arr(axB,(0.26,0.86),(0.26,0.71))                       # x -> gate (right of the Bx feed)
arr(axB,(0.78,0.86),(0.78,0.71))                       # h -> phi
arr(axB,(0.13,0.86),(0.115,0.575),color=GREY,rad=0.0)   # x_t -> Bx (short, terminates AT box top)
arr(axB,(0.22,0.61),(0.44,0.335),color=C_gate,rad=-0.08)   # gate -> combine
arr(axB,(0.78,0.61),(0.56,0.335),color=C_map,rad=0.08)     # phi  -> combine
arr(axB,(0.215,0.50),(0.45,0.32),color=GREY,rad=-0.12)     # Bx -> combine (curved under)
# skip path: h_{t-1} -> combine, routed on the far right, clearly away from phi
arr(axB,(0.88,0.86),(0.56,0.315),color=C_state,rad=-0.38,ls=(0,(5,3)),lw=1.6)
axB.text(0.90,0.47,"$(1{-}g_t)h_{t-1}$",ha="center",va="center",fontsize=8.2,color=C_state,rotation=0)
arr(axB,(0.5,0.25),(0.5,0.185))                        # combine -> fold
arr(axB,(0.5,0.108),(0.5,0.088))                       # fold -> h_t
# combine formula BELOW the node, clear of arrows


# =========================== PANEL C ===========================
title(axR,"(c) Pre-norm residual block")
xw=0.60
inp=box(axR,0.5,0.05,0.42,0.07,"#EAEFF6",C_edge,"input  $x$",10)
ln1=box(axR,0.5,0.19,xw,0.075,"#EFEFEF",GREY,"LayerNorm",9.5,tc="#3A3A3A")
cel=box(axR,0.5,0.33,xw,0.085,C_box,C_block,"recurrent cell (a,b)",10,bold=True,tc=C_block)
axR.add_patch(Circle((0.5,0.44),0.032,fc="white",ec=C_edge,lw=1.5,zorder=5))
axR.text(0.5,0.44,"$+$",ha="center",va="center",fontsize=12,zorder=6)
ln2=box(axR,0.5,0.55,xw,0.075,"#EFEFEF",GREY,"LayerNorm",9.5,tc="#3A3A3A")
mlp=box(axR,0.5,0.68,xw,0.085,C_box,C_block,"feed-forward (MLP)",10,tc=C_block)
axR.add_patch(Circle((0.5,0.79),0.032,fc="white",ec=C_edge,lw=1.5,zorder=5))
axR.text(0.5,0.79,"$+$",ha="center",va="center",fontsize=12,zorder=6)
outp=box(axR,0.5,0.90,0.42,0.07,"#EAEFF6",C_edge,"output",10)
# main path
for p0,p1 in [(0.085,0.152),(0.2275,0.2875),(0.3725,0.408),(0.472,0.5125),(0.5875,0.6375),(0.7225,0.758),(0.822,0.865)]:
    arr(axR,(0.5,p0),(0.5,p1))
# residual skips on the LEFT, clearly outside the boxes
arr(axR,(0.20,0.05),(0.468,0.44),color=C_state,rad=-0.55,ls=(0,(5,3)),lw=1.5)
arr(axR,(0.20,0.44),(0.468,0.79),color=C_state,rad=-0.55,ls=(0,(5,3)),lw=1.5)
axR.text(0.005,0.62,"residual\nconnections",ha="left",va="center",fontsize=7.6,
         color=C_state,style="italic")

fig.text(0.5,0.015,
    "Only the recurrent cell (a,b) differs across arms; the host block (c) is identical for every model.",
    ha="center",va="bottom",fontsize=9.3,style="italic",color=GREY)

fig.savefig("/home/claude/paper/fig1_architecture.png",dpi=300,bbox_inches="tight",facecolor="white")
from PIL import Image
print("saved",Image.open("/home/claude/paper/fig1_architecture.png").size)
