#!/usr/bin/env python3
''' A module '''

from asyncio import gather
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    ''' A function '''
    start: float = time.perf_counter()
    await gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
