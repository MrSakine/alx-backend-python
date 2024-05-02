#!/usr/bin/env python3
"""102-type_checking.py"""
import typing


def zoom_array(
        lst: typing.Sequence[typing.Any],
        factor: typing.Any = 2
        ) -> typing.List:
    """Type Checking"""
    zoomed_in: typing.List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = [12, 72, 91]
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3.0)
