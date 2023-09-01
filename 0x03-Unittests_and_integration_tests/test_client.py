#!/usr/bin/env python3
""" Module to unittest the client module """

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


def fake_get_json(url) -> Dict:
    """ Replaces get_json """
    return {"url": url}


class TestGithubOrgClient(unittest.TestCase):
    """ Test Class for Client Classs """

    @parameterized.expand([
        ("google", {"url": "https://api.github.com/orgs/google"}),
        ("abc", {"url": "https://api.github.com/orgs/abc"})
    ])
    @unittest.mock.patch("client.get_json", new=fake_get_json)
    def test_org(self, org_name: str, exp: Dict) -> None:
        """ Tests the org function of githubclient class """
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, exp)
