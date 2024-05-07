#!/usr/bin/env python3
"""0-async_generator.py"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    """
    n: int = 10
    sec: int = 1
    for _ in range(n):
        number: float = random.uniform(0, n)
        await asyncio.sleep(sec)
        yield number
