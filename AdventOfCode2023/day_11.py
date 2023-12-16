import numpy as np

from AdventOfCode2023.inputs.day_11_input import day_11_example, day_11_input


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


def expand_universe(rows):
    universe = np.array([list(i) for i in rows])
    new_universe = expand_universe_rows(universe)
    new_universe = expand_universe_rows(new_universe.T)
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


if __name__ == '__main__':
    print(puzzle_1_solution(day_11_input))
