#!/usr/bin/python3
"""
    Here is the module Exo 100
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Saving the first element """
    if lst:
        return lst[0]
    else:
        return None
