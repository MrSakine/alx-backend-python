#!/usr/bin/env python3
"""Unittests and Integration Tests"""
import unittest
from unittest.mock import (
    patch,
    PropertyMock,
    Mock
)
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient class definition """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org: str, mock_get_json: Mock):
        """ Test `org` method """
        url = GithubOrgClient.ORG_URL.format(org=org)
        test_payload = {"url": url}
        mock_get_json.return_value = test_payload
        client = GithubOrgClient(org_name=org)
        result = client.org
        self.assertEqual(result, test_payload)
        mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """ Test `_public_repos_url` method """
        org = "google"
        test_payload = {
            "repos_url": f"https://api.github.com/orgs/{org}/repos"
        }
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock
        ) as mock:
            mock.return_value = test_payload
            client = GithubOrgClient(org_name=org)
            result = client._public_repos_url
            self.assertEqual(result, test_payload["repos_url"])
            mock.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: Mock):
        """ Test `public_repos` method """
        test_payload = [
            {
                "name": "Google",
                "license": None
            },
            {
                "name": "Facebook",
                "license": {
                    "key": "private"
                }
            }
        ]
        mock_get_json.return_value = test_payload
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock
        ) as mock:
            org = "google"
            mock.return_value = f"https://api.github.com/orgs/{org}/repos"
            client = GithubOrgClient(org_name=f"{org}")
            result = client.public_repos()
            self.assertEqual(result, ["Google", "Facebook"])
            mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org}/repos"
            )
            mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, key: str, excepted: bool) -> None:
        """ Test `has_license` method """
        has_license = GithubOrgClient.has_license(repo, key)
        self.assertEqual(has_license, excepted)
