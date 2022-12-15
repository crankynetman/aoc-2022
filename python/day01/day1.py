"""Module for solving day 1 of Advent of Code 2022.
https://adventofcode.com/2022/day/1
"""

from os import path
from typing import Any, List, Dict, Union

INPUT_FILE = "input.txt"  # Default input file name


def find_location() -> str:
    """Find the absolute location of this module.
    Args:
        None
    Returns:
        here (str): The absolute path of this python script
    """
    here = path.abspath(path.dirname(__file__))
    return here


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


def sum_calories(calorie_data: Dict[str, Dict[str, Any]]) -> None:
    """Takes the calorie data Dict and modifies it to add up all of the
    per-elf calorie values

    Args:
        calorie_data (dict): Dictionary of the elves and their pouch contents
    Returns:
        None
    """
    for value in calorie_data.items():
        for calorie_value in value[1]["items"]:
            value[1]["total"] += int(calorie_value)


def split_into_elfs(values: List[str]) -> Dict[str, Dict[str, Union[List[int], int]]]:
    """Takes the file values and spits out a dict of dicts containing the
    elfs and their contents, like so:

    {
        "elf1": {
            "items": [
                "2027",
                "1671",
            ],
            "total": 3698,
        },
        "elf10": {
            "items": [
                "6000",
                "7000",
                "5000",

            ],
            "total": 18000,
        },
    }

    Args:
        values (list): List of the values given by AoC
    Returns:
        calorie_data (dict): Dictionary of the elves and their pouch contents
    """
    calorie_data: Dict[str, Dict[str, Any]] = {}
    elf_number: int = 1
    # Creat Elfs
    for value in values:
        if value != "":
            calorie_data.setdefault(f"elf{elf_number}", {"items": [], "total": 0})
            if value not in calorie_data[f"elf{elf_number}"]:
                calorie_data[f"elf{elf_number}"]["items"].append(value)
        elif value == "":
            elf_number += 1

    sum_calories(calorie_data)
    return calorie_data


def solve_part_1(calorie_data: Dict[str, Dict[str, Any]]) -> int:
    """Takes the calorie data Dict and finds the elf with the largest amount
    of calories in their pouch.

    Args:
        calorie_data (dict): Dictionary of the elves and their pouch contents
    Returns:
        solution (int): Highest number of calories in any elf's pouch
    """
    solution = max(int(d["total"]) for d in calorie_data.values())
    return solution


def grab_totals_only(calorie_data: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    """Takes the calorie data Dict and returns a new dict with just the totals
    for easier processing later. Example dict:
    {
        "elf1": 5000,
        "elf2": 10231,
    }

    Args:
        calorie_data (dict): Dictionary of the elves and their pouch contents
    Returns:
        elf_totals (dict): Simplified dict where the key is the elf name, the
        value is the total calories they have.
    """
    elf_totals: Dict[str, int] = {}
    for elf, pouch in calorie_data.items():
        elf_totals[elf] = pouch["total"]

    return elf_totals


def solve_part_2(elf_totals: Dict[str, int], top_quantity: int = 3) -> int:
    """Takes the elf_totals Dict and finds the top N number of elves (by
    total calories). Then it adds up how many calories those elves have.

    Args:
        elf_totals (dict): Simplified dict where the key is the elf name, the
        value is the total calories they have.
        top_quantity (int): The top number of elves to add up.
    Returns:
        solution (int): The sum of how many calories the top N elves have.
    """
    solution_list = sorted(elf_totals.values())[-top_quantity:]
    solution = int(sum(solution_list))
    return solution


def main() -> None:
    """Main function for solving Part 1 and Part 2 of AoC day 1"""

    # Construct the full path to the input file
    inputs_path = f"{find_location()}/{INPUT_FILE}"
    # Read the values from the input file
    values = read_file(inputs_path)
    # Structure the data
    calorie_data = split_into_elfs(values)
    # Solve for Part 1
    part1_solution = solve_part_1(calorie_data)
    print(part1_solution)
    # Solve for Part 2
    part2_solution = solve_part_2(grab_totals_only(calorie_data))
    print(part2_solution)


if __name__ == "__main__":
    main()
