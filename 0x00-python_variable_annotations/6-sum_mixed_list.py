#!/usr/bin/env python3
'''Task 6'module '''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''return the sum of floats'''
    return float(sum(mxd_lst))