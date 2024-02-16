def bissection(f, x0: float, x1: float, tol: float) -> list:
    """
    Hypothèses initiales à remplir: -> f(x) doit etre continue sur l'intervalle [x0, x1]
                                    -> f(x0) * f(x1) < 0
                                    -> tol > 0
    """
    # Hypothèses 1: f(x) doit etre continue sur l'intervalle [x0, x1]
    # Hypothèses 2: f(x0) * f(x1) < 0
    if f(x0) * f(x1) > 0:
        print("The selected interval is invalid for this algorithm.")
        return
    # Hypothèses 3: tol > 0
    if tol < 0:
        print("Tol is negative or null.")
        return

    # Exécution de l'algorithme puisque les hypothèses sont remplies

    # Recherche du point se situant au milieu de l'intervalle
    m = (x0 + x1) / 2

    # Si le point au mileu de l'intervalle est plus petit que l'erreur, ce point est concidéré comme la solution
    if m < tol:
        return m

    # On redéfinit l'intervalle de recherche pour la prochaine itération.
    if f(x0) * f(m) < 0:
        return bissection(f, x0, m, tol)
    return bissection(f, m, x1, tol)


def secante(f, x0: float, x1: float, tol: float) -> list:
    pass
