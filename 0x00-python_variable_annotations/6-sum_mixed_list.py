#!/usr/bin/env python3
'''A script which takes a mixed list and returns the sum as a float
'''


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''Returns the sum of a list of integers and floats
        Args:
            mxd_list: a list of integers and floats
        Returns:
            the sum of the list as a float
    '''
    return sum(mxd_list)
