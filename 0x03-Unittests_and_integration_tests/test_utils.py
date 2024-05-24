#!/usr/bin/env python3
"""Unittests and Integration Tests"""
import unittest
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json
)
from typing import (
    Dict,
    Tuple,
    Union,
    Any
)
from unittest.mock import (
    patch,
    Mock
)


class TestAccessNestedMap(unittest.TestCase):
    """ Class definition """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        map: Dict,
        path: Tuple[str],
        expected: Union[Dict, int]
    ) -> None:
        """ Test `access_nested_map` method """
        self.assertEqual(access_nested_map(map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
        self,
        map: Dict,
        path: Tuple[str]
    ) -> None:
        """ Test `access_nested_map_exception` method """
        with self.assertRaises(KeyError):
            access_nested_map(map, path)


class TestGetJson(unittest.TestCase):
    """ Class definition """

    @patch("requests.get")
    def test_get_json(self, mock: Mock) -> None:
        """ Test `get_json` method """
        test_cases = [
            {
                "test_url": "http://example.com",
                "test_payload": {"payload": True}
            },
            {
                "test_url": "http://holberton.io",
                "test_payload": {"payload": False}
            }
        ]
        for case in test_cases:
            test_url: str = case["test_url"]
            test_payload: Dict[str, Any] = case["test_payload"]
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock.return_value = mock_response
            result: Dict[str, Any] = get_json(test_url)
            mock.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)
            mock.reset_mock()
