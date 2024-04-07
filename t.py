from SimReacteur import calculConcentrationsEuler
import numpy as np
from matplotlib import pyplot as plt


C_CH4_b = 1 / (4 * 22.4)
C_H2O_b = 3 * C_CH4_b
T = 973.15
C0 = np.array([C_CH4_b, C_H2O_b, 1e-4, 0, 0, 0, T, 3])


z, C = calculConcentrationsEuler([0, 0.29], C0, True)

plt.plot(z, C[0], label="CH4")
plt.plot(z, C[1], label="H2O")
plt.plot(z, C[2], label="H2")
plt.plot(z, C[3], label="CO")
plt.plot(z, C[4], label="CO2")
plt.legend()
plt.grid()
plt.show()
