from typing import List, Callable

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


def rows_almost_equals(row_1: np.ndarray, row_2: np.ndarray) -> bool:
    if np.sum(abs(row_1 - row_2)) == 1:
        return True
    else:
        return False


def find_and_fix_possible_lines_of_reflection_2(rows: np.ndarray) -> List[int]:
    """
    Finds all possible lines of reflection in rows. A possible line of
    reflection is the index of the row so that the next row is equal to
    it
    """
    lines = []
    for row_n in range(len(rows) - 1):
        row_up = rows[row_n]
        row_down = rows[row_n + 1]
        if rows_almost_equals(row_up, row_down):
            # fix the line with the smudge
            for col_n, (el_1, el_2) in enumerate(zip(row_up, row_down)):
                if el_1 != el_2:
                    rows[row_n][col_n] = el_2

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


def find_horizontally(rows: np.ndarray, find_lines_function: Callable):
    possible_lines_of_reflection = find_lines_function(rows)
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
        h = find_horizontally(rows, find_possible_lines_of_reflection)

        # Look for the vertical lines of reflection by transposing the
        # rows
        v = find_horizontally(rows.T, find_possible_lines_of_reflection)

        sum += (v + 1) + 100 * (h + 1)
    return sum

def puzzle_2_solution(input_str):
    patterns = input_str.split('\n\n')
    sum = 0
    for pattern in patterns:
        new_pattern = pattern.replace('#', '1').replace('.', '2')
        rows = np.array([list(i) for i in new_pattern.split('\n')]).astype(int)

        # Look for the horizontal lines of reflection
        h = find_horizontally(rows, find_and_fix_possible_lines_of_reflection_2)

        # Look for the vertical lines of reflection by transposing the
        # rows
        v = find_horizontally(rows.T, find_and_fix_possible_lines_of_reflection_2)

        sum += (v + 1) + 100 * (h + 1)
    return sum


if __name__ == '__main__':
    # print(puzzle_1_solution(day_13_example))
    # print(puzzle_1_solution(day_13_input))
    print(puzzle_2_solution(day_13_example))
    # print(puzzle_2_solution(day_13_input))
