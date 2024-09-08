#!/usr/bin/env python3
"""
Here some documentation comments for the module
"""
from typing import Any, Mapping, Sequence
import unittest.mock
from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Test Access Nested Map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected: Any):
        """ Testing of the access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence):
        """ Checking Exception cases """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test Get JSOn from the utils module """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        # ("http://holberton.io", {"payload": False})
    ])
    @unittest.mock.patch('requests.get')
    def test_get_json(self, url: str, payload: Mapping, mocked_data):
        """ Here we get the testing json """
        mock_response = unittest.mock.MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = payload
        mocked_data.return_value = mock_response
        self.assertIsInstance(mocked_data, unittest.mock.MagicMock)

        response = get_json(url)
        self.assertEqual(response, payload)


class TestMemoize(unittest.TestCase):
    """ Defining the test function for testMemorize """
    def test_memoize(self):
        """ Here the testing function for test memorize """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()


if __name__ == "__main__":
    unittest.main()
