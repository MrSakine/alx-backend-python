#!/usr/bin/env python3
"""101-safely_get_value.py"""
import typing

T = typing.TypeVar("T")


def safely_get_value(
    dct: typing.Mapping, key: typing.Any, default: typing.Union[T, None] = None
) -> typing.Union[typing.Any, T]:
    """More involved type annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
