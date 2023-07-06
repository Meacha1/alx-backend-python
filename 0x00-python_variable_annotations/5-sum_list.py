#!/usr/bin/env python3
'''A script which takes a list of floats and returns the sum
'''


def sum_list(input_list: list[float]) -> float:
    '''Takes a list of floats and returns the sum
    of all the floats in the list.

    Args:
        input_list (list): a list of floats

    Returns:
        float: the sum of all the floats in the list.
    '''
    sum = 0.0
    for item in input_list:
        sum += item        
