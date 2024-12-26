from collections import defaultdict

import numpy as np

from advent_of_code_2024.inputs.day_1 import puzzle_1_input


def part_1(input_str):
    rows = input_str.split('\n')
    first_col = []
    second_col = []
    for row in rows:
        first, second = row.split('   ')
        first_col.append(int(first))
        second_col.append(int(second))

    differences = np.array(sorted(first_col)) - np.array(sorted(second_col))
    solution = sum(np.abs(differences))
    return solution


def part_2(input_str):
    rows = input_str.split('\n')
    value_counts = defaultdict(int)
    left_numbers = []
    for row in rows:
        left, right = row.split('   ')
        left_numbers.append(int(left))
        value_counts[int(right)] += 1

    total = 0
    for number in left_numbers:
        total += number * value_counts.get(number, 0)

    return total


if __name__ == '__main__':
    print(part_1(puzzle_1_input))
    print(part_2(puzzle_1_input))
