#!/usr/bin/env python3
'''task 7 module
'''
from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, int | float]:
    return (k, float(v**2))
