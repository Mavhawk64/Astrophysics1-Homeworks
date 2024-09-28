import os

import matplotlib.pyplot as plt
import numpy as np

# Data from the user
mass = [50, 10, 1, 0.1]  # in solar masses
log_T_c = [7.6, 7.5, 7.2, 6.6]  # log temperature in K
log_rho_c = [0.3, 0.8, 2.0, 2.8]  # log density in g/cm^3

# Convert to linear scale for better plotting in log-log space
T_c = np.power(10, log_T_c)
rho_c = np.power(10, log_rho_c)

# Plotting the temperature vs density in a log-log plot
plt.figure(figsize=(8, 6))
plt.loglog(rho_c, T_c, marker="o", linestyle="-", color="b")
plt.xlabel("Central Density (g/cm³)")
plt.ylabel("Central Temperature (K)")
plt.title("Temperature vs Density at the Center of Stars")
plt.grid(True, which="both", ls="--")

# Save the plot before showing it
plt.savefig(f"{os.path.dirname(os.path.realpath(__file__))}/question1.png")

# Now show the plot
plt.show()
