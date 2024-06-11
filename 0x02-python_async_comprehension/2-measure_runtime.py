#!/usr/bin/env python3
'''Task 2 module'''
import asyncio
from typing import List
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''collect 10 numbers and return them'''
    cur = time.time()
    await asyncio.gather(
        async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension()
    )
    return (time.time() - cur)
