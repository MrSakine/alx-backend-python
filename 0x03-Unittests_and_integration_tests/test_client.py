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
        mock_get_json.return_value = url
        client = GithubOrgClient(org_name=org)
        result = client.org
        self.assertEqual(result, url)
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
