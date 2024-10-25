m_p = 1.0072766
m_1H = m_p
m_4He = 4.002603
m_12C = 12.0
m_16O = 15.994915
m_28Si = 27.976927
m_56Fe = 55.934937


def calculate_mass_defect_fraction(m_reactants, m_products):
    return calculate_mass_defect(m_reactants, m_products) / m_reactants


def calculate_mass_defect(m_reactants, m_products):
    return m_reactants - m_products


mass_defects = [  # Mass defect values for each reaction
    calculate_mass_defect(m_1H * 4, m_4He),
    calculate_mass_defect(m_4He * 3, m_12C),
    calculate_mass_defect(m_12C + m_4He, m_16O),
    calculate_mass_defect(m_16O * 2, m_28Si + m_4He),
    calculate_mass_defect(m_28Si * 2, m_56Fe),
]

mass_defect_fractions = [  # Mass defect fractions for each reaction
    calculate_mass_defect_fraction(m_1H * 4, m_4He),
    calculate_mass_defect_fraction(m_4He * 3, m_12C),
    calculate_mass_defect_fraction(m_12C + m_4He, m_16O),
    calculate_mass_defect_fraction(m_16O * 2, m_28Si + m_4He),
    calculate_mass_defect_fraction(m_28Si * 2, m_56Fe),
]

# Print the mass defect and mass defect fraction in the LaTeX table
table = r"""
\begin{table}[h!]
\centering
\begin{tabular}{|c|c|c|}
    \hline
    \textbf{Reaction} & \textbf{Mass Defect }$\Delta m$ (\textbf{amu}) & \textbf{Mass Defect Fraction} \\ \hline
    \ce{4^1H -> ^4He}              & %.6f & %.6f                       \\ \hline
    \ce{3^4He -> ^{12}C}           & %.6f & %.6f                       \\ \hline
    \ce{^{12}C + ^4He -> ^{16}O}   & %.6f & %.6f                       \\ \hline
    \ce{2^{16}O -> ^{28}Si + ^4He} & %.6f & %.6f                       \\ \hline
    \ce{2^{28}Si -> ^{56}Fe}       & %.6f & %.6f                       \\ \hline
\end{tabular}
\caption{Mass Defect and Mass Defect Fractions for Fusion Reactions}
\label{table:mass_defect_fractions}
\end{table}
""" % tuple(
    [value for sublist in zip(mass_defects, mass_defect_fractions) for value in sublist]
)

print(table)

import os

import matplotlib.pyplot as plt

# Enable LaTeX rendering
# plt.rc("text", usetex=True)


# Create x-axis labels for the reactions
reaction_labels = [
    r"$4^1H \rightarrow ^4He$",
    r"$3^4He \rightarrow ^{12}C$",
    r"$^{12}C + ^4He \rightarrow ^{16}O$",
    r"$2^{16}O \rightarrow ^{28}Si + ^4He$",
    r"$2^{28}Si \rightarrow ^{56}Fe$",
]


# Generate a plot of mass defect fractions (MDF) against the equation number (reaction number)
plt.figure(figsize=(8, 5))
plt.plot(range(1, 6), mass_defect_fractions, marker="o", linestyle="-", color="b")

# Add labels and title
plt.xticks(range(1, 6), reaction_labels, rotation=45, ha="right")
plt.xlabel("Fusion Reactions")
plt.ylabel("Mass Defect Fraction")
plt.title("Mass Defect Fractions for Fusion Reactions")

# Display the plot
plt.tight_layout()
plt.savefig(f"{os.path.dirname(os.path.realpath(__file__))}/question1.png")
plt.show()
