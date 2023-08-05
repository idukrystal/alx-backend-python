#!/usr/bin/env python3
''' A module '''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    ''' A function '''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
