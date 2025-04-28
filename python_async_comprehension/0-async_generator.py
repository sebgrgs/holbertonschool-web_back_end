#!/usr/bin/env python3
"""Async generator that yields a random number every second."""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yields a random number between 0 and 10 every second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
