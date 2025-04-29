#!/usr/bin/env python3
"""Async generator that yields a random number every second."""
import random
import asyncio
import typing

async def async_generator() -> typing.Generator[float, None, None]:
    """Yields a random number between 0 and 10 every second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
