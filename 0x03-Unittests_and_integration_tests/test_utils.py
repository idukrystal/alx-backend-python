#!/usr/bin/env python3
""" Module to test Utils Module """

from parameterized import parameterized
from unittest import TestCase
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """ To test utills.access_nested_map methos """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ function to test access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)
