#!/usr/bin/env python3

"""
This module provides a function to safely retrieve the first element from a list.
"""

from typing import Any, List, Optional

def safe_first_element(lst: List[Any]) -> Optional[Any]:
    """
    Safely retrieves the first element from the input list.

    Args:
        lst (List[Any]): The input list.

    Returns:
        Optional[Any]: The first element of the list, or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

