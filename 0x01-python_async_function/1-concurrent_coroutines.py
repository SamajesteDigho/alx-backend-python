#!/usr/bin/env python3
"""
    The module for Exo 1
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Waiting async routine """
    data = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(data)
