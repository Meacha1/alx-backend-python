#!/usr/bin/env python3

"""
This module provides a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that
        multiplies a float by the multiplier.
    """
    def multiply(num: float) -> float:
        """
        Multiplies a float by the multiplier.

        Args:
            num (float): The float number to be multiplied.

        Returns:
            float: The result of multiplying the float by the multiplier.
        """
        return num * multiplier

    return multiply
