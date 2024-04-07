import numpy as np
from Config import Constantes
import matplotlib.pyplot as plt
from SimReacteur import calculConcentrationsIVP

C_CH4_b = 1 / (4 * 22.4)
C_H2O_b = 3 * C_CH4_b
T = 973.15
C0 = np.array([C_CH4_b, C_H2O_b, 1e-10, 0, 0, 0, T, 3])


# Déterminer graphiquement les valeurs de l'intervalle pour la méthode de la bissection
def C_Finales_Variation_flux_CaO(pct: float, C0: list):
    """
    Crée un graphique illustrant l'effet d'un flux de CaO plus important sur les concentrations finales
    en gaz secs afin de déterminer visuellement la méthode  de recherche de racine appropriée à appliquer
    à la fonction Optimisation_Reacteur du module Optimisation_Fonctionnement. Permet également de déterminer
    des bornes approriées.

    Args:
        pct (float): Pourcentage de CO2 reformé demandé.
    """

    # Initialisation des tableaux et paramètres
    u_s = []
    pcts_CO2_reforme = []
    valeurs_u_s = np.linspace(1e-5, 1, 100)

    # Calcul des concentrations finales en gaz secs pour chaque valeur de u_s
    for i in valeurs_u_s:
        Constantes.u_s = i
        solution_t, solution_y = calculConcentrationsIVP([0, 0.29], C0)
        pct_CO2_reforme = (solution_y[4, -1]) / (
            solution_y[0, -1] + np.sum(solution_y[2:5, -1])
        ) * 100 - pct
        pcts_CO2_reforme.append(pct_CO2_reforme)
        u_s.append(i)

    # Création du graphique
    plt.figure(figsize=(20, 10))
    plt.plot(u_s[:], pcts_CO2_reforme[:])
    plt.xlabel("Flux d'Entrée de CaO [m/s]")
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.ylabel(
        "Différence Entre le Pourcentage de $CO_2$ reformé (gaz sec) et le pourcentage demandé [%]"
    )
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()


# C_Finales_Variation_flux_CaO(7.5, C0)
