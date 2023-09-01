#!/usr/bin/env python3
""" Module to unittest the client module """

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """ Test Class for Client Classs """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, exp: Dict, mock: MagicMock) -> None:
        """ Tests the org function of githubclient class """
        mock.return_value = exp
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, exp)
        mock.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
