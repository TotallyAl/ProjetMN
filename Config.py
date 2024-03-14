import numpy as np


class Constantes:
    """
    # Constantes
    Cette classe regrouge toutes les constantes dans ce fichier
    """

    C_pg: float = 8.45
    """Constante en kJ/(kg*K)"""

    C_ps: float = 0.98
    """Constante en kJ/(kg*K)"""

    d_p: float = 3 * 10 ** (-3)
    """Constante en m"""

    D_R: float = 2.4 * 10 ** (-2)
    """Constante en m"""

    k_g: float = 2.59 * 10 ** (-4)
    """Conductivités thermiques du gaz constituant le lit catalytique dans le réacteur en kJ/(m*s*K)"""

    k_s: float = 10 ** (-3)
    """Conductivités thermiques du solide constituant le lit catalytique dans le réacteur en kJ/(m*s*K)"""

    M_CaO: float = 56
    """Masse molaire du CaO (kg/kmol)"""

    M_CH4: float = 16
    """Masse molaire du CH4 (kg/kmol)"""

    M_H2O: float = 18
    """Masse molaire du H2O (kg/kmol)"""

    M_H2: float = 2
    """Masse molaire du H2 (kg/kmol)"""

    M_CO: float = 28
    """Masse molaire du CO (kg/kmol)"""

    M_CO2: float = 44
    """Masse molaire du CO2 (kg/kmol)"""

    W_CaO: float = 83.6 * 10 ** (-3)
    """Flux massiques de CaO (kg/h)"""

    W_cat: float = 16.4 * 10 ** (-3)
    """Flux massiques du catalyseur (kg/h)"""

    epsilon: float = 0.5
    """Prosité du réacteur, constante (adimensionnelle)"""

    mu: float = 2.8 * 10 ** (-3)
    """L'efficacité du réacteur en (Pa*s)"""

    rho_CaO: float = 1620
    """Masse volumique des pellets de CaO en (kg/m^3)"""

    rho_cat: float = 1100
    """Masse volumique du catalyseur en (kg/m^3)"""

    eta: float = 0.3
    """Constante (adimensionnelle)"""

    M_k: float = 303
    """Constante (adimensionnelle)"""

    N_k: float = -13146
    """Constante (adimensionnelle)"""

    M_b: float = 1.6
    """Constante (adimensionnelle)"""

    N_b: float = 5649
    """Constante (adimensionnelle)"""

    R: float = 8.314
    """Constante universelle des gazs parfaits en J * mol^-1 * K^-1"""

    u_g: float = 1
    """Vitesse superficielle du gaz à travers le réacteur en (m/s)"""

    u_s: float = 10 ** (-3)
    """Vitesse linéaire du lit mobile le long du réacteur en (m/s)"""

    H_R1: float = 206.0 * 10**3
    """La chaleur de la réaction R1 en (kJ/kmol)"""

    H_R2: float = 164.9 * 10**3
    """La chaleur de la réaction R2 en (kJ/kmol)"""

    H_R3: float = -41.1 * 10**3
    """La chaleur de la réaction R3 en (kJ/kmol)"""

    H_CBN: float = -178.8 * 10**3
    """La chaleur de la réaction de carbonatation en (kJ/kmol)"""

    # k0_z: float = k_g * (
    #     epsilon + (1 - epsilon) / (0.139 * epsilon - 0.0339 + 2 / 3 * (k_g / k_s))
    # )
    k0_z: float = k_g * (
        epsilon + (1 - epsilon) / (0.139 * epsilon - 0.0339 + 2 / 3 * (k_g / k_s))
    )
    """Constante"""

    t_w: float = 700 + 273.15
    """Temperature t_w en (K)"""
