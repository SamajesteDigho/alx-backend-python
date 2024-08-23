#!/usr/bin/env python3
"""
    Here the module description for exo 1
"""
import asyncio
import random
from typing import Any


async def async_generator() -> Any:
    """ Async Geneator co routine """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
