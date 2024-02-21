from typing import Callable
import numpy as np

from Config import RRConfig

"""
Les méthodes récursives ne sont seront pas utilisés car elle ont quelques désavantages dans le cadre du projet:
    1. La récursions coûte énormément en temps et en mémoire.
    2. Si le niveau de précision est haut, la méthode risque de s'arrêter car elle "sature" la mémoire allouée par le 
        "compilateur".

Mêmes si la récursion peut être plus rapide dans certains cas ou qu'elle soit plus facile à lire/écrire, nous utiliserons l'itération.
"""


def secante_recursive(
    f: Callable[[float], float], x0: float, x1: float, tol: float
) -> list:
    if tol < 0:
        return [0, -1]
    if f(x0) == f(x1):
        print("f(x0) == f(x1)")
        return [0, -1]
    x2 = x1 - (f(x1) * ((x1 - x0) / (f(x1) - f(x0))))
    if np.abs(f(x2)) < tol:
        return [x2, 0]
    return secante_recursive(f, x1, x2, tol)


def bissection_recursive(
    f: Callable[[float], float], x0: float, x1: float, tol: float
) -> list:
    if f(x0) * f(x1) > 0:
        print("f(x0) et f(x1) sont de meme signes")
        return [0, -1]
    m = (x0 + x1) / 2

    if np.abs(f(m)) < tol:
        return [m, 0]

    if f(x0) * f(m) < 0:
        return bissection_recursive(f, x0, m, tol)
    return bissection_recursive(f, m, x1, tol)


"""
Méthode plus directe qui ne consomme pas spécialement beaucoup de mémoire.
-> Utilisation de boucles "while".
"""


def secante_iterative(
    f: Callable[[float], float], x0: float, x1: float, tol: float
) -> list:
    iter = 0
    f0 = f(x0)
    while iter <= RRConfig.max_iter:
        f1 = f(x1)
        if f0 == f1:
            print("f0 et f1 ont la même valeur")
            return [0, 1]
        x2 = x1 - (f1 * ((x1 - x0) / (f1 - f0)))
        if np.abs(f(x2)) < tol:
            return [x2, 0]
        iter += 1
        x0 = x1
        f0 = f1
        x1 = x2
    print(
        f"Nous avons atteint la limite maximum d'itérations({RRConfig.max_iter}), la méthode ne converge donc pas."
    )
    return [0, -1]


def bissection_iterative(
    f: Callable[[float], float], x0: float, x1: float, tol: float
) -> list:
    if f(x0) * f(x1) > 0:
        print("f(x0) et f(x1) ont le même signe. L'hypothèse n'est pas atteinte.")
        return [0, 1]

    iter = 0
    while iter <= RRConfig.max_iter:
        m = (x0 + x1) / 2
        if np.abs(f(m)) < tol:
            return [m, 0]
        iter += 1
        if f(x0) * f(m) < 0:
            x1 = m
        else:
            x0 = m
    print(
        f"Nous avons atteint la limite maximum d'itérations({RRConfig.max_iter}), la méthode ne converge donc pas."
    )
    return [0, -1]
