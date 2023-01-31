#!/usr/bin/env python3
""" Basic annotations - to_kv """
from typing import Tuple, Union


def element_length(lst):
    return [(i, len(i)) for i in lst]