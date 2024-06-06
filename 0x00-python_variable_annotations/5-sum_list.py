#!/usr/bin/env python3
'''Task 5'module '''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''return the sum of floats'''
    sum = 0
    for num in input_list:
        sum += num
    return sum
