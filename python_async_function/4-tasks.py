#!/usr/bin/env python3
"""Module that contains a function to spawn tasks."""

import asyncio
from typing import List
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of delays in ascending order."""
    delay = []
    for i in range(n):
        delay.append(task_wait_random(max_delay))
    delays = await asyncio.gather(*delay)
    return sorted(delays)
