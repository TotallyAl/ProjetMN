import numpy as np
from Config import Constantes


def dCi_dz(r_i: float, r_cbn: float) -> float:
    return (
        Constantes.eta * (1 - Constantes.epsilon) * Constantes.rho_cat * r_i
        - (1 - Constantes.epsilon) * Constantes.rho_CaO * r_cbn
    ) / Constantes.u_g


def h_w(Re_p: float) -> float:
    if (
        (Re_p > 20)
        and (Constantes.d_p / Constantes.D_R > 0.05)
        and (Constantes.d_p / Constantes.D_R < 0.3)
    ):
        return (
            2.03
            * (Constantes.k_g / Constantes.D_R)
            * Re_p**0.8
            * np.exp(-6 * Constantes.d_p / Constantes.D_R)
        )
    elif Re_p < 20:
        return 6.15 * (Constantes.k0_z / Constantes.D_R)
    else:
        print("Re_p: ", Re_p)
        raise ValueError("Re_p is not in the right range")


def odefunction(z: float, C: list) -> list:

    C_CH4, C_H2O, C_H2, C_CO, C_CO2, X, T, P = C

    # Cherchons dCi_dz pour tous les composés se trouvant dans la liste C
    """
    
    ===Calcul de dCi_dz===

    Nous pouvons calculer r_CBN.
    Pour cela nous avons besoin de k_c(T) et de b(T) qui dependent tous les deux de la température en Kelvin.

    Nous devons commencer par chercher les pressions partielles des composés dans le système.
    Cela nous permettra de trouver les r_i de chaque composé.

    Nous pouvons calculer la pression partielle grace a la formule de Dalton
    """

    # Calculons k_c(T) et b(T)
    k_c: float = Constantes.M_k * np.exp(Constantes.N_k / T)
    b: float = Constantes.M_b * np.exp(Constantes.N_b / T)
    X_u: float = k_c * b

    # Calculons r_CBN
    r_CBN: float = (k_c / Constantes.M_CaO) * ((1 - X / X_u) ** 2)
    """Le taux de concentration de CO2 par carbonatation en (kmol * kg^-1 * s^-1)"""

    # Les pressions partielles des composés dans C en (Pa)
    C_TOT = C_CH4 + C_H2O + C_H2 + C_CO + C_CO2
    P_CH4 = P * C_CH4 / C_TOT
    P_H2O = P * C_H2O / C_TOT
    P_H2 = P * C_H2 / C_TOT
    P_CO = P * C_CO / C_TOT
    P_CO2 = P * C_CO2 / C_TOT

    """Nous devons calculer les vitesses de réaction pour chaque composé:
        -> Nous devons calculer K_j, k_j et K_i
    """
    # Calculons K_j qui dependent de la température
    K1: float = 4.707 * (10 ** (12)) * np.exp(-224000 / (Constantes.R * T))
    """Constante d'équilibre de la réaction R1 en (bar^2)"""
    K3: float = 1.142 * (10 ** (-2)) * np.exp(37300 / (Constantes.R * T))
    """Constante d'équilibre de la réaction R3 (adimensionnelle)"""
    K2: float = K1 * K3
    """Constante d'équilibre de la réaction R2 en (bar^2)"""

    # Calculons les K_i
    K_CH4: float = 0.179 * np.exp(((38280 / Constantes.R) * ((1 / T) - (1 / 823))))
    K_H2O: float = 0.4152 * np.exp(((-88680 / Constantes.R) * ((1 / T) - (1 / 823))))
    K_H2: float = 0.0296 * np.exp(((82900 / Constantes.R) * ((1 / T) - (1 / 648))))
    K_CO: float = 40.91 * np.exp(((70650 / Constantes.R) * ((1 / T) - (1 / 648))))

    # calculons les k_j
    k1: float = (
        (1.842 / 3600) * 1e-4 * np.exp((-240100 / Constantes.R) * ((1 / T) - (1 / 648)))
    )
    """Constante de vitesse de la réaction en (kmol * bar^1/2 * kg_cat^-1 * s^-1)"""

    k2: float = (
        (2.193 / 3600) * 1e-5 * np.exp((-243900 / Constantes.R) * ((1 / T) - (1 / 648)))
    )
    """Constante de vitesse de la réaction en (kmol * bar^1/2 * kg_cat^-1 * s^-1)"""

    k3: float = (7.558 / 3600) * np.exp((-67130 / Constantes.R) * ((1 / T) - (1 / 648)))
    """Constante de vitesse de la réaction en (kmol * kg_cat^-1 * s^-1 * bar^-1)"""

    # Calculons DEN et les différents R_i, i -> [1, 3]
    DEN: float = 1 + K_CO * P_CO + K_H2 * P_H2 + K_CH4 * P_CH4 + K_H2O * P_H2O / P_H2

    R1 = (k1 / P_H2**2.5) * (P_CH4 * P_H2O - (P_H2**3 * P_CO) / K1) / (DEN**2)
    """Vitesse de réaction en (kmol * kg^-1 * s^-1)"""
    R2 = (k2 / P_H2**3.5) * (P_CH4 * P_H2O**2 - (P_H2**4 * P_CO2) / K2) / (DEN**2)
    """Vitesse de réaction en (kmol * kg^-1 * s^-1)"""
    R3 = (k3 / P_H2) * (P_CO * P_H2O - (P_H2 * P_CO2) / K3) / (DEN**2)
    """Vitesse de réaction en (kmol * kg^-1 * s^-1)"""

    # Calculons les différents r_i
    r_CH4 = -R1 - R2
    r_H2O = -R1 - 2 * R2 - R3
    r_H2 = 3 * R1 + 4 * R2 + R3
    r_CO = R1 - R3
    r_CO2 = R2 + R3

    """
    ===Calcul de dX_dz===
    """

    dX_dz: float = (Constantes.M_CaO / Constantes.u_s) * r_CBN

    """
    ===Calcul de dT_dz===
    """

    rho_s: float = (Constantes.W_cat + Constantes.W_CaO) / (
        Constantes.W_cat / Constantes.rho_cat + Constantes.W_CaO / Constantes.rho_CaO
    )

    rho_g: float = (100 / (Constantes.R * T)) * (
        Constantes.M_CH4 * P_CH4
        + Constantes.M_H2O * P_H2O
        + Constantes.M_H2 * P_H2
        + Constantes.M_CO * P_CO
        + Constantes.M_CO2 * P_CO2
    )

    Re_p: float = (
        Constantes.u_g * Constantes.epsilon * rho_g * Constantes.d_p
    ) / Constantes.mu

    NUM: float = (
        -(1 - Constantes.epsilon)
        * Constantes.rho_cat
        * (
            Constantes.eta
            * (R1 * Constantes.H_R1 + R2 * Constantes.H_R2 + R3 * Constantes.H_R3)
        )
        - (1 - Constantes.epsilon) * Constantes.rho_CaO * r_CBN * Constantes.H_CBN
        + h_w(Re_p) * (Constantes.t_w - T) * (4 / Constantes.D_R)
    )

    DENOM: float = (
        (1 - Constantes.epsilon) * rho_s * Constantes.u_s * Constantes.C_ps
        + rho_g * Constantes.u_g * Constantes.C_pg
    )

    dT_dz: float = NUM / DENOM

    """
    ===Calcul de dP_dz===
    """

    dP_dz: float = -(
        (rho_g * (Constantes.u_g**2) / Constantes.d_p)
        * ((1 - Constantes.epsilon) / Constantes.epsilon)
        * (
            (150 * (1 - Constantes.epsilon) * Constantes.mu)
            / (Constantes.d_p * rho_g * Constantes.u_g)
            + 1.75
        )
        * (10 ** (-5))
    )

    # C = (C_CH4, C_H20, C_H2, C_CO, C_CO2, X, T, P)

    return [
        dCi_dz(r_CH4, r_CBN),
        dCi_dz(r_H2O, r_CBN),
        dCi_dz(r_H2, r_CBN),
        dCi_dz(r_CO, r_CBN),
        dCi_dz(r_CO2, r_CBN),
        dX_dz,
        dT_dz,
        dP_dz,
    ]
