from RechercheRacine import bissection, secante
from scipy.integrate import solve_ivp
from Derivee import odefunction_q
import numpy as np

C_CH4_b = 1 / 22.4 / 4
C_H2O_b = 3 * C_CH4_b
T = 973.15
C0 = np.array([C_CH4_b, C_H2O_b, 1e-20, 0, 0, 0, T, 3])


def optimisation(u_g: float, C: list, Y: float) -> float:

    def f(u_s: float) -> float:
        sol = solve_ivp(lambda z, C: odefunction_q(z, C, u_g, u_s), [0, 0.29], C)
        somme_C = sol.y[0, -1] + sol.y[2, -1] + sol.y[3, -1] + sol.y[4, -1]
        co2 = (sol.y[4, -1] / somme_C) * 100 - Y
        return co2

    u_s = bissection(f, 1e-3, 0.2, 1e-6)
    return u_s


print(f"{optimisation(1, C0, 7.5)}")
