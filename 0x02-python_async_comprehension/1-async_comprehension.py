#!/usr/bin/env python3
"""1-async_comprehension.py"""
import typing


async def async_comprehension() -> typing.List[float]:
    """Async Comprehensions"""
    return [i async for i in async_generator()]
