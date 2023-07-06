#!/usr/bin/env python3

"""
This module provides a function to create a tuple with the string k and
the square of int/float v.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the string k and the square of int/float v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple with the string k and the square of v.
    """
    return k, v ** 2
