import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from Derivee import odefunction
from Config import Constantes

C_CH4_b = 1 / 22.4 / 4
C_H2O_b = 3 * C_CH4_b
T = 973.15
C0 = np.array([C_CH4_b, C_H2O_b, 1e-3, 0, 0, 0, T, 3])

iterations = 100000


def calculConcentrationsIVP(interval: list, C0: list) -> list:
    return solve_ivp(
        odefunction,
        interval,
        t_eval=np.linspace(interval[0], interval[1], iterations),
        method="RK45",
        y0=C0,
    )


# Euler Explicite
def calculConcentrationsEuler(interval: list, C0: list) -> list:
    n = iterations
    z = np.linspace(interval[0], interval[1], n)
    """Cette liste contient les valeurs de z qui seront utilisés pour calculer les concentrations."""
    C = np.zeros((8, n))
    C[:, 0] = C0
    h: float = z[1] - z[0]
    for i in range(n - 1):
        C[:, i + 1] = C[:, i] + h * (odefunction(z[i], C[:, i]))

    return [z, C]


# print("Euler: ", calculConcentrationsEuler([0, 0.29], C0))


solution = calculConcentrationsIVP([0, 0.29], C0)
# print("IVP: ", solution)
# print("IVP z: ", solution.t)
# print("IVP T: ", solution.y[6])

# Graphe
"""Graphe pour IVP"""
# fig, plot = plt.subplots(2, 2)
# plot[0, 0].plot(solution.t, solution.y[0, :], label="CH4")
# plot[0, 0].plot(solution.t, solution.y[1, :], label="H2O")
# plot[0, 0].plot(solution.t, solution.y[2, :], label="H2")
# plot[0, 0].plot(solution.t, solution.y[3, :], label="CO")
# plot[0, 0].plot(solution.t, solution.y[4, :], label="CO2")
# plot[0, 1].plot(solution.t, solution.y[5, :], label="X")
# plot[1, 0].plot(solution.t, solution.y[6, :], label="T")
# plot[1, 1].plot(solution.t, solution.y[7, :], label="P")
# plt.xlabel("Longueur du réacteur (m)")
# plt.ylabel("Concentration (kmol/m3)")
# plot[0, 0].legend()
# plot[0, 1].legend()
# plot[1, 0].legend()
# plot[1, 1].legend()

# plt.grid(True)
# plot[0, 0].grid(True)
# plot[0, 1].grid(True)
# plot[1, 0].grid(True)
# plot[1, 1].grid(True)
# plt.show()

"""Graphe pour Euler"""
z, concentrations = calculConcentrationsEuler([0, 0.29], C0)
# print(f"{concentrations[0,:]=}")
# print(f"{solution.y[0,:]=}")
fig, plot = plt.subplots(2, 2)
plot[0, 0].plot(z, concentrations[0, :], label="CH4")
plot[0, 0].plot(z, concentrations[1, :], label="H2O")
plot[0, 0].plot(z, concentrations[2, :], label="H2")
plot[0, 0].plot(z, concentrations[3, :], label="CO")
plot[0, 0].plot(z, concentrations[4, :], label="CO2")
plot[0, 1].plot(z, concentrations[5, :], label="X")
plot[1, 0].plot(z, concentrations[6, :], label="T")
plot[1, 1].plot(z, concentrations[7, :], label="P")
plt.xlabel("Longueur du réacteur en (m)")
plt.ylabel("Concentration des composés en (kmol/m^3)")
plt.title("Concentrations des composés en fonction de la longueur du réacteur")
plt.grid(True)
plt.show()

# print(odefunction(0, C0))
