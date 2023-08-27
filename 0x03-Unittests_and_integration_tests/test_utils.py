#!/usr/bin/env python3
""" Module to test Utils Module """

import requests
from parameterized import parameterized
from unittest import TestCase, mock
from utils import access_nested_map, get_json


class TestAccessNestedMap(TestCase):
    """ To test utills.access_nested_map method """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ function to test access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, msg):
        """ function to test access_nested_map execeptions"""
        with self.assertRaises(KeyError) as except_cm:
            access_nested_map(nested_map, path)
        # self.assertEqual(except_cm.exception.args, (msg,))


class TestGetJson(TestCase):
    """ To test utills.get_json method  """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """ function to test get_json results """
        with mock.patch(
            "requests.get",
            return_value=mock_request_get(payload),
        ) as mock_response:
            self.assertEquals(get_json(url), payload)


def mock_request_get(fake_response):
    """ Reusable Mock fuction to replace requests.get """
    class MockResponse:
        """ Mock Response object """

        def __init__(self, response):
            self.response = response

        def json(self):
            return self.response
    return MockResponse(fake_response)
