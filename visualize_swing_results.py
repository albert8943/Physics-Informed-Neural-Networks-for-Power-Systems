"""
Visualization for swingEquation_inference.py results
Author: Albert Poulose (based on Misyris–Chatzivasileiadis PINN)
"""

import numpy as np
import matplotlib.pyplot as plt

# === Load saved results ===
# Make sure swingEquation_inference.py saved swing_PINN_results.npz in this same folder
results = np.load("swing_PINN_results.npz")

X = results["X"]
T = results["T"]
Exact = results["Exact"]
U_pred = results["U_pred"]
error_u = results["error_u"]

print(f"Loaded results successfully. Relative L2 error: {error_u:.4e}")

# === Plot exact solution ===
plt.figure(figsize=(6,5))
cs1 = plt.contourf(X, T, Exact, 50)
plt.title("Exact u(x,t)")
plt.xlabel("x")
plt.ylabel("t")
plt.colorbar(cs1)
plt.tight_layout()

# === Plot predicted solution ===
plt.figure(figsize=(6,5))
cs2 = plt.contourf(X, T, U_pred, 50)
plt.title("PINN Prediction u(x,t)")
plt.xlabel("x")
plt.ylabel("t")
plt.colorbar(cs2)
plt.tight_layout()

# === Plot absolute error ===
plt.figure(figsize=(6,5))
err = np.abs(U_pred - Exact)
cs3 = plt.contourf(X, T, err, 50)
plt.title("|Error|")
plt.xlabel("x")
plt.ylabel("t")
plt.colorbar(cs3)
plt.tight_layout()

plt.show()
