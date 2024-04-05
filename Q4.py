from RechercheRacine import bissection, secante
from scipy.integrate import solve_ivp
from Derivee import odefunction
import numpy as np
from matplotlib import pyplot as plt

from Config import Constantes

C_CH4_b = 1 / 22.4 / 4
C_H2O_b = 3 * C_CH4_b
T = 973.15
C0 = np.array([C_CH4_b, C_H2O_b, 1e-10, 0, 0, 0, T, 3])


def optimisation(C: list, Y: float) -> float:
    us_constante = Constantes.u_s

    def f(u_s: float) -> float:
        Constantes.u_s = u_s
        sol = solve_ivp(
            fun=odefunction, t_span=[0, 0.29], y0=C, method="RK45", args=(False,)
        )
        somme_C = sol.y[0, -1] + sol.y[2, -1] + sol.y[3, -1] + sol.y[4, -1]
        co2 = (sol.y[4, -1] / somme_C) * 100 - Y
        return co2

    Constantes.u_s = us_constante
    u_s = bissection(f, 1e-3, 0.2, 1e-6)[0]
    return u_s


print(f"{optimisation(C0, 7.5)}")


def variation_température(interval: list) -> list:
    t = np.arange(interval[0], interval[1], 0.1)
    sol = []
    C_CH4_b = 1 / 22.4 / 4
    C_H2O_b = 3 * C_CH4_b
    C0 = np.array([C_CH4_b, C_H2O_b, 1e-10, 0, 0, 0, 973.15, 3])
    for v in t:
        C0[6] = v
        sol.append(optimisation(C0, 7.5))
    return [t, sol]


def variation_temperature(interval: list, C: list) -> list:
    t = np.arange(interval[0], interval[1], 0.1)
    sol = []
    tw_constante = Constantes.t_w
    for v in t:
        Constantes.t_w = v
        sol.append(optimisation(C, 7.5))
        print(sol[-1])
    Constantes.t_w = tw_constante
    return [t, sol]


# t, u_s = variation_température([973.15, 1073.15])
t, u_s = variation_temperature([973.15, 1073.15], C0)
plt.close()
plt.plot(t, u_s, label="$u_s$", color="blue")
plt.xlabel("Température (K)")
plt.ylabel("$u_s$")
plt.legend()
plt.grid()
plt.show()
