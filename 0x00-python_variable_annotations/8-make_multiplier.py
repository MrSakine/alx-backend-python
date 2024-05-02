#!/usr/bin/env python3
"""Complex types - functions"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    return (lambda x: x * multiplier)
