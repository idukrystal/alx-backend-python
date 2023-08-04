#!/usr/bin/env python3
''' Module to house element_length function '''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Function that performs some mqgic
    '''
    return [(i, len(i)) for i in lst]
