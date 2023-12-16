from typing import List

import numpy as np

from AdventOfCode2023.inputs.day_11_input import day_11_example, day_11_input

MULTIPLIER = 1000000 - 1


def find_galaxies_coordinates(rows):
    coordinates = []
    for row_n, row in enumerate(rows):
        for col_n, el in enumerate(row):
            if el == '#':
                coordinates.append((row_n, col_n))
    return coordinates


def expand_universe_rows(universe):
    new_universe = []
    for row in universe:
        # If the row only contains '.', then should be expanded
        unique_row_elements = np.unique(row)

        # If the row needs to be expanded, add it to
        if (len(unique_row_elements) == 1) & (unique_row_elements[0] == '.'):
            new_universe.append(row)

        # If the row should not be expanded, just add it
        new_universe.append(row)
    return np.array(new_universe)


def find_empty_rows(universe) -> np.ndarray:
    empty_rows = []
    for row_n, row in enumerate(universe):
        # If the row only contains '.', then should be expanded
        unique_row_elements = np.unique(row)

        # If the row needs to be expanded, add its number to the list
        if (len(unique_row_elements) == 1) & (unique_row_elements[0] == '.'):
            empty_rows.append(row_n)

    return np.array(empty_rows)


def expand_universe(rows):
    universe = np.array([list(i) for i in rows])
    new_universe = expand_universe_rows(universe)

    # To expand the columns, use the same function but with a transposed
    # matrix
    new_universe = expand_universe_rows(new_universe.T)

    # Transpose the matrix back
    return new_universe.T


def find_min_distance(coords_el_1, coords_el_2):
    row_1, col_1 = coords_el_1
    row_2, col_2 = coords_el_2
    return abs(row_1 - row_2) + abs(col_1 - col_2)


def puzzle_1_solution(input_str):
    sum = 0
    rows = input_str.split('\n')
    expanded_universe = expand_universe(rows)
    coordinates = find_galaxies_coordinates(expanded_universe)
    for idx, coords_el_1 in enumerate(coordinates):
        for coords_el_2 in coordinates[idx + 1:]:
            sum += find_min_distance(coords_el_1, coords_el_2)

    return sum


def find_min_distance_2(coords_el_1, coords_el_2, empty_rows: np.ndarray,
                        empty_columns: np.ndarray):
    row_1, col_1 = coords_el_1
    row_2, col_2 = coords_el_2
    distance_without_expansion = find_min_distance(coords_el_1, coords_el_2)
    empty_rows_in_between = empty_rows[
        (empty_rows >= min(row_1, row_2)) & (empty_rows <= max(row_1, row_2))]
    empty_cols_in_between = empty_columns[
        (empty_columns >= min(col_1, col_2)) & (
                    empty_columns <= max(col_1, col_2))]

    return distance_without_expansion + MULTIPLIER * (
                len(empty_cols_in_between) + len(empty_rows_in_between))


def puzzle_2_solution(input_str):
    sum = 0
    rows = input_str.split('\n')
    universe = np.array([list(i) for i in rows])
    coordinates = find_galaxies_coordinates(universe)

    empty_rows = find_empty_rows(universe)
    # To find the columns to be expanded, use the same function but
    # with a transposed matrix
    empty_columns = find_empty_rows(universe.T)

    for idx, coords_el_1 in enumerate(coordinates):
        for coords_el_2 in coordinates[idx + 1:]:
            sum += find_min_distance_2(coords_el_1, coords_el_2, empty_rows,
                                       empty_columns)

    return sum


if __name__ == '__main__':
    # print(puzzle_1_solution(day_11_input))
    print(puzzle_2_solution(day_11_input))
