#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
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
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test the get_json function with mocked HTTP calls.

        Args:
            test_url (str): The URL to be used in the test.
            test_payload (dict): The expected payload to be returned.
            mock_get (MagicMock): The mocked get method from requests module.

        Returns:
            None
        """
        mock_get.return_value = Mock()
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

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """
        Test the memoize decorator.

        Args:
            mock_a_method (MagicMock): The mocked a_method.

        Returns:
            None
        """
        instance = TestClass()
        mock_a_method.return_value = 42

        result1 = instance.a_property
        result2 = instance.a_property

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
        mock_a_method.assert_called_once()

if __name__ == "__main__":
    unittest.main()
