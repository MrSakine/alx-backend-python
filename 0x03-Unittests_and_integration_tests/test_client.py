#!/usr/bin/env python3
"""Unittests and Integration Tests"""
import unittest
from unittest.mock import (
    patch,
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
