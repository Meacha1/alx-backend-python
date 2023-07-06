#!/usr/bin/env python3
'''A script which takes a list of floats and returns the sum
'''


def sum_list(numbers: float) -> float:
    '''Takes a list of floats and returns the sum
    of all the floats in the list.

    Args:
        numbers (list): a list of floats

    Returns:
        float: the sum of all the floats in the list.
    '''
    sum = 0.0
    for number in numbers:
        sum += number
    return sum
