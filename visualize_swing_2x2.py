import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ---- config: which P values to plot ----
P_targets = [0.17, 0.18]   # p.u.

# ---- load results saved by swingEquation_inference.py ----
results_path = Path(__file__).resolve().parent / "swing_PINN_results.npz"
data = np.load(results_path)

X      = data["X"]          # shape: (Nt, Nx)
T      = data["T"]          # shape: (Nt, Nx)
Exact  = data["Exact"]      # shape: (Nt, Nx)  (delta exact)
U_pred = data["U_pred"]     # shape: (Nt, Nx)  (delta predicted)
error_u = float(data["error_u"])

# time (Nt,) and parameter (Nx,)
t = T[:, 0]
P = X[0, :]

# time step for gradient
dt = float(np.mean(np.diff(t)))

def nearest_idx(arr, target):
    return int(np.argmin(np.abs(arr - target)))

# compute omega = d(delta)/dt along time axis
def time_derivative(mat, dt):
    # central difference via numpy.gradient (handles edges)
    return np.gradient(mat, dt, axis=0)

omega_exact  = time_derivative(Exact,  dt)
omega_pred   = time_derivative(U_pred, dt)

# ----- plotting -----
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 6), sharex="col")
# Styling: exact (solid black), predicted (red dashed)
kw_exact = dict(color="k", linewidth=1.8)
kw_pred  = dict(color="r", linestyle="--", linewidth=1.8)

for col, P_tar in enumerate(P_targets):
    j = nearest_idx(P, P_tar)
    P_used = P[j]  # nearest available

    # top row: delta
    ax = axes[0, col]
    ax.plot(t, Exact[:, j], label="Exact", **kw_exact)
    ax.plot(t, U_pred[:, j], label="Predicted", **kw_pred)
    ax.set_title(f"P = {P_used:.2f} [p.u.]", fontsize=11)
    ax.set_ylabel(r"$\delta$ [rad]")
    ax.grid(True, alpha=0.4)

    # bottom row: omega
    ax = axes[1, col]
    ax.plot(t, omega_exact[:, j], **kw_exact)
    ax.plot(t, omega_pred[:, j],  **kw_pred)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel(r"$\omega$ [rad/s]")
    ax.grid(True, alpha=0.4)

# one shared legend centered at top
fig.legend(["Exact", "Predicted"], ncol=2, loc="upper center", bbox_to_anchor=(0.5, 1.03), frameon=True)

plt.tight_layout(rect=[0, 0, 1, 0.96])  # leave space for legend
out_png = Path(__file__).resolve().parent / "swing_2x2_compare.png"
plt.savefig(out_png, dpi=300)
print(f"Saved figure to: {out_png}")
plt.show()
