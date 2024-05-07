#!/usr/bin/env python3
"""1-async_comprehension.py"""
import typing

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> typing.List[float]:
    """Async Comprehensions"""
    return [i async for i in async_generator()]
