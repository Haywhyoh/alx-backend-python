#!/usr/bin/env python3
""" Basic annotations - sum_list """
from typing import List



def sum_list(input_list: List[float]) -> float:
    """ a type-annotated function sum_list which takes
    a list input_list of floats as argument and returns
    their sum as a float. """
    total = 0
    for i in input_list:
        total = total + i
    return total
