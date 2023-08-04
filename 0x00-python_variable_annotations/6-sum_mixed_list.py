#!/usr/bin/env python3
''' A module to housecthe sum_mixed_list function
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Sums up all the values in
    list of floats/integers  and return sum
    '''
    total: float = 0.0
    for n in mxd_lst:
        total += n
    return total
