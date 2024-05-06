#!/usr/bin/env python3
"""4-tasks.py"""
import asyncio
import typing

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Spawn task_wait_n n times with the specified max_delay"""
    delays = []
    spawns = []
    for i in range(n):
        task = task_wait_random(max_delay)
        task.add_done_callback(lambda x: delays.append(x.result()))
        spawns.append(task)
    for spawn in spawns:
        await spawn
    return delays
