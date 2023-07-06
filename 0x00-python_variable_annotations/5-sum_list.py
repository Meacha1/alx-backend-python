#!/usr/bin/env python3
'''A script which takes a list of floats and returns the sum
'''


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of float numbers.

    Args:
        input_list (List[float]): The list of float numbers.

    Returns:
        float: The sum of the float numbers in the list.
    """
    return sum(input_list)
