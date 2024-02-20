from typing import Callable
import numpy as np


def secante_recursive(
    f: Callable[[float], float], x0: float, x1: float, tol: float, max_iter: int = 100
) -> list:
    if tol < 0:
        return [0, -1]

    iter = 0
    f0 = f(x0)
    while True:
        f1 = f(x1)
        if f0 == f1:
            print("f0 et f1 ont la meme valeur")
            return [0, -1]
        x2 = x1 - (f1 * ((x1 - x0) / (f1 - f0)))
        if np.abs(f(x2)) < tol:
            return [x2, 0]
        if iter > max_iter:
            return [x2, -1]
        iter += 1
        x0 = x1
        f0 = f1
        x1 = x2


def secante_iteration(
    f: Callable[[float], float], x0: float, x1: float, tol: float, max_iter: int = 100
) -> list:
    if tol < 0:
        return [0, -1]

    iter = 0
    f0 = f(x0)
    while True:
        f1 = f(x1)
        if f0 == f1:
            print("f0 et f1 ont la meme valeur")
            return [0, -1]
        x2 = x1 - (f1 * ((x1 - x0) / (f1 - f0)))
        if np.abs(f(x2)) < tol:
            return [x2, 0]
        if iter > max_iter:
            print("Reached max iteration")
            return [x2, -1]
        iter += 1
        x0 = x1
        f0 = f1
        x1 = x2


def bissection_recursive(
    f: Callable[[float], float], x0: float, x1: float, tol: float, max_iter: int = 100
) -> list:
    if f(x0) * f(x1) > 0:
        print("f(x0) et f(x1) sont de meme signes")
        return [0, -1]
    if tol < 0:
        print("Tol is negatif of null")
        return [0, -1]

    m = (x0 + x1) / 2

    if np.abs(f(m)) < tol:
        return [m, 0]

    if f(x0) * f(m) < 0:
        return bissection_recursive(f, x0, m, tol)
    return bissection_recursive(f, m, x1, tol)


def bissection_iterative(
    f: Callable[[float], float], x0: float, x1: float, tol: float, max_iter: int = 100
) -> list:
    if f(x0) * f(x1) > 0:
        print("f(x0) et f(x1) sont de meme signes")
        return [0, -1]
    if tol < 0:
        print("Tol is negatif of null")
        return [0, -1]

    iter = 0
    while iter <= max_iter:
        m = (x0 + x1) / 2
        if np.abs(f(m)) < tol:
            return [m, 0]
        iter += 1
        if f(x0) * f(m) < 0:
            x1 = m
        else:
            x0 = m
    print("Reached maximum amount of iterations")
    return [0, -1]
