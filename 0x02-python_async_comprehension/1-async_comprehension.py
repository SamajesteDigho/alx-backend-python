#!/usr/bin/env python3
"""
    Here the module description for exo 1
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async Comprehension coroutine """
    return [x async for x in async_generator()]
