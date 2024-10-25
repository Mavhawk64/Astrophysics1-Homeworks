# $$R_\text{max} = R_\odot \cdot 100 M/M_\odot$$
# $$R_\text{min} = 2 \cdot R_\text{MS}$$
# $$R_\text{MS} = R_\odot \cdot (M/M_\odot)^{0.7}$$
M_M_odot = [0.1, 0.3, 1, 3, 10, 30, 100]
R_MS_R_odot = [i ** 0.7 for i in M_M_odot]
R_min_R_odot = [2 * i for i in R_MS_R_odot]
R_max_R_odot = [100 * i for i in M_M_odot]

# output as LaTeX table
table = r"""
\begin{table}[H]
    \centering
    \begin{tabular}{|c|c|c|c|}
        \hline
        $M/M_\odot$ & $R_{MS}/R_\odot$ & $R_{min}/R_\odot$ & $R_{max}/R_\odot$ \\
        & (PMS END) & (PMS START AND HAYASHI END) & (HAYASHI START) \\
        \hline
"""
for i in range(len(M_M_odot)):
    table += f"{M_M_odot[i]} & {R_MS_R_odot[i]
        :.2f} & {R_min_R_odot[i]:.2f} & {R_max_R_odot[i]:.2f} \\\\\n"
table += r"""\hline
\end{tabular}
    \caption{Estimates for $R_{MS}$, $R_{min}$, and $R_{max}$ for stars of various masses}
    \label{tab:star_radii}
\end{table}
"""

print(table)
