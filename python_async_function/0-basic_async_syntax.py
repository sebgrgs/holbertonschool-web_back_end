#!/usr/bin/env python3
"""This module contains a function that waits for a random delay
between 0 and max_delay seconds and returns the delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns a random delay between 0 and max_delay."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
