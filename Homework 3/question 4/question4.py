import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


# Define the Lane-Emden equation as a system of first-order ODEs
def lane_emden(xi, y, n):
    theta, z = y  # theta = y[0], z = y[1] = dtheta/dxi
    dtheta_dx = z
    dz_dx = (
        -2 / xi * z - theta**n if xi != 0 else 0
    )  # Handling the singularity at xi = 0
    return [dtheta_dx, dz_dx]


# Initial conditions and solving setup
y0 = [1, 0]  # theta(0) = 1, dtheta/dxi(0) = 0

# Parameters
n_vals = [0.1, 1.5, 3, 5, 10]
xi_max = 10  # The maximum value of xi for the numerical solution
xi_vals = np.linspace(1e-4, xi_max, 1000)  # Avoid xi = 0 to prevent singularity

# Solve for different n values
solutions = []

# Increase the tolerance to make sure it covers the full range for each n
for n in n_vals:
    sol = solve_ivp(
        lane_emden,
        [1e-4, xi_max],
        y0,
        args=(n,),
        t_eval=xi_vals,
        method="RK45",  # Runge-Kutta 4th/5th order method
        rtol=1e-8,
        atol=1e-8,
    )
    solutions.append(
        np.interp(xi_vals, sol.t, sol.y[0])
    )  # Interpolate to match xi_vals

# Plotting only theta in [0, 1]
plt.figure(figsize=(10, 6))
for i, n in enumerate(n_vals):
    theta_vals = solutions[i]
    plt.plot(
        xi_vals[theta_vals >= 0], theta_vals[theta_vals >= 0], label=f"n={n}"
    )  # Plot only values where theta >= 0 and <= 1
    plt.xlim([0, xi_max])
    plt.ylim([0, 1])

plt.title(r"Lane-Emden Equation Solutions for Different $n$ ($\theta\in[0,1]$)")
plt.xlabel(r"$\xi$")
plt.ylabel(r"$\theta(\xi)$")
plt.legend()
plt.grid(True)

plt.savefig(f"{os.path.dirname(os.path.realpath(__file__))}/question4.png")

plt.show()
