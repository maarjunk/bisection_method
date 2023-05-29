"""
in this module we create some math function to
use them in the bisection function
"""
import math


def tabe1(x: float) -> float:
    return x + math.cos(x)


def tabe2(x: float) -> float:
    return math.exp(x) - (3 * (x ** 2))
