#!/usr/bin/env python3
'''Task 0 module'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''wait randomly between zero and passed number'''
    wait_time = random.uniform(0.0, float(max_delay))
    await asyncio.sleep(wait_time)
    return wait_time
