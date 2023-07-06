#!/usr/bin/env python3

"""
This module provides a function to safely retrieve the first element from a list.
"""

from typing import Any, Optional, Sequence, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Safely retrieves the first element from the input list.

    Args:
        lst (Sequence): The input list.

    Returns:
        Union[Any, None]: The first element of the list, or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
