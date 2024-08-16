#!/usr/bin/python3
"""
    Here is the module Exo 8
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function """

    def multiply(n: float) -> float:
        """ Here the multiply function """
        return multiplier * n
    return multiply
