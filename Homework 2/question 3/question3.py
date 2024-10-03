T_surface = 5778  # Surface temperature of the Sun in K
mu = 0.62  # Mean molecular weight of the Sun
m_H = 1.67e-24  # Mass of hydrogen atom in g
G = 6.674e-8  # Gravitational constant in cm^3/g/s^2
M_odot = 1.989e33  # Solar mass in g
R_odot = 6.96e10  # Solar radius in cm
k_B = 1.38e-16  # Boltzmann constant in erg/K


def T(r):
    return T_surface + 2 / 5 * G * M_odot * mu * m_H / k_B * (1 / r - 1 / R_odot)


print(T(0.71 * R_odot))
