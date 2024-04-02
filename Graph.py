from matplotlib import pyplot as plt
import numpy as np

from SimReacteur import (
    calculConcentrationsIVP_g,
    calculConcentrationsEuler,
    calculConcentrationsIVP,
    calculConcentrationsIVP_g2,
    calculConcentrationsIVP_g3,
)

C_CH4_b = 1 / (4 * 22.4)
C_H2O_b = 3 * C_CH4_b
T = 973.15
C0 = np.array([C_CH4_b, C_H2O_b, 1e-3, 0, 0, 0, T, 3])


def concentrationSaveIMG(setting: str, title: str, filename: str) -> None:
    z, C = calculConcentrationsIVP_g([0, 0.29], C0, "z", True)
    z1, C1 = calculConcentrationsIVP_g([0, 0.29], C0, "z", False)
    plt.close()
    if setting == "concentration" or setting == "c":
        plt.plot(z, C[0], label="CH4 avec capture de CO2", color="red")
        plt.plot(z1, C1[0], label="CH4 sans capture de CO2", ls="--", color="orange")
        plt.plot(z, C[2], label="H2 avec capture de CO2", color="blue")
        plt.plot(z1, C1[2], label="H2 sans capture de CO2", ls="--", color="cyan")
        plt.plot(z, C[3], label="CO avec capture de CO2", color="green")
        plt.plot(z1, C1[3], label="CO sans capture de CO2", ls="--", color="lime")
        plt.plot(z, C[4], label="CO2 avec capture de CO2", color="purple")
        plt.plot(z1, C1[4], label="CO2 sans capture de CO2", ls="--", color="magenta")
    elif setting == "temperature" or setting == "t":
        plt.plot(z, C[6], label="T avec capture de CO2", color="red")
        plt.plot(z1, C1[6], label="T sans capture de CO2", ls="--", color="orange")
    else:
        print("Paramètre non valide")
        return
    plt.legend()
    plt.grid()
    plt.title(title)
    plt.show()
    # plt.savefig(filename, dpi=300, format="png")


def concentrationSaveIMG_variation_us(setting: str, title: str, filename: str) -> None:
    # z, C = calculConcentrationsIVP_variation_us([1e-5, 1], C0)
    z, C = calculConcentrationsIVP_g2([1e-5, 1], C0)
    # z, C = calculConcentrationsIVP_g3([1e-5, 10], C0)
    plt.close()
    if setting == "concentration" or setting == "c":
        plt.plot(z, C[0], label="CH4", color="red")
        plt.plot(z, C[2], label="H2", color="blue")
        plt.plot(z, C[3], label="CO", color="green")
        plt.plot(z, C[4], label="CO2", color="purple")
    elif setting == "temperature" or setting == "t":
        plt.plot(z, C[6], label="T", color="orange")
    else:
        print("Paramètre non valide")
        return
    plt.legend()
    plt.grid()
    plt.title(title)
    plt.show()
    # plt.savefig(filename, dpi=300, format="png")


def concentrationSaveIMG_variation_ug(setting: str, title: str, filename: str) -> None:
    # z, C = calculConcentrationsIVP_variation_ug([0.5, 5], C0)
    z, C = calculConcentrationsIVP_g3([1e-5, 1], C0)
    plt.close()
    if setting == "concentration" or setting == "c":
        plt.plot(z, C[0], label="CH4", color="red")
        plt.plot(z, C[2], label="H2", color="blue")
        plt.plot(z, C[3], label="CO", color="green")
        plt.plot(z, C[4], label="CO2", color="purple")
    elif setting == "temperature" or setting == "t":
        plt.plot(z, C[6], label="T", color="orange")
    else:
        print("Paramètre non valide")
        return
    plt.legend()
    plt.grid()
    plt.title(title)
    # plt.show()
    plt.savefig(filename, dpi=300, format="png")
