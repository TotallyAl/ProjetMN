#!/usr/bin/env python
from RechercheRacine import (
    secante,
    secante_recursive,
    bissection_recursive,
    bissection,
)

import numpy as np
import math


def f(x: float) -> float:
    return 3 * x**3 - 4 * x - 17


solution: float
statut: int
print(bissection(f, -3, 4, 0.01))
print(secante(f, -3, 4, 0.01))
