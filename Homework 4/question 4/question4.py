import sympy as sp

# Define constants in CGS units
G_cgs = 6.67430 * 10 ** (-8)  # Gravitational constant in cm^3/g/s^2
L_sol_cgs = 3.83 * 10**33  # Solar luminosity in erg/s
M_sol_cgs = 1.989 * 10**33  # Solar mass in g

# Define specific values for problem
m = 0.5 * M_sol_cgs  # Mass of the core in g
rho_0 = 10**6  # Initial density in g/cm^3
rho_f = 10**4  # Final density in g/cm^3
L_peak = 10**10 * L_sol_cgs  # Peak luminosity in erg/s

# Initial and final radii calculations in cm
R_0 = sp.N((3 / (4 * sp.pi) * m / rho_0) ** (1 / 3), 3)
R_f = sp.N((3 / (4 * sp.pi) * m / rho_f) ** (1 / 3), 3)

# Initial and final potential energy in erg
u = 3 / 5 * G_cgs * m**2
Del_U = u * (1 / R_0 - 1 / R_f)

# Time duration of the flash in seconds and days
t_seconds = Del_U / (0.2 * L_peak)
t_days = t_seconds / (24 * 3600)  # Convert seconds to days

# Display results in LaTeX format
print("Initial radius R_0 (cm):", sp.latex(R_0))
print("Final radius R_f (cm):", sp.latex(R_f))
print("Change in potential energy Del_U (erg):", sp.latex(Del_U))
print("Flash duration (seconds):", sp.latex(t_seconds))
print("Flash duration (days):", sp.latex(t_days))
