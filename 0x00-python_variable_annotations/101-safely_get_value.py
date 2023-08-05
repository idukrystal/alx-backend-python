#!/usr/bin/env python3
''' A mododule '''
from typing import Any, Mapping, TypeVar, Union


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, type(None)] = None) -> Union[Any, T]:
    ''' A function '''
    if key in dct:
        return dct[key]
    else:
        return default
