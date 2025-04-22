#!/usr/bin/env python3
"""
This module contains a function that takes a float n as an argument
and returns a function that multiplies a number by n.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a number by the given multiplier.
    """
    def make_multiplier2(x: float) -> float:
        return x * multiplier
    return make_multiplier2
