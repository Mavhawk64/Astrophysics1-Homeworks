P_sun = 27  # days
R_sun = 696340  # km
R_ns = 10  # km

P_ns = P_sun * (R_ns / R_sun) ** 2
# days is too large a unit for the period of a neutron star, so we convert to milliseconds
P_ns *= 86400 * 1000

print(f"The rotation period of a neutron star is {P_ns:.2f} ms.")

P_bu = 2.78 * 60 * 60 * 1000 * (R_ns / R_sun) ** 1.5

# there is an extra space, so it formats nicely with the previous print statement
print(f"The  breakup period of a neutron star is {P_bu:.2f} ms.")

v_rot = R_ns * 2 * 3.1415926535897932384626 / P_ns
v_bu = R_ns * 2 * 3.1415926535897932384626 / P_bu

# these are in km / ms, so we convert to c
c = 299792.458  # km / s
v_rot = v_rot / c * 1000
v_bu = v_bu / c * 1000

print(f"The rotation velocity of a neutron star is {v_rot:.2f} c.")

print(f"The breakup velocity of a neutron star is {v_bu:.2f} c.")
