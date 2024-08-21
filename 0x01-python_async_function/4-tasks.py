#!/usr/bin/env python3
"""
    The module for Exo 4
"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Waiting async routine """
    return [await task_wait_random(max_delay) for _ in range(n)]
