#!/usr/bin/env python3
"""Unittests and Integration Tests"""
import unittest
from parameterized import parameterized
from .utils import access_nested_map
from typing import Sequence


class TestAccessNestedMap(unittest.TestCase):
    """ Class definition """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map: Sequence, path: Sequence, result: int):
        """ Test access nested map method"""
        self.assertEqual(access_nested_map(map, path), result)


if __name__ == '__main__':
    unittest.main()
