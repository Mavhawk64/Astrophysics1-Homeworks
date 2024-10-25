m = [0.1, 0.3, 1, 3, 10, 30, 100]

t_Hayashi = [1/i for i in m]
t_MS = [60*i ** -2.5 for i in m]

table = r"""
\begin{table}[H]
    \centering
    \begin{tabular}{|c|c|c|}
        \hline
        $M/M_\odot$ & $\tau_\text{Hayashi}$ (Myr) & $\tau_\text{MS}$ (Myr) \\
        \hline
"""
for i in range(len(m)):
    table += f"{m[i]} & {t_Hayashi[i]:.3f} & {t_MS[i]:.3f} \\\\\n"
table += r"""\hline
\end{tabular}
    \caption{Estimates for $\tau_\text{Hayashi}$ and $\tau_\text{MS}$ for stars of various masses}
    \label{tab:star_lifetimes}
\end{table}
"""

print(table)
