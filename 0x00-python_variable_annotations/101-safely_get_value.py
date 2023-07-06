#!/usr/bin/env python3

"""
This module provides a function to safely retrieve a value from a dictionary.
"""

from typing import Any, Dict, Mapping, TypeVar, Union


KT = TypeVar("KT")  # Key Type
VT = TypeVar("VT")  # Value Type

def safely_get_value(dct: Mapping[KT, VT], key: KT, default: Union[VT, None] = None) -> Union[VT, None]:
    """
    Safely retrieves the value associated with the key from the dictionary.

    Args:
        dct (Mapping[KT, VT]): The input dictionary.
        key (KT): The key to retrieve the value for.
        default (Union[VT, None], optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        Union[VT, None]: The value associated with the key, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
