"""Module for solving day 1 of Advent of Code 2022.
https://adventofcode.com/2022/day/1
"""

from os import path
from pprint import pprint as pprint


def find_location():
    """Find the absolute location of this module.
    Args:
        None
    Returns:
        None
    """
    here = path.abspath(path.dirname(__file__))
    return here


def read_file(file):
    """Reads the assignment input file from disk.
    Args:
        file (str): File name to open.
    Returns:
        correction_values (list): List of the values
    """
    with open(file, "r") as fh:
        values = []
        # Don't use readlines() because it keeps the newline
        for value in fh.read().splitlines():
            values.append(value)

    return values


def split_into_elfs(values):
    calorie_data = dict()
    calorie_list = list()
    elf_number = 1
    # Creat Elfs
    for value in values:
        if value != "":
            calorie_data.setdefault(f"elf{elf_number}", {"items": [], "total": 0})
            if value not in calorie_data[f"elf{elf_number}"]:
                calorie_data[f"elf{elf_number}"]["items"].append(value)
        elif value == "":
            elf_number += 1

    return calorie_data


def sum_calories(calorie_data):
    for key, value in calorie_data.items():
        for calorie_value in value["items"]:
            value["total"] += int(calorie_value)


def solve_part_1(calorie_data):
    solution = max(int(d["total"]) for d in calorie_data.values())
    return solution


def grab_totals_only(calorie_data):
    elf_totals = dict()
    for elf, pouch in calorie_data.items():
        elf_totals[elf] = pouch["total"]

    return elf_totals


def solve_part_2(elf_totals, top_quantity: int = 3):
    solution_list = sorted(elf_totals.values())[-top_quantity:]
    solution = sum(solution_list)
    return solution


def main():
    """Main function for solving Part 1 and Part 2 of AoC day 1"""
    input_file = "input.txt"
    top_quantity = 3

    inputs_path = f"{find_location()}/{input_file}"
    values = read_file(inputs_path)
    calorie_data = split_into_elfs(values)
    sum_calories(calorie_data)
    part1_solution = solve_part_1(calorie_data)
    print(part1_solution)
    part2_solution = solve_part_2(grab_totals_only(calorie_data), top_quantity)
    print(part2_solution)


if __name__ == "__main__":
    main()
