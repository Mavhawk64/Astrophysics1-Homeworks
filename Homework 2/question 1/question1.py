import os

import matplotlib.pyplot as plt
import numpy as np

mass = [50, 10, 1, 0.1]  # in solar masses
log_T_c = [7.6, 7.5, 7.2, 6.6]  # log temperature in K
log_rho_c = [0.3, 0.8, 2.0, 2.8]  # log density in g/cm^3

# Convert to linear scale for better plotting in log-log space
T_c = np.power(10, log_T_c)
rho_c = np.power(10, log_rho_c)

# Degenerate line: rho = 10^6 (for all temperatures)
rho_deg = 1e6
T_vals_extended = np.logspace(4, 8.48, 100)  # Extended range of temperatures to plot

# Constant temperature line: T = 10^8.48 for all densities
T_constant = 10**8.48
rho_vals = np.logspace(-10, 10, 100)  # Range of densities to plot

# Adding the trial and error curve: y = 10^7.5 * rho^0.33
T_trial_error = 10**7.5 * np.power(rho_vals, 0.33)

# Adding the new curve: T = 10^4.7 * rho^0.65
T_new_curve = 10**4.7 * np.power(rho_vals, 0.65)

# Plotting the figure
plt.figure(figsize=(8, 6))

# Plot the user's points
plt.loglog(rho_c, T_c, marker="o", linestyle="-", color="b", label="Mass points")

# Degenerate line: rho = 10^6 extended
plt.loglog(
    [rho_deg] * len(T_vals_extended),
    T_vals_extended,
    linestyle="--",
    color="r",
    label=r"$\rho = 10^6$ g/cm³",
)

# Trial and error line: T = 10^7.5 * rho^0.33
plt.loglog(
    rho_vals,
    T_trial_error,
    linestyle="-.",
    color="m",
    label=r"$T = 10^{7.5} \cdot \rho^{0.33}$",
)

# New curve: T = 10^4.7 * rho^0.65
plt.loglog(
    rho_vals,
    T_new_curve,
    linestyle=":",
    color="c",
    label=r"$T = 10^{4.7} \cdot \rho^{0.65}$",
)

# Setting the axis limits
plt.xlim(1e-10, 1e8)
plt.ylim(1e4, 10**8.48)

# Adding the region labels
plt.text(1e-7, 1.1e7, "Radiation", fontsize=12, color="black")
plt.text(1e-4, 1.1e5, "Ideal Gas", fontsize=12, color="black")
plt.text(1e2, 1.1e5, "Degeneracy", fontsize=12, color="black")
plt.text(
    1e7,
    1e6,
    "Relativistic Degeneracy",
    fontsize=12,
    color="black",
    rotation=90,
    verticalalignment="center",
)

# Labels, title, and legend
plt.xlabel("Central Density (g/cm³)")
plt.ylabel("Central Temperature (K)")
plt.title("Temperature vs Density at the Center of Stars")
plt.grid(True, which="both", ls="--")
# plt.legend()

# Save the plot before showing it
plt.savefig(f"{os.path.dirname(os.path.realpath(__file__))}/question1.png")

# Now show the plot
plt.show()
