#!/usr/bin/env python3
''' A module '''

import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """A coroutine ...."""
    result = [num async for num in async_generator()]
    return result
