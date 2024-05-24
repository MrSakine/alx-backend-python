#!/usr/bin/env python3
"""Unittests and Integration Tests"""
import unittest
from unittest.mock import (
    patch,
    Mock
)
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json
)
from typing import (
    Dict,
    Tuple,
    Union,
    List,
    Any
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

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url: str, payload: Dict[str, Any]) -> None:
        """ Test `get_json` method """
        attrs = {"json.return_value": payload}
        mock = Mock(**attrs)
        with patch("utils.requests.get", return_value=mock) as req:
            self.assertEqual(get_json(url), payload)
            req.assert_called_once_with(url)
