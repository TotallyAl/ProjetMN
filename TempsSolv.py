import time
import matplotlib.pyplot as plt
from SimReacteur import calculConcentrationsIVP, calculConcentrationsEuler
import numpy as np

C_CH4_b = 1 / (4 * 22.4)
C_H2O_b = 3 * C_CH4_b
T = 973.15
C0 = np.array([C_CH4_b, C_H2O_b, 1e-3, 0, 0, 0, T, 3])


def Temps_Solveur(C0, methode):

    # Initialisation du temps
    start_time = time.time()

    # Choix de la méthode
    if methode == "Euler":
        calculConcentrationsEuler([0, 0.29], C0, True)
    elif methode == "IVP":
        calculConcentrationsIVP([0, 0.29], C0, True)

    return time.time() - start_time


def Temps_Moyen_Solveur(C0):
    """
    Calcule le temps moyen d'exécution des solveurs d'équations différentielles de la méthode d'Euler et de la méthode IVP.

    Args:
        C0 (array): Vecteur des conditions initiales.

    Returns:
        float: Temps moyen d'exécution pour la méthode d'Euler.
        float: Temps moyen d'exécution pour la méthode IVP.
    """

    # Initialisation des tableaux
    Temps_Euler = []
    Temps_IVP = []

    # Calcul des temps de solveur d'edo
    for i in range(100):
        Temps_Euler.append(Temps_Solveur(C0, "Euler"))
        Temps_IVP.append(Temps_Solveur(C0, "IVP"))
        print(f"{i}% iterations")

    # Retourne le temps moyen
    return sum(Temps_Euler) / len(Temps_Euler), sum(Temps_IVP) / len(Temps_IVP)


# Histogramme
def Comparaison_Recherche_Racine(C0):
    """
    Crée un histogramme comparant les temps de résolution des solveurs d'équations différentielles
    de la méthode d'Euler et de la méthode IVP.

    Args:
        C0 (array): Vecteur des conditions initiales.
    """

    # Calcul des temps moyens
    Temps_Euler, Temps_IVP = Temps_Moyen_Solveur(C0)

    # Largeur des barres
    largeur_barre = 0.4

    # Création de l'histogramme
    plt.figure(figsize=(10, 6))
    plt.bar(0, Temps_Euler, width=largeur_barre, label="Euler")
    plt.bar(1, Temps_IVP, width=largeur_barre, label="IVP")
    plt.title(
        "Comparaison des Temps de Résolution des Solveurs d'Equations Différentielles"
    )
    plt.ylabel("Temps [s]")
    plt.legend(loc="best")
    plt.grid(True)

    plt.show()


Comparaison_Recherche_Racine(C0)
