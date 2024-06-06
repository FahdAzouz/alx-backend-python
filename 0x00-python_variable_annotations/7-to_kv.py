#!/usr/bin/env python3
'''task 7 module
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns tuple of parameters'''
    return (k, float(v**2))
