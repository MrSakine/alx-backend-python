#!/usr/bin/env python3
"""1-concurrent_coroutines.py"""
import asyncio
import typing

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Spawn wait_random n times with the specified max_delay"""
    delays = []
    spawns = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        task.add_done_callback(lambda x: delays.append(x.result()))
        spawns.append(task)
    for spawn in spawns:
        await spawn
    return delays
