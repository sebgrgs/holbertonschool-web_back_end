#!/usr/bin/env python3
"""Module with type-annotated function to_kv."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple containing k and the square of v as a float"""
    return (k, float(v ** 2))