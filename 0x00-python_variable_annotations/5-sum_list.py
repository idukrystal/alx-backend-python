#!/usr/bin/env python3
''' A module to housecthe sum_list function
'''


def sum_list(input_list: list[float]) -> float:
    ''' Sums up all the values in
    list of floats and return sum
    '''
    total = 0.0
    for n in input_list:
        total += n
    return total
