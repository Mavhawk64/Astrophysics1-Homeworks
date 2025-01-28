import sympy as sp

# Given:
# epsilon \propto rho^2 T^nu
# P \propto rho T
# L_rad \propto R T^4 rho^-1
# L_thm \propto R epsilon
# R_c \propto M_c^{a(nu)}

M, R, nu = sp.symbols("M R \\nu", positive=True, real=True)


T = M / R
rho = M / R**3
epsilon = rho**2 * T**nu

print("\\epsilon \\propto", sp.latex(epsilon.simplify()))

L_rad = R * T**4 * rho**-1

print("L_\\text{rad} \\propto", sp.latex(L_rad.simplify()))

L_thm = R * epsilon

print("L_\\text{thm} \\propto", sp.latex(L_thm.simplify()))

# Equate L_rad and L_thm to find R_c in terms of M_c
eq = sp.Eq(L_rad, L_thm)

R_c = sp.solve(eq, R)[0]

print("R_c \\propto", sp.latex(R_c.simplify()))

# Try nu = 40
R_c = R_c.subs(nu, 40)

print("R_c \\propto", sp.latex(R_c.simplify()))
