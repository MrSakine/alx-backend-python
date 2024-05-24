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
    get_json,
    memoize
)
from typing import (
    Dict,
    Tuple,
    Union,
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
    @patch("utils.requests.get")
    def test_get_json(
        self,
        url: str,
        payload: Dict[str, Any],
        mock: Mock
    ) -> None:
        """ Test `get_json` method """
        mock_response = Mock()
        mock_response.json.return_value = payload
        mock.return_value = mock_response
        self.assertEqual(get_json(url=url), payload)
        mock.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """ TestMemoize class definition """

    def test_memoize(self):
        """ Test `memoize` method"""
        class TestClass:
            """ TestClass definition """

            def a_method(self):
                """ Definition of `a_method` """
                return 42

            @memoize
            def a_property(self):
                """ Call `a_method` """
                return self.a_method()

        with patch.object(
            TestClass,
            "a_method",
            return_value=42
        ) as mock_method:
            instance = TestClass()
            r1, r2 = [instance.a_property, instance.a_property]
            self.assertEqual(r1, 42)
            self.assertEqual(r2, 42)
            mock_method.assert_called_once()
