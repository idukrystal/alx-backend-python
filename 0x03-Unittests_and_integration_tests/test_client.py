#!/usr/bin/env python3
""" Module to unittest the client module """

import unittest
from unittest.mock import patch, MagicMock, PropertyMock
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

    @parameterized.expand([({"repos_url": "mock.com"}, "mock.com")])
    def test_public_repos_url(self, org_value: Dict, expected: str) -> None:
        """ Test a particular function """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock
        ) as mock:
            mock.return_value = org_value
            client = GithubOrgClient("")
            self.assertEquals(client._public_repos_url, expected)
        mock.assert_called_once_with()

    @parameterized.expand([("mock.com",)], skip_on_empty=True)
    @patch("client.get_json")
    def test_public_repos(
            self, fake_repo_url: str, mock_json: MagicMock
    ) -> None:
        """ tests a fuction """
        mock_json.return_value = [
            {
                "name": "mock",
                "license": {
                    "key": "secret_key"
                }
            },
            {
                "name": "mock2",
                "license": {
                    "key": "a_diffrent_key"
                }
            }
        ]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                return_value=fake_repo_url
        ) as mock:
            client = GithubOrgClient("")
            self.assertEqual(
                client.public_repos(license="secret_key"),
                ["mock",]
            )
        mock.assert_called_once()
        mock_json.assert_called_once()
