r = 1495979000  # m
G_SC = 1361  # W/m^2
L_wd = G_SC * 4 * 3.1415926535897932384626 * r ** 2  # W

print(f"The luminosity of a white dwarf is {L_wd:.2e} W.")

R_wd = 10515000  # m
sigma = 5.67 * 10 ** -8  # W/m^2/K^4
T_wd = (L_wd / (4 * 3.1415926535897932384626 * R_wd ** 2 * sigma)) ** 0.25  # K

print(f"The temperature of a white dwarf is {T_wd:.2f} K.")

L_sun = 3.828 * 10 ** 26  # W

t_wd = 110 * (L_wd / (0.01 * L_sun)) ** -(5/7)  # Myr

print(f"The lifetime of a white dwarf is {t_wd:.2f} Myr.")
