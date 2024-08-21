#!/usr/bin/env python3
"""
    Here the module description for exo 1
"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ Async Comprehension coroutine """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
