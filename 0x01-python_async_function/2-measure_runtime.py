#!/usr/bin/env python3
'''Task 2 module'''
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''return average time'''
    cur_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return ((time.time() - cur_time) / n)
