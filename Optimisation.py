from RechercheRacine import bissection, secante
from scipy.integrate import solve_ivp
from Derivee import odefunction
import numpy as np
from matplotlib import pyplot as plt

from Config import Constantes

C_CH4_b = 1 / (4 * 22.4)
C_H2O_b = 3 * C_CH4_b
T = 973.15
C0 = np.array([C_CH4_b, C_H2O_b, 1e-10, 0, 0, 0, T, 3])


def optimisation(C: list, Y: float, setting: str = "bissection") -> float:
    us_constante = Constantes.u_s

    """Ce code trouve la fonction des concentrations de CO2 que nous utiliserons pour trouver CO2"""

    def f(u_s: float) -> float:
        Constantes.u_s = u_s
        sol = solve_ivp(
            fun=odefunction, t_span=[0, 0.29], y0=C, method="RK45", args=(True,)
        )
        somme_C = sol.y[0, -1] + sol.y[2, -1] + sol.y[3, -1] + sol.y[4, -1]
        co2 = (sol.y[4, -1] / somme_C) * 100 - Y
        return co2

    Constantes.u_s = us_constante
    if setting == "bissection":
        u_s = bissection(f, 1e-2, 3e-1, 1e-6)[0]
    elif setting == "secante":
        u_s = secante(f, 1e-2, 3e-1, 1e-6)[0]
    # Valeurs qui fonctionnent bien -> 1e-2 et 0.2 (Methode de la bissection et de la sécante!!)
    return u_s


print(f"{optimisation(C0, 7.5)}")


def variation_temperature(interval: list, C: list) -> list:
    t = np.arange(interval[0], interval[1], 1)
    sol = []
    tw_constante = Constantes.t_w
    for v in t:
        Constantes.t_w = v
        sol.append(optimisation(C, 7.5))
    Constantes.t_w = tw_constante
    return [t, sol]


t, u_s = variation_temperature([973.15, 1073.15], C0)
plt.close()
plt.plot(t, u_s, label="$u_s$", color="blue")
plt.title(
    "Variation du Flux d'Entrée de $CaO$ en Fonction de la Température d'Entrée du Réacteur"
)
plt.xlabel("Température d'Entrée du Réacteur (K)")
plt.ylabel("Flux d'Entrée de $CaO$ [m/s]")
plt.legend()
plt.grid()
plt.show()
