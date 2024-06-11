#!/usr/bin/env python3
'''Task 0's module'''
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''loops ten times then yield a random number'''
    for _ in range(10):
        asyncio.sleep(1)
        yield random.random() * 10
