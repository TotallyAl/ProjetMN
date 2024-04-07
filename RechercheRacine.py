import numpy as np


class Config:
    max_iter: int = 1000
    error: int = 10e-30


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
    """On place f(x0) dans une variable pour eviter de la calculer à chaque itération. Cela permet de gagner du temps et de la place en mémoire."""
    iter = 0
    while iter <= Config.max_iter:
        f1 = f(x1)

        # On veut savoir si f(x0) == f(x1), avec le probleme d'arrondi des ordinateurs, nous ne pouvons pas utiliser le == de comparaison.
        # Nous devons donc soustraire f(x0) et f(x1) et regarder si la différence est plus petite qu'un marge d'erreur. Ici nous utilisons la tolérance (tol)
        """
        Vu que f(x0) et f(x1) sont des valeurs flottantes, une comparaison en == n'est pas recommandée car les valeurs peuvent être légèrement différentes.
        """
        if np.abs(f0 - f1) < Config.error:
            print(
                "f0 et f1 sont trop proches. La méthode de la sécante n'est pas un algorithme adapté pour cette fonction."
            )
            return [0, 1]

        if np.abs(f0) < tol:
            return [x0, 0]

        if np.abs(f1) < tol:
            return [x1, 0]

        x2 = x1 - (f1 * ((x1 - x0) / (f1 - f0)))
        """Ici, nous utilisons le critère de Cauchy pour voir si nous avons atteint la convergence. Si la différence entre x1 et x0 est plus petite que la tolérance, nous avons atteint la convergence."""
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

    if np.abs(f0) < tol:
        return [x0, 0]

    if np.abs(f1) < tol:
        return [x1, 0]

    if f0 * f1 > 0:
        print("f(x0) et f(x1) ont le même signe. L'hypothèse n'est pas vérifiée.")
        return [0, 1]

    """Ici, nous utilisons le critère de Cauchy pour voir si nous avons atteint la convergence. Si la différence entre x1 et x0 est plus petite que la tolérance, nous avons atteint la convergence."""
    while np.abs(x0 - x1) > tol:
        m = (x0 + x1) / 2
        fm = f(m)
        if f0 * fm < 0:
            x1 = m
        else:
            x0 = m
            f0 = fm
    return [m, 0]
