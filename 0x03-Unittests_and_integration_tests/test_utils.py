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
    def test_access_nested_map(self, nested_map, path, expected_result):
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
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that KeyError is raised for specific inputs.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The path to the desired value in the nested dictionary.

        Returns:
            None
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        expected_error_msg = 'Key not found: "{}"'.format(path[-1])
        self.assertEqual(str(context.exception), expected_error_msg)

if __name__ == "__main__":
    unittest.main()
