#!/usr/bin/env python3
"""This module contains a function that takes a list of floats as an argument
and returns the sum of the list as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of the list as a float."""
    return sum(input_list)
