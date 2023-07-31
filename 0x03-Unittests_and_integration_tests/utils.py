#!/usr/bin/env python3
"""Unit tests for utils.py"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

class TestUtils(unittest.TestCase):
    """Test cases for utils.py"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json function"""
        mock_response = mock_get.return_value
        mock_response.json.return_value = test_payload

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

    class TestClass:
        """Test class for memoize decorator"""

        def a_method(self):
            """Test method for memoize decorator"""
            return 42

        @memoize
        def a_property(self):
            """Test property for memoize decorator"""
            return self.a_method()

    def test_memoize(self):
        """Test memoize decorator"""
        my_object = self.TestClass()

        with patch.object(my_object, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42

            result1 = my_object.a_property
            result2 = my_object.a_property

            mock_a_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

if __name__ == "__main__":
    unittest.main()
