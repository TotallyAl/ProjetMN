#!/usr/bin/env python
from RechercheRacine import (
    secante_iteration,
    secante_recursive,
    bissection_recursive,
    bissection_iterative,
)


def f(x: float) -> float:
    return x**3 - 6 * x + 17


solution: float
statut: int
print(bissection_recursive(f, -4, 3, 0.01))
print(bissection_iterative(f, -4, 3, 0.01))
