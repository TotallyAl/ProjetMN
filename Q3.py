from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from Derivee import odefunction

from SimReacteur import (
    calculConcentrationsEuler,
    calculConcentrationsIVP,
)
from Config import Constantes

C_CH4_b = 1 / (4 * 22.4)
C_H2O_b = 3 * C_CH4_b
T = 973.15
C0 = np.array([C_CH4_b, C_H2O_b, 1e-3, 0, 0, 0, T, 3])


def variation_us(interval: list, C0: list) -> list:
    u_s = np.arange(interval[0], interval[1], 0.01)
    matrix = np.zeros((8, len(u_s)))
    x = 0  # Compteur
    us_constante = Constantes.u_s
    for v in u_s:
        Constantes.u_s = v
        sol = solve_ivp(
            fun=odefunction, t_span=[0, 0.29], y0=C0, method="RK45", args=(False,)
        )
        matrix[:, x] = sol.y[:, -1]
        # On recupère les valeurs à la fin de l'intervalle et on les stoques dans une matrice.
        x += 1
    Constantes.u_s = us_constante
    # on remet la valeur de us a sa valeur initiale
    return [u_s, matrix]


def variation_ug(interval: list, C0: list) -> list:
    u_g = np.arange(interval[0], interval[1], 0.01)
    matrix = np.zeros((8, len(u_g)))
    ug_constante = Constantes.u_g
    x = 0  # Compteur
    for v in u_g:
        Constantes.u_g = v
        sol = solve_ivp(
            fun=odefunction, t_span=[0, 0.29], y0=C0, method="RK45", args=(False,)
        )
        matrix[:, x] = sol.y[:, -1]
        x += 1
    Constantes.u_g = ug_constante
    return [u_g, matrix]


# z, C = variation_us([1e-5, 1], C0)
# z, C = variation_ug([0.5, 30], C0)
z, C = calculConcentrationsIVP([0, 0.29], C0, True)
z1, C1 = calculConcentrationsIVP([0, 0.29], C0, False)

plt.plot(z, C[0], label="$CH_4$")
plt.plot(z1, C1[0], label="$CH_4$ sans captage")
plt.plot(z, C[2], label="$H_2$")
plt.plot(z1, C1[2], label="$H_2$ sans captage")
plt.plot(z, C[3], label="$CO$")
plt.plot(z1, C1[3], label="$CO$ sans captage")
plt.plot(z, C[4], label="$CO_2$")
plt.plot(z1, C1[4], label="$CO_2$ sans captage")
# plt.plot(z, C[6], label="$T$")
# plt.plot(z1, C1[6], label="$T$ sans captage")q
plt.grid()
plt.legend()
plt.xlabel("$u_s$")
plt.ylabel("Concentration")
plt.show()
