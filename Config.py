import numpy as np


class RRConfig:
    max_iter: int = 1000


class Constantes:
    """
    Toutes les valeurs des constantes peuvent être trouvés dans l'énoncé du projet.
    Ces constantes peuvent changer à n'importe quel moment durant le projet.
    """

    M_k: float = 303
    """Constante (adimensionnelle)"""

    N_k: float = -13146
    """Constante (adimensionnelle)"""

    M_b: float = 1.6
    """Constante (adimensionnelle)"""

    N_b: float = 5649
    """Constante (adimensionnelle)"""

    M_CaO: float = 56
    """Masse molaire du CaO (kg/mol)"""

    T: float = 1
    """Température (K)"""


class Valeurs:
    # Valeurs qui dependent des constantes (Dans la classe constante)

    k_c: float = Constantes.M_k * np.exp(Constantes.N_k / Constantes.T)
    """La vitesse apparente de carbonatation (s^-1)"""

    b: float = Constantes.M_b * np.exp(Constantes.N_b / Constantes.T)
    """Le temps pour arriver à la moitié de la conversion ultime Xu (s)"""

    X_u: float = k_c * b
    """Conversion ultime (adimensionnelle)"""
