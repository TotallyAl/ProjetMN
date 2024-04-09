from SimReacteur import calculConcentrationsIVP
import numpy as np
from matplotlib import pyplot as plt


C_CH4_b = 1 / (4 * 22.4)
C_H2O_b = 3 * C_CH4_b
T = 973.15
C0 = np.array([C_CH4_b, C_H2O_b, 1e-4, 0, 0, 0, T, 3])


z, C = calculConcentrationsIVP([0, 0.29], C0, True)

fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(z, C[0], label="CH4", color="blue")
ax[0, 0].plot(z, C[1], label="H2O", color="purple")
ax[0, 0].plot(z, C[2], label="H2", color="orange")
ax[0, 0].plot(z, C[3], label="CO", color="green")
ax[0, 0].plot(z, C[4], label="CO2", color="red")
ax[0, 0].set_xlabel("Distance [m]")
ax[0, 0].set_ylabel("Concentrations [$kmol/m^3$]")
ax[0, 1].plot(z, C[5], label="X", color="green")
ax[0, 1].set_xlabel("Distance [m]")
ax[0, 1].set_ylabel("Conversion Fractionnaire")
ax[1, 0].plot(z, C[6], label="T", color="red")
ax[1, 0].set_xlabel("Distance [m]")
ax[1, 0].set_ylabel("Température [K]")
ax[1, 1].plot(z, C[7], label="P", color="blue")
ax[1, 1].set_xlabel("Distance [m]")
ax[1, 1].set_ylabel("Pression [bar]")
ax[0, 0].legend()
ax[0, 1].legend()
ax[1, 0].legend()
ax[1, 1].legend()
ax[0, 0].grid()
ax[0, 1].grid()
ax[1, 0].grid()
ax[1, 1].grid()
plt.show()
