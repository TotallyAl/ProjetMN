import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from Derivee import odefunction
from Config import Constantes

C_CH4_b = 1 / 22.4 / 4
C_H2O_b = 3 * C_CH4_b
T = 973.15
C0 = np.array([C_CH4_b, C_H2O_b, 1e-3, 0, 0, 0, T, 3])


def calculConcentrationsIVP(interval: list, C0: list) -> list:
    return solve_ivp(
        odefunction,
        interval,
        t_eval=np.linspace(interval[0], interval[1], 100),
        method="RK45",
        y0=C0,
    )


# Euler Explicite
def calculConcentrationsEuler(interval: list, C0: list) -> list:
    n = 100
    z = np.linspace(interval[0], interval[1], n)
    """Cette liste contient les valeurs de z qui seront utilisés pour calculer les concentrations."""
    C = np.zeros((8, n))
    for i in range(n - 1):
        h: float = z[i + 1] - z[i]
        for x in range(8):
            C[x, i + 1] = C[x, i] + h * (odefunction(z[i], C0))[x]

    return [z, C]


# print("Euler: ", calculConcentrationsEuler([0, 0.29], C0))


solution = calculConcentrationsIVP([0, 0.29], C0)
# print("IVP: ", solution)
# print("IVP z: ", solution.t)
# print("IVP T: ", solution.y[6])

# Graphe
"""Graphe pour IVP"""
fig, plot = plt.subplots(2, 2)
plot[0, 0].plot(solution.t, solution.y[0, :], label="CH4")
plot[0, 0].plot(solution.t, solution.y[1, :], label="H2O")
plot[0, 0].plot(solution.t, solution.y[2, :], label="H2")
plot[0, 0].plot(solution.t, solution.y[3, :], label="CO")
plot[0, 0].plot(solution.t, solution.y[4, :], label="CO2")
plot[0, 1].plot(solution.t, solution.y[5, :], label="X")
plot[1, 0].plot(solution.t, solution.y[6, :], label="T")
plot[1, 1].plot(solution.t, solution.y[7, :], label="P")
plt.xlabel("Longueur du réacteur (m)")
plt.ylabel("Concentration (kmol/m3)")
plot[0, 0].legend()
plot[0, 1].legend()
plot[1, 0].legend()
plot[1, 1].legend()

plt.grid(True)
plot[0, 0].grid(True)
plot[0, 1].grid(True)
plot[1, 0].grid(True)
plot[1, 1].grid(True)
plt.show()

"""Graphe pour Euler"""
# z, concentrations = calculConcentrationsEuler([0, 0.29], C0)
# plt.plot(z, concentrations[0, :], label="CH4")
# plt.plot(z, concentrations[1, :], label="H2O")
# plt.plot(z, concentrations[2, :], label="H2")
# plt.plot(z, concentrations[3, :], label="CO")
# plt.plot(z, concentrations[4, :], label="CO2")
# plt.xlabel("Longueur du réacteur en (m)")
# plt.ylabel("Concentration des composés en (kmol/m^3)")
# plt.legend()
# plt.title("Concentrations des composés en fonction de la longueur du réacteur")
# plt.grid(True)
# plt.show()

# print(odefunction(0, C0))
