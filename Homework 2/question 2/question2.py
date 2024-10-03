import numpy as np

# Given data for the table
table = [
    {"mass": 50, "log_T_c": 7.6, "log_rho_c": 0.3},
    {"mass": 10, "log_T_c": 7.5, "log_rho_c": 0.8},
    {"mass": 1, "log_T_c": 7.2, "log_rho_c": 2.0},
    {"mass": 0.1, "log_T_c": 6.6, "log_rho_c": 2.8},
]


# Radiation Pressure (dyne/cm^2) = a / 3 * T^4
def P_rad(T, a=7.566e-15):
    return a / 3 * np.power(T, 4)


# Ideal Gas Pressure (dyne/cm^2) = k * rho * T / mu_bar
def P_ideal(rho, T, k=1.38e-16, m_AMU=1.66e-24, mu_bar=1):
    return k / m_AMU * rho * T / mu_bar


# Degenerate Non-relativistic Pressure (dyne/cm^2)
def P_deg_nr(rho, mu_e=2, m_H=1.67e-24, h=6.626e-27, m_e=9.11e-28):
    return (
        np.power(3 / np.pi, 2 / 3)
        * np.power(h, 2)
        / (20 * m_e)
        * np.power(rho / (mu_e * m_H), 5 / 3)
    )


# Degenerate Relativistic Pressure (dyne/cm^2)
def P_deg_r(rho, mu_e=2):
    return 1.243e15 * np.power(rho / mu_e, 4 / 3)


# Calculate the pressures for each mass
for row in table:
    row["T_c"] = np.power(10, row["log_T_c"])
    row["rho_c"] = np.power(10, row["log_rho_c"])
    row["P_rad"] = P_rad(row["T_c"])
    row["P_ideal"] = P_ideal(row["rho_c"], row["T_c"])
    row["P_deg_nr"] = P_deg_nr(row["rho_c"])
    row["P_deg_r"] = P_deg_r(row["rho_c"])


# Function to format numbers in scientific notation in LaTeX style
def latex_scientific_notation(num):
    # Split the scientific notation into mantissa and exponent
    mantissa, exp = "{:.2e}".format(num).split("e")
    mantissa = float(mantissa)
    exp = int(exp)
    return f"${mantissa:.2f}\\times10^{{{exp}}}$"


# Create LaTeX table format
latex_table = """
\\begin{table}[!ht]
    \\centering
    \\begin{tabular}{|c|c|c|c|c|c|c|}
    \\hline
    Mass & $T_c$ & $\\rho_c$ & $P_\\text{{rad}}$ & $P_\\text{{ideal}}$ & $P_\\text{{deg,nr}}$ & $P_\\text{{deg,r}}$ \\\\
    $[M_\\odot]$ & [K] & $[\\text{{g/cm}}^3]$ & [dyne/cm$^2$] & [dyne/cm$^2$] & [dyne/cm$^2$] & [dyne/cm$^2$] \\\\
    \\hline
"""

# Add rows to the table using LaTeX scientific notation
for row in table:
    latex_table += (
        f"{row['mass']} & "
        f"{latex_scientific_notation(row['T_c'])} & "
        f"{latex_scientific_notation(row['rho_c'])} & "
        f"{latex_scientific_notation(row['P_rad'])} & "
        f"{latex_scientific_notation(row['P_ideal'])} & "
        f"{latex_scientific_notation(row['P_deg_nr'])} & "
        f"{latex_scientific_notation(row['P_deg_r'])} \\\\ \n"
    )

# Closing LaTeX table
latex_table += """
    \\hline
    \\end{tabular}
    \\caption{Computed pressures for main sequence stars with different masses.}
    \\end{table}
"""

# Output LaTeX table
print(latex_table)
