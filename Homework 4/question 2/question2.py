import sympy as sp

# Redefining constants and symbols based on provided notation
mu_bar = 4 / (8 - 5 * 0.25)  # Calculating mu_bar
R_star, M_star, K = sp.symbols("R_* M_* K", positive=True, real=True)
nu = 3.8  # Given exponent value

# Define the first relation and solve for R_star
r_m_rel = (
    sp.log(R_star, 10)
    - K
    - ((nu - 4) / (nu - 3)) * sp.log(mu_bar, 10)
    - ((nu - 1) / (nu + 3)) * sp.log(M_star, 10)
)
R_star_solution = sp.simplify(sp.solve(r_m_rel, R_star)[0]).evalf(3)

# Define Mass-Luminosity relation
L = sp.simplify(mu_bar ** (-4) * M_star**3 * R_star_solution).evalf(3)

# Define Mass-Central Temperature relation
C, T_c = sp.symbols("C T_c")
T_c_M = sp.simplify(C * mu_bar * M_star / M_star**3.5).evalf(3)

# Solving for constant 'c' given T_c(1, C) = 1.5 * 10^7
c_value = sp.solve(T_c_M.subs(M_star, 1) - 1.5 * 10**7, C)[0]

# Solve for M_star when T_c(M_star, c) = 10^8
M_star_at_10e8 = sp.simplify(
    sp.solve(T_c_M.subs(C, c_value) - 10**8, M_star)[0]
).evalf(3)

# Generate LaTeX output
R_star_latex = "R_* \\propto " + sp.latex(R_star_solution)
L_latex = "L_* \\propto " + sp.latex(L)
T_c_M_latex = "T_c \\propto " + sp.latex(T_c_M)
c_latex = "c = " + sp.latex(c_value)
M_star_latex = "M_* = " + sp.latex(M_star_at_10e8)

print(R_star_latex)
print(L_latex)
print(T_c_M_latex)
print(c_latex)
print(M_star_latex)
