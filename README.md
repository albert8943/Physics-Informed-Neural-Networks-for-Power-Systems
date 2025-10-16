# Physics-Informed Neural Networks for Power Systems

We introduce  a  framework  for  physics-informed  neural  networks in power system applications. Exploiting the underlying physical laws  governing  power  systems,  and  inspired  by  recent  developments  in  the  field  of  machine  learning, we propose  a neural network training procedure that can make use of the wide range of mathematical models describing power system behavior, both  in  steady-state  and  in  dynamics.  Physics-informed  neural networks  require  substantially  less  training  data  and  result  in much  simpler  neural  network  structures,  while  achieving  high accuracy.  This  work  unlocks  a  range  of  opportunities  in  power systems,  being  able  to  determine  dynamic  states,  such  as  rotor angles and frequency, and uncertain parameters such as inertia and  damping  at  a  fraction  of  the  computational  time  required by conventional methods. We focus on introducing the framework  and  showcases  its  potential  using  a  single-machine infinite bus system as a guiding example. Physics-informed neural networks  are  shown  to  accurately  determine  rotor  angle  and frequency  up  to 87 times faster than  conventional  methods.


The folder `continuous_time_inference’ corresponds to the results presented in Section III.B. First, we load the input data file (swingEquation_inference.mat). Then, we randomly define the training set based on the number of Nu.  After the training process, the variables U_pred and Exact contain the predicted and actual values of the angle trajectories, respectively. The code also provides the L2 error between exact and predicted solutions for the angle (error_u).
The folder `continuous_time_identification’ corresponds to the results presented in Section III.C. By running the file swingEquation_identification.py we can predict system inertia and damping based on the input data (swingEquation_identification.mat). The exact values of the inertia and damping levels are 0.25 and 0.15. After the training process, the code prints the estimation error for the inertia (error_lambda_1) and damping (error_lambda_2), as well as the L2 error between exact and predicted solutions for the angle (error_u).

Code variables:
lb : defines the lower bound for the inputs (P,t)
ub: defines the upper bound for the inputs (P,t)
Nu : number of initial and boundary data
Nf : number of collocation points
usol (δ): is an array containing the angle trajectories for different pair of (P,t) (output to the NN)
x (P1): is an array containing different power levels in the range [0.08, 0.18] (input to the NN)
t : is an array containing time instants in the range [0, 20] (input to the NN)


When publishing results based on this data/code, please cite:
	G. Misyris, A. Venzke, S. Chatzivasileiadis, " Physics-Informed 
	Neural Networks for Power Systems", 2019. Available online: 
	https://arxiv.org/abs/1911.03737

@misc{misyris2019physicsinformed,
    title={Physics-Informed Neural Networks for Power Systems},
    author={George S. Misyris and Andreas Venzke and Spyros Chatzivasileiadis},
    year={2019},
    eprint={1911.03737},
    archivePrefix={arXiv},
    primaryClass={eess.SY}
}

---

# Contents from Albert

This repository reproduces and extends the classic work by  
**Misyris, Venzke, and Chatzivasileiadis (2019)** – *"Physics-Informed Neural Networks for Power Systems"*,  
implementing a PINN-based inference framework for the swing equation dynamics of a synchronous generator.

---

## 📘 Overview

This implementation demonstrates how a Physics-Informed Neural Network (PINN) learns the rotor angle and speed trajectories of a single-machine infinite-bus (SMIB) system governed by the swing equation.  
The framework combines the physical model residuals with data-driven learning to estimate system dynamics.

**Key features:**
- TensorFlow 1.15 implementation (compatible with TF 1.x syntax)
- L-BFGS-B optimization through `tf.contrib.opt.ScipyOptimizerInterface`
- Physics-informed residual enforcement using the swing equation
- Automatic saving of results (`.npz`) for reproducibility
- Visualization scripts to generate publication-quality figures

---

## ⚙️ Environment Setup

The project runs under a dedicated Conda environment named **`tf1-pinn`**.

Clone this repository and move into it:
    git clone <your_repo_url>
    cd "Physics-Informed-Neural-Networks-for-Power-Systems"


Create the Conda environment (first time only):
     conda env create -f environment.yml


Activate the environment:
    conda activate tf1-pinn


The environment.yml file pins all required versions (Python 3.7, TensorFlow 1.15, SciPy 1.4.1, NumPy 1.18.5, etc.) for long-term reproducibility.

Running the PINN Inference

Navigate to the continuous-time inference module and execute the training script:

cd "continuous_time_inference"
python swingEquation_inference.py

During training, you’ll see iterative loss updates such as:

Loss: 2.64e-06
Training time: 32.12 s
Error u: 2.73e-02
Results saved to swing_PINN_results.npz


The trained model automatically saves its results to:

swing_PINN_results.npz


📊 Visualization and Figure Reproduction
1. Contour Plots (Full Field Visualization)

To generate contour plots of the predicted vs. exact trajectories:

python visualize_swing_results.py


2. Publication-Style 2×2 Time-Series Figure

To reproduce the figure shown in the original paper (δ and ω vs time for P = 0.17 p.u. and 0.18 p.u.):

python visualize_swing_2x2.py


This script:

Extracts trajectories from the saved results


Produces a 2×2 plot:

A high-resolution image is saved automatically as:

swing_2x2_compare.png

🧠 Notes for Researchers

The environment targets TensorFlow 1.15 (with tf.Session, tf.placeholder, and tf.contrib), ensuring compatibility with legacy PINN codes.

All paths in Python use raw strings or forward slashes to avoid Windows escape-character issues.

GPU is not required. The message
Could not load dynamic library 'cudart64_100.dll'
is harmless on CPU systems.

Use pip freeze > requirements_tf1_pinn.txt to snapshot current versions for archival purposes.

## Project structure

```text
📂 Project Structure
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
│   └── visualize_swing_2x2.py          # 2×2 δ–ω publication figure
│
└── run_pinn_tf1.bat                    # Optional: one-click launcher
```




