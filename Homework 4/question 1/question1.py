import sympy as sp

# Define the constant(s)
n = 5

# M = - r^2 / (G * rho) * dP / dr
# P(rho) = K_n * rho^(1 + 1/n)
# theta = (rho / rho_c)^(1/n)
# xi = r / alpha_n
# alpha_n = ((n + 1) * K_n / (4 * pi * G * rho_c^(1-1/n)))^(1/2)

# Let's find an equation for M in terms of theta and xi
# First define the variables:
# Let's solve things in terms of theta and xi in the comments :)
# theta ^ n = rho / rho_c -> rho = rho_c * theta^n
# \theta = (1 + \xi^2/3)^{-1/2}
# xi = r / alpha_n -> r = xi * alpha_n

# Define the variables
theta, xi = sp.symbols("\\theta \\xi")
K_n = sp.symbols(f"K_{n}", real=True, positive=True)
G, rho_c = sp.symbols("G \\rho_c", real=True, positive=True)

alpha_n = sp.sqrt((n + 1) * K_n / (4 * sp.pi * G * rho_c ** (1 - 1 / n)))

theta = (1 + xi**2 / 3) ** (-1 / 2)

r = xi * alpha_n

rho = rho_c * theta**n

# Define the function P(rho)
P = K_n * rho ** (1 + 1 / n)

# Print out in cyan: P(rho)

print("\033[96mPressure\033[00m")

print("P(\\xi) =", sp.latex(P.simplify()))

# since xi = r / alpha_n and alpha_n is a constant, we can substitute r = xi * alpha_n -> dr = alpha_n dxi

M = -(r**2) / (G * rho) * sp.diff(P, xi) / alpha_n

# Print out in magenta: M

print("\033[95mMass\033[00m")

# Print the result in LaTeX
print("M(\\xi) =", sp.latex(M))

# Print out in yellow: limit xi -> \infty
print("\033[93mLimit xi -> oo\033[00m")

# Try limit xi -> infinity
print("\\lim_{\\xi\\to\\infty}M(\\xi) =", sp.latex(sp.limit(M, xi, sp.oo).simplify()))
