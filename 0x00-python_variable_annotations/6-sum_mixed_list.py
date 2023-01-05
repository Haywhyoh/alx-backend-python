#!/usr/bin/env python3
""" Basic annotations - sum_mixed_list """
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ a type-annotated function sum_mixed_list which takes
    a list mxd_lst of integers and floats and returns
    their sum as a float. """
    total = 0
    for i in mxd_list:
        total = total + i
    return total
