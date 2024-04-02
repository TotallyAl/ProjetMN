import numpy as np
from scipy.integrate import solve_ivp
from Derivee import odefunction, odefunction_g, odefunction_q
from Config import Constantes
from matplotlib import pyplot as plt

# C_CH4_b = 1 / 22.4 / 4
# C_H2O_b = 3 * C_CH4_b
# T = 973.15
# C0 = np.array([C_CH4_b, C_H2O_b, 1e-3, 0, 0, 0, T, 3])


def calculConcentrationsIVP(interval: list, C0: list) -> list:
    sol = solve_ivp(
        odefunction,
        interval,
        t_eval=np.linspace(interval[0], interval[1], 1000000),
        method="RK45",
        rtol=1e-6,
        y0=C0,
    )
    return [sol.t, sol.y]


def calculConcentrationsEuler(interval: list, C0: list) -> list:
    """
    # Méthode d'Euler

    ### Explication de la méthode d'Euler
    ### Paramètres a prendre en compte
    ### Exemple d'utilisation
    """
    n = 1000000  # 100k iterations
    z = np.linspace(interval[0], interval[1], n)
    """Cette liste contient les valeurs de z qui seront utilisés pour calculer les concentrations."""
    C = np.zeros((8, n))
    """Cette matrice contiendra les concentrations des composés à chaque itération."""
    C[:, 0] = C0
    """On initialise la première colonne de la matrice C avec les concentrations initiales."""
    h: float = z[1] - z[0]
    """On calcule le pas une fois car il est constant. Cela permet d\'économiser du temps car nous ne devons pas le calculer à chaque itération."""
    for i in range(n - 1):
        C[:, i + 1] = C[:, i] + h * (odefunction(z[i], C[:, i]))
    return [z, C]


def calculConcentrationsIVP_g(
    interval: list, C0: list, param: str = "z", captage: bool = True
) -> list:
    sol = solve_ivp(
        lambda var, C: odefunction_g(var, C, param, captage),
        interval,
        t_eval=np.linspace(interval[0], interval[1], 1000000),
        method="RK45",
        y0=C0,
    )
    return [sol.t, sol.y]


def calculConcentrationsIVP_g2(interval: list, C0: list) -> list:
    u_s = np.arange(interval[0], interval[1], 0.001)
    matrix = np.zeros((8, len(u_s)))
    x: int = 0  # Compteur
    for g in u_s:
        sol = solve_ivp(
            odefunction_q,
            t_span=[0, 0.29],
            y0=C0,
            method="RK45",
            args=(Constantes.u_g, g),
        )
        matrix[:, x] = sol.y[:, -1]
        x += 1
    return [u_s, matrix]


def calculConcentrationsIVP_g3(interval: list, C0: list) -> list:
    u_g = np.arange(interval[0], interval[1], 0.001)
    matrix = np.zeros((8, len(u_g)))
    x: int = 0  # Compteur
    for g in u_g:
        sol = solve_ivp(
            odefunction_q,
            t_span=[0, 0.29],
            y0=C0,
            method="RK45",
            args=(g, Constantes.u_s),
        )
        matrix[:, x] = sol.y[:, -1]
        x += 1
    return [u_g, matrix]
