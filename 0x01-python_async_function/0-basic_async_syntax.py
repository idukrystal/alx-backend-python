#!/usr/bin/env python3
''' A Module '''

import asyncio
from random import uniform


async def wait_random(max_delay=10):
    ''' A corotine function example '''
    delay_time = uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
