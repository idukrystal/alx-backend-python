#!/usr/bin/env python3
""" Module to test Utils Module """

import requests
from parameterized import parameterized
from unittest import TestCase, mock, main
from utils import access_nested_map, get_json, memoize
from typing import Dict, Tuple, Union


class TestAccessNestedMap(TestCase):
    """ To test utills.access_nested_map method """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        nested_map: Dict,
        path: Tuple[str],
        expected: Union[Dict, int],
    ) -> None:
        """ function to test access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Dict,
        path: Tuple[str],
        msg: str
    ) -> None:
        """ function to test access_nested_map execeptions"""
        with self.assertRaises(KeyError) as except_cm:
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """ To test utills.get_json method  """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(
        self,
        url: str,
        payload: Dict,
    ) -> None:
        """ function to test get_json results """
        with mock.patch(
            "requests.get",
            return_value=mock_request_get(payload),
        ) as mock_response:
            self.assertEquals(get_json(url), payload)


class TestMemoize(TestCase):
    """ to test utills.memoize decorator """

    def test_memoize(self) -> None:
        """ Test the memoise decorators posutively """
        class TestClass:
            """ a test class """
            def a_method(self):
                """ a method """
                return 42

            @memoize
            def a_property(self):
                """ a property """
                return self.a_method()
        with mock.patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
        ) as mock_fn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
        mock_fn.assert_called_once()
