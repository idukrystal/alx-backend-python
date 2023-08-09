#!/usr/bin/env python3
''' This is a module'''

import asyncio
import random


async def async_generator() -> type(None):
    """ A coroutine that yields """
    for _ in range(10):
        await asyncio.sleep(1)
        res: float = random.uniform(0, 10)
        yield res
