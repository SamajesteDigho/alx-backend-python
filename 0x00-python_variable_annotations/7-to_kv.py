#!/usr/bin/python3
"""
    Here is the module Exo 7
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Return key-value tuple """
    return (k, v * v)
