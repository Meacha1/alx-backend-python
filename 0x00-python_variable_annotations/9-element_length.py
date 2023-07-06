#!/usr/bin/env python3

"""
This module provides a function to calculate the length of elements in a list.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element of the input list
    along with its length.

    Args:
        lst (Iterable[Sequence]): The input list of elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing each element
        of the input list along with its length.
    """
    return [(i, len(i)) for i in lst]
