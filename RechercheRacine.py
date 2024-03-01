import numpy as np


class Config:
    max_iter: int = 1000
    error: int = 0.0000000000001


"""
Les méthodes récursives ne sont seront pas utilisés car elle ont quelques désavantages dans le cadre du projet:
    1. La récursions coûte énormément en temps et en mémoire.
    2. Si le niveau de précision est haut, la méthode risque de s'arrêter car elle "sature" la mémoire allouée par le 
        "compilateur".

Mêmes si la récursion peut être plus rapide dans certains cas ou qu'elle soit plus facile à lire/écrire, nous utiliserons l'itération.
"""


def secante_recursive(f, x0: float, x1: float, tol: float) -> list:
    if tol < 0:
        return [0, -1]
    if f(x0) == f(x1):
        print("f(x0) == f(x1)")
        return [0, -1]
    x2 = x1 - (f(x1) * ((x1 - x0) / (f(x1) - f(x0))))
    if np.abs(f(x2)) < tol:
        return [x2, 0]
    return secante_recursive(f, x1, x2, tol)


def bissection_recursive(f, x0: float, x1: float, tol: float) -> list:
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


def secante(f, x0: float, x1: float, tol: float) -> list:
    if tol < 0:
        tol = np.abs(tol)

    if x0 == x1:
        print("x0 et x1 sont égaux. Intervalle nul.")
        return [0, 1]

    f0 = f(x0)
    iter = 0
    while iter <= Config.max_iter:
        f1 = f(x1)

        # On veut savoir si f(x0) == f(x1), avec le probleme d'arrondi des ordinateurs, nous ne pouvons pas utiliser le == de comparaison.
        # Nous devons donc soustraire f(x0) et f(x1) et regarder si la différence est plus petite qu'un marge d'erreur. Ici nous utilisons la tolérance (tol)
        if np.abs(f0 - f1) < Config.error:
            print(
                "f0 et f1 sont trop proches. La méthode de la sécante n'est pas un algorithme adapté pour cette fonction."
            )
            return [0, 1]

        if f0 == 0:
            return [x0, 0]

        if f1 == 0:
            return [x1, 0]

        x2 = x1 - (f1 * ((x1 - x0) / (f1 - f0)))
        if np.abs(x1 - x0) < tol:
            return [x2, 0]
        iter += 1
        x0 = x1
        f0 = f1
        x1 = x2
    print(
        f"Nous avons atteint la limite maximum d'itérations({Config.max_iter}), la méthode n'a pas convergé."
    )
    return [0, -1]


def bissection(f, x0: float, x1: float, tol: float) -> list:
    if tol < 0:
        tol = np.abs(tol)

    if x0 == x1:
        print("x0 et x1 sont égaux. L'intervalle est nul.")
        return [0, 1]

    f0 = f(x0)
    f1 = f(x1)

    if f0 == 0:
        return [x0, 0]

    if f1 == 0:
        return [x1, 0]

    if f0 * f1 > 0:
        print("f(x0) et f(x1) ont le même signe. L'hypothèse n'est pas vérifiée.")
        return [0, 1]

    while np.abs(x0 - x1) > tol:
        m = (x0 + x1) / 2
        fm = f(m)
        if f0 * fm < 0:
            x1 = m
        else:
            x0 = m
            f0 = fm
    return [m, 0]
