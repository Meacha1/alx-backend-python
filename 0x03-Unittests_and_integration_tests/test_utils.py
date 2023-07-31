#!/usr/bin/env python3

"""
This module contains unit tests for the utils.access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple, expected_result):
        """
        Test the access_nested_map function for various inputs.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The path to the desired value in the nested dictionary.
            expected_result: The expected result when accessing the nested dictionary.

        Returns:
            None
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: dict, path: tuple, exception_type):
        """
        Test that the access_nested_map function raises KeyError for specific inputs.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The path to the desired value in the nested dictionary.
            exception_type (Exception): The expected exception type.

        Returns:
            None
        """
        with self.assertRaises(exception_type) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), f"Key not found: {path[-1]}")

if __name__ == "__main__":
    unittest.main()
