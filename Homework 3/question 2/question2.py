from math import exp


def calculate_Y3(T_c, X_1):
    k_B = 8.6177e-8  # Boltzmann constant in keV/K
    return 5.6e-13 * exp(20.62 * (3 / 2 * k_B * T_c / 1.29) ** (-1 / 3)) * X_1


print(f"Y3 = {calculate_Y3(T_c=1.27e7, X_1=0.71):.2e}")
print(f"Y3 = {calculate_Y3(T_c=1.57e7, X_1=0.34):.2e}")
