#!/usr/bin/env python3
"""
    Here is the module Exo 9
"""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Defining the type annotations """
    return [(i, len(i)) for i in lst]
