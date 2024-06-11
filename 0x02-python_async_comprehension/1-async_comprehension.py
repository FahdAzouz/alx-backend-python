#!/usr/bin/env python3
'''Task 1 module'''
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    '''collect 10 numbers and return them'''
    result = [i async for i in async_generator()]
    return result
