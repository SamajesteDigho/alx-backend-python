#!/usr/bin/env python3
"""
    The module for Exo 3
"""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int):
    """ Here the Task awaiting """
    return asyncio.Task(wait_random(max_delay))
