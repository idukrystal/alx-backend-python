#!/usr/bin/env python3
""" Module to unittest the client module """

import utils
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """ Test Class for Client Classs """

    @parameterized.expand([
        ("google", {"url": "https://api.github.com/orgs/gogle"}),
        ("abc", {"url": "https://api.github.com/orgs/abc"})
    ])
    #@unittest.mock.patch('__main__.utils.get_json')
    def test_org(self, org_name: str, exp: Dict) -> None:
        """ Tests the org function of githubclient class """
        with unittest.mock.patch("utils.get_json") as mock:
            mock.return_value = exp
            client = GithubOrgClient(org_name)
            print(client.org)
        mock.assert_called_once()
unittest.main()
        
