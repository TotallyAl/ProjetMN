import numpy as np
from scipy.integrate import solve_ivp
from Derivee import odefunction
from Config import Constantes

# C_CH4_b = 1 / 22.4 / 4
# C_H2O_b = 3 * C_CH4_b
# T = 973.15
# C0 = np.array([C_CH4_b, C_H2O_b, 1e-3, 0, 0, 0, T, 3])


def calculConcentrationsIVP(interval: list, C0: list, captage: bool = True) -> list:
    """
    # CalculConcentrationsIVP
    ### Paramètres a prendre en compte
        -> interval (list): Liste contenant les bornes de l'intervalle de la longueur du réacteur.
        -> C0 (list): Liste contenant les concentrations initiales des composés.
        -> captage (bool): Booléen indiquant si le captage est activé ou non.
    ### Exemple d'utilisation
    ```py
    calculConcentrationsIVP([0, 0.29], C0, True)
    ```
    """
    sol = solve_ivp(
        fun=odefunction,
        t_span=interval,
        t_eval=np.linspace(interval[0], interval[1], 1000000),
        method="RK45",
        rtol=1e-6,
        y0=C0,
        args=(captage,),
    )
    return [sol.t, sol.y]


def calculConcentrationsEuler(interval: list, C0: list, captage: bool = True) -> list:
    """
    # Méthode d'Euler

    ### Paramètres a prendre en compte
        -> interval (list): Liste contenant les bornes de l'intervalle de la longueur du réacteur.
        -> C0 (list): Liste contenant les concentrations initiales des composés.
        -> captage (bool): Booléen indiquant si le captage est activé ou non.
    ### Exemple d'utilisation
    """
    n = 100000  # 1M iterations
    z = np.linspace(interval[0], interval[1], n)
    """Cette liste contient les valeurs de z qui seront utilisés pour calculer les concentrations."""
    C = np.zeros((8, n))
    """Cette matrice contiendra les concentrations des composés à chaque itération."""
    C[:, 0] = C0
    """On initialise la première colonne de la matrice C avec les concentrations initiales."""
    h: float = z[1] - z[0]
    """On calcule le pas une fois car il est constant. Cela permet d\'économiser du temps car nous ne devons pas le calculer à chaque itération."""
    for i in range(n - 1):
        C[:, i + 1] = C[:, i] + h * (odefunction(z[i], C[:, i], captage))
        """Formule de Euler explicite -> Ci+1 = Ci + h * f(z, Ci)"""
    return [z, C]
