#!/usr/bin/env python3
''' Module to house make_multiplier function '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Function that returna a function that can multiply
    a number by float: multiplier
    '''
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
