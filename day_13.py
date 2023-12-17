from typing import List

import numpy as np

from AdventOfCode2023.inputs.day_13_input import day_13_example, day_13_input


def rows_equals(row_1: np.ndarray, row_2: np.ndarray) -> bool:
    """
    Returns True if row_1 is equal to row_2
    """
    try:
        np.testing.assert_array_equal(row_1, row_2)
        return True
    except AssertionError:
        return False


def find_possible_lines_of_reflection(rows: np.ndarray) -> List[int]:
    """
    Finds all possible lines of reflection in rows. A possible line of
    reflection is the index of the row so that the next row is equal to
    it
    """
    lines = []
    for row_n in range(len(rows) - 1):
        if rows_equals(rows[row_n], rows[row_n + 1]):
            lines.append(row_n)
    return lines


def verify_reflection(rows, row_n):
    """
    Verifies is the reflection on a given line of reflection is correct
    by comparing all the rows before and after the line
    """
    rows_before_reflection_line = list(reversed(rows[0: row_n + 1]))
    rows_after_reflection_line = (rows[row_n + 1: len(rows)])
    # Minimum number of rows that should coincide
    threshold = min(len(rows_before_reflection_line),
                    len(rows_after_reflection_line))
    n_reflection = 0
    for row_up, row_down in zip(rows_before_reflection_line,
                                rows_after_reflection_line):
        if rows_equals(row_up, row_down):
            n_reflection += 1

    if n_reflection == threshold:
        return True
    return False


def find_horizontally(rows: np.ndarray):
    possible_lines_of_reflection = find_possible_lines_of_reflection(rows)
    for possible_line in possible_lines_of_reflection:
        if verify_reflection(rows, possible_line):
            return possible_line
    return -1


def puzzle_1_solution(input_str):
    patterns = input_str.split('\n\n')
    sum = 0
    for pattern in patterns:
        rows = np.array([list(i) for i in pattern.split('\n')])

        # Look for the horizontal lines of reflection
        h = find_horizontally(rows)

        # Look for the vertical lines of reflection by transposing the
        # rows
        v = find_horizontally(rows.T)

        sum += (v + 1) + 100 * (h + 1)
    return sum


if __name__ == '__main__':
    print(puzzle_1_solution(day_13_example))
    print(puzzle_1_solution(day_13_input))
