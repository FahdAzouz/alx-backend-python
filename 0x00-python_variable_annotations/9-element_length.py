#!/usr/bin/env python3
'''Task 9 module '''
from typing import Tuple, List, Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Something something something'''
    return [(i, len(i)) for i in lst]
