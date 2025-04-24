#!/usr/bin/env python3
"""Returns a list of delays in ascending order."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of delays in ascending order."""
    delay = []
    for i in range(n):
        delay.append(wait_random(max_delay))
    delays = await asyncio.gather(*delay)
    return sorted(delays)
