#!/usr/bin/env python3

"""
This module contains unit tests for the utils functions.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize

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
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: dict, path: tuple):
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

class TestGetJson(unittest.TestCase):
    """
    Test class for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str, test_payload: dict, mock_get):
        """
        Test the get_json function with mocked HTTP calls.

        Args:
            test_url (str): The URL to be used for testing.
            test_payload (dict): The expected JSON payload.
            mock_get: The mocked requests.get function.

        Returns:
            None
        """
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)

class TestMemoize(unittest.TestCase):
    """
    Test class for the memoize decorator.
    """

    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        """
        Test that the memoize decorator caches the result.

        Returns:
            None
        """
        test_instance = self.TestClass()
        with patch.object(test_instance, 'a_method') as mock_method:
            result_1 = test_instance.a_property
            result_2 = test_instance.a_property

            self.assertEqual(result_1, 42)
            self.assertEqual(result_1, result_2)
            mock_method.assert_called_once()

if __name__ == "__main__":
    unittest.main()
