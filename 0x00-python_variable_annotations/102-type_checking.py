#!/usr/bin/env python3

"""
This module provides a function to zoom in an array.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in an array by repeating each element by the given factor.

    Args:
        lst (Tuple): The input tuple.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List: The zoomed-in list.
    """
    zoomed_in = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
