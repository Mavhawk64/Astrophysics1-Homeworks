k_I = 0.4  # uniform sphere
t_J = 10  # Myr
m_sun_dot = 2*10**-8  # M_sun / Myr
m = 90  # M_sun

m_dot = m_sun_dot * 3500 * 1000 * 0.4 / 0.07 * m / 10  # M_sun / Myr

print(f"The mass loss rate of a 90 M_sun star is {m_dot:.2e} M_sun / Myr.")
