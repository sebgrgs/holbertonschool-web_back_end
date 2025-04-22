#!/usr/bin/env python3
"""This module contains element_length function that takes a list of sequences
and returns a list of tuples containing the sequence and its length.
"""
from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
