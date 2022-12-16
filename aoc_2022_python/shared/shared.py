"""Shared Code for solving Advent of Code 2022.
https://adventofcode.com/2022
"""
from typing import List


def read_file(file: str) -> List[str]:
    """Reads the assignment input file from disk.
    Args:
        file (str): File name to open.
    Returns:
        values (list): List of the values
    """
    with open(file, "r", encoding="utf-8") as file_handle:
        values = []
        # Don't use readlines() because it keeps the newline
        for value in file_handle.read().splitlines():
            values.append(value)

    return values
