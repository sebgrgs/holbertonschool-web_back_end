#!/usr/bin/env python3
"""Measure the runtime of async_comprehension."""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of async_comprehension."""
    task = []
    start_time = time.time()
    for _ in range(4):
        task.append(asyncio.create_task(async_comprehension()))

    await asyncio.gather(*task
    )
    end_time = time.time()
    return end_time - start_time
