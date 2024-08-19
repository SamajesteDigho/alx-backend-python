#!/usr/bin/env python3
"""
    The module for Exo 0
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Async Max delay """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
