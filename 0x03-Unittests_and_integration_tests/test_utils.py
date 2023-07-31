#!/usr/bin/env python3
"""
Utility functions for working with nested maps and API requests.
"""

from typing import Any, Dict, Tuple, Union
import requests
from functools import wraps

def access_nested_map(nested_map: Dict[str, Any], path: Tuple[str]) -> Union[Dict, Any]:
    """
    Access value in a nested map using a sequence of keys.

    Args:
        nested_map (dict): The nested map (dictionary) to traverse.
        path (tuple): The sequence of keys to access the desired value.

    Returns:
        Union[dict, Any]: The value at the given path in the nested map, or the nested map itself.

    Example:
        >>> access_nested_map({"a": {"b": 2}}, ("a",))
        {"b": 2}

        >>> access_nested_map({"a": {"b": 2}}, ("a", "b"))
        2
    """
    for key in path:
        nested_map = nested_map[key]
    return nested_map

def get_json(url: str) -> Dict[str, Any]:
    """
    Perform an HTTP GET request to fetch JSON data from the given URL.

    Args:
        url (str): The URL to make the GET request.

    Returns:
        Dict[str, Any]: The JSON data retrieved from the URL.

    Example:
        >>> get_json("https://api.github.com/users/octocat")
        {"login": "octocat", "id": 1, ...}
    """
    response = requests.get(url)
    return response.json()

def memoize(func: Any) -> Any:
    """
    Memoization decorator to cache the result of a method.

    Args:
        func (callable): The method to be memoized.

    Returns:
        Any: The cached result of the method.

    Example:
        >>> class TestClass:
        ...     @memoize
        ...     def expensive_operation(self, x):
        ...         print("Doing expensive operation...")
        ...         return x * x
        ...
        >>> test_object = TestClass()
        >>> result1 = test_object.expensive_operation(5)  # This will do the expensive operation
        >>> result2 = test_object.expensive_operation(5)  # This will use the memoized result
        >>> print(result1)
        25
        >>> print(result2)
        25
    """
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper
