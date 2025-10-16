# Physics-Informed Neural Networks for Power Systems

This repository provides the TensorFlow implementation of the paper:

> **G. Misyris, A. Venzke, and S. Chatzivasileiadis,**  
> *"Physics-Informed Neural Networks for Power Systems,"*  
> 2019. [arXiv:1911.03737](https://arxiv.org/abs/1911.03737)

It introduces a **Physics-Informed Neural Network (PINN)** framework for power-system dynamics.  
By exploiting the underlying physical laws (swing equation) and embedding them directly into neural-network training, the PINN requires less data and achieves accurate learning of dynamic system states such as rotor angle and speed.

---

## 🧠 Background Summary (from Original Authors)

Physics-informed neural networks (PINNs) combine physical modeling and machine learning to estimate states such as rotor angles (δ) and frequencies (ω), as well as uncertain parameters like inertia and damping.

Compared to conventional methods, the PINN approach:
- Requires **fewer training data**
- Uses **simpler network architectures**
- Achieves **high accuracy and faster computation** (up to 87× speed-up)

### Original Folders from the Authors
- **`continuous_time_inference/`** — Reproduces results from Section III.B  
  Trains the network using swing-equation data (`swingEquation_inference.mat`)  
  and reports the prediction error `error_u`.

- **`continuous_time_identification/`** — Reproduces results from Section III.C  
  Estimates system **inertia** and **damping** from input data  
  (`swingEquation_identification.mat`), printing:
  - `error_lambda_1` → Inertia error  
  - `error_lambda_2` → Damping error  
  - `error_u` → L2 error between predicted and exact trajectories  

### Key Variables
| Variable | Description |
|-----------|-------------|
| `lb`, `ub` | Lower and upper bounds for (P, t) |
| `Nu` | Number of initial/boundary points |
| `Nf` | Number of collocation points |
| `usol` (δ) | Angle trajectories for different (P, t) |
| `x` (P₁) | Power levels in range [0.08, 0.18] |
| `t` | Time instants in range [0, 20] |

---

## ✳️ Extended Work by Albert Poulose

This repository has been **enhanced and extended** to improve reproducibility and visualization.  
Key additions include:
- Complete **Conda environment setup** (`environment.yml`)
- **Automatic result saving** (`swing_PINN_results.npz`)
- **Visualization scripts** for contour and time-series (2×2) figures
- **README documentation** for quick replication by other researchers

---

## ⚙️ Environment Setup

The project runs under a dedicated Conda environment named **`tf1-pinn`**.

### 1. Clone this repository
```bash
git clone <your_repo_url>
cd "Physics-Informed-Neural-Networks-for-Power-Systems"
```
### 2. Create the Conda environment (first time only)
```bash
conda env create -f environment.yml
```
### 3. Activate the environment
```bash
conda activate tf1-pinn
```
🧩 The `environment.yml` file pins all required versions:
Python 3.7, TensorFlow 1.15, SciPy 1.4.1, NumPy 1.18.5, pyDOE 0.3.8, etc.

### Running the PINN Inference
Navigate to the inference folder and run:
```bash
cd continuous_time_inference
python swingEquation_inference.py
```
During training, you’ll see outputs like:
```vbnet
Loss: 2.64e-06
Training time: 32.12 s
Error u: 2.73e-02
✅ Results saved to swing_PINN_results.npz
```
The trained model automatically saves the results for post-processing as: `swing_PINN_results.npz`
### Visualization and Figure Reproduction
1. Contour Visualization
Generates contour plots comparing exact and predicted swing trajectories:
```bash
python visualize_swing_results.py
```
2. 2×2 Time-Series Visualization
Reproduces the paper’s main figure showing δ(t) and ω(t) for P = 0.17 p.u. and P = 0.18 p.u.: 
```bash
python visualize_swing_2x2.py
```
### Project Structure
```text
Physics-Informed-Neural-Networks-for-Power-Systems/
│
├── environment.yml
├── README.md
│
├── Data/
│   └── swingEquation_inference.mat
│
├── continuous_time_inference/
│   ├── swingEquation_inference.py      # Main PINN training script
│   ├── visualize_swing_results.py      # Contour visualization
│   └── visualize_swing_2x2.py          
│
└── run_pinn_tf1.bat                    # Optional: one-click launcher
```

