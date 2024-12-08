import os

import matplotlib.pyplot as plt
import mesa_reader as mr


def plot(x, y, xlabel, ylabel, title, invert_x=False, invert_y=False):
    plt.figure()
    plt.plot(x, y, label=f"{ylabel} vs {xlabel}")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if invert_x:
        plt.gca().invert_xaxis()
    if invert_y:
        plt.gca().invert_yaxis()
    plt.legend()
    plt.grid(True)


# Get the paths to the data files
## Get the current file
dir_path = os.path.dirname(os.path.realpath(__file__))
history_data = "LOGS/history.data"
## Join the paths
z0001 = os.path.join(dir_path, "0_0001Z", history_data)
z001 = os.path.join(dir_path, "0_001Z", history_data)
z01 = os.path.join(dir_path, "0_01Z", history_data)
z02 = os.path.join(dir_path, "0_02Z", history_data)

# Load the data
history_0001 = mr.MesaData(z0001)
history_001 = mr.MesaData(z001)
history_01 = mr.MesaData(z01)
history_02 = mr.MesaData(z02)

col_names = history_0001.bulk_names  # they should all have the same column names:
# ('model_number', 'num_zones', 'star_age', 'log_dt', 'star_mass', 'log_xmstar', 'log_abs_mdot', 'mass_conv_core', 'conv_mx1_top', 'conv_mx1_bot', 'conv_mx2_top', 'conv_mx2_bot', 'mx1_top', 'mx1_bot', 'mx2_top', 'mx2_bot', 'log_LH', 'log_LHe', 'log_LZ', 'log_Lnuc', 'pp', 'cno', 'tri_alfa', 'epsnuc_M_1', 'epsnuc_M_2', 'epsnuc_M_3', 'epsnuc_M_4', 'epsnuc_M_5', 'epsnuc_M_6', 'epsnuc_M_7', 'epsnuc_M_8', 'he_core_mass', 'c_core_mass', 'o_core_mass', 'si_core_mass', 'fe_core_mass', 'neutron_rich_core_mass', 'log_Teff', 'log_L', 'log_R', 'log_g', 'v_div_csound_surf', 'log_cntr_P', 'log_cntr_Rho', 'log_cntr_T', 'center_mu', 'center_ye', 'center_abar', 'center_h1', 'center_he4', 'center_c12', 'center_o16', 'surface_c12', 'surface_o16', 'total_mass_h1', 'total_mass_he4', 'num_retries', 'num_iters', 'log_star_age', 'log_center_T', 'log_center_Rho', 'log_center_P', 'Pc_scaled')


# SAMPLE - HR DIAGRAM
xname = "log_Teff"
yname = "log_L"

plot(
    history_0001.data(xname),
    history_0001.data(yname),
    xname,
    yname,
    "HR Diagram (0.0001 Z)",
    invert_x=True,
)

plot(
    history_001.data(xname),
    history_001.data(yname),
    xname,
    yname,
    "HR Diagram (0.001 Z)",
    invert_x=True,
)

plot(
    history_01.data(xname),
    history_01.data(yname),
    xname,
    yname,
    "HR Diagram (0.01 Z)",
    invert_x=True,
)

plot(
    history_02.data(xname),
    history_02.data(yname),
    xname,
    yname,
    "HR Diagram (0.02 Z)",
    invert_x=True,
)


# Make this the last line of the file:
plt.show()
