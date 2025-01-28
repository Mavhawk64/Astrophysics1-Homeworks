import os

import matplotlib.pyplot as plt
import mesa_reader as mr
import numpy as np

# Specify the directory path and history file path
dir_path = os.path.dirname(os.path.realpath(__file__))
history_path = os.path.join(dir_path, "0.3M-entropy/LOGS/history.data")

# Load the history data using mesa_reader
history = mr.MesaData(history_path)

# Extract central temperature (T_c) and entropy (s)
T_c = np.array(history.data("center_T"))
s = np.array(history.data("center_entropy"))

# Plot s vs T_c
plt.figure()
plt.plot(T_c, s, label="Entropy (s) vs Central Temperature (T_c)")
plt.xlabel("Central Temperature (T_c)")
plt.ylabel("Entropy (s)")
plt.title("Entropy vs Central Temperature")
plt.legend()
plt.grid(True)
# plt.show()

import numpy as np
from scipy.optimize import curve_fit


# Define the original function
def model(x, A, B):
    return A + B * np.log(x ** (3 / 2))


# Fit the data
params, covariance = curve_fit(model, T_c, s)

# Extract fitted parameters
A_fit, B_fit = params
print(f"Fitted A: {A_fit}, Fitted B: {B_fit}")

s_actual = A_fit + B_fit * np.log(T_c ** (3 / 2))

plt.figure()
plt.plot(T_c, s_actual, label="Actual Entropy (s) vs Central Temperature (T_c)")
plt.xlabel("Central Temperature (T_c)")
plt.ylabel("Actual Entropy (s)")
plt.title("Actual Entropy vs Central Temperature")
plt.legend()
plt.grid(True)

# The derivative of ln(x) is 1/x, so if we find c_* = T_c * (ds/dT_c), we should get B * 3/2,
# therefore print c_star = B * 3/2
c_star = B_fit * 3 / 2

print(f"c_*: {c_star}")
plt.show()
