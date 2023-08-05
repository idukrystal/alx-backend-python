#!/usr/bin/env python3
''' Module to house safe_first_element function '''
from typing import Any, NoneType, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, type(None)]:
    ''' Mors Megic, i didnt write it '''
    if lst:
        return lst[0]
    else:
        return None
