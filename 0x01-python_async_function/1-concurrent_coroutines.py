#!/usr/bin/env python3
"""1-concurrent_coroutines.py"""
import typing

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Spawn wait_random n times with the specified max_delay"""
    data: list[float] = []
    for i in range(n):
        res: float = await wait_random(max_delay)
        data.append(res)
    return data
