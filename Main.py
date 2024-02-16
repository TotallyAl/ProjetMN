#!/usr/bin/env python
from RechercheRacine import bissection, secante


def f(x: float) -> float:
    return x**2 - 3 * x + 1


solution: list = bissection(f, -5, 10, 0.00001)
print(solution)


# Changement
