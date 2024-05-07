#!/usr/bin/env python3
"""0-async_generator.py"""
import asyncio
import random


async def async_generator() -> None:
    """
    Loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    """
    max_delay: int = 10
    n: int = 9
    sec: int = 1
    for i in range(n):
        number: float = random.uniform(0, max_delay)
        await asyncio.sleep(sec)
        yield number
