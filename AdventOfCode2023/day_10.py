from enum import Enum
from typing import Tuple, Optional

from AdventOfCode2023.inputs.day_10_input import day_10_example_1, \
    day_10_example_2


class Direction(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    DOWN = 'down'
    UP = 'up'




def validate_new_coords(new_row, new_col, rows):
    if (
            (new_row < 0) |
            (new_col < 0) |
            (new_row >= len(rows)) |
            (new_col >= len(rows[0]))
    ):
        return False

def get_start_coordinates(rows):
    for row_n, row in enumerate(rows):
        for col_n, el in enumerate(row):
            if el == 'S':
                return row_n, col_n


def go_up(row, col, rows):
    new_row = row - 1
    new_col = col
    if validate_new_coords(new_row, new_col, rows) is False:
        return None
    return new_row, new_col


def go_down(row, col, rows):
    new_row = row + 1
    new_col = col
    if validate_new_coords(new_row, new_col, rows) is False:
        return None
    return new_row, new_col


def go_right(row, col, rows):
    new_row = row
    new_col = col + 1
    if validate_new_coords(new_row, new_col, rows) is False:
        return None
    return new_row, new_col


def go_left(row, col, rows):
    new_row = row
    new_col = col - 1
    if validate_new_coords(new_row, new_col, rows) is False:
        return None
    return new_row, new_col


def validate_next_cell(curr_elem, next_elem, going_towards: Direction):
    if curr_elem == '-':
        if going_towards == Direction.RIGHT:
            if next_elem not in ['-', '7', 'J']:
                return False
        elif going_towards == Direction.LEFT:
            if next_elem not in ['-', 'L', 'F']:
                return False
    elif curr_elem == 'F':
        if going_towards == Direction.UP:
            if next_elem not in ['-', '7', 'J']:
                return False
        if going_towards == Direction.DOWN:
            if next_elem not in ['|', 'L', 'J']:
                return False
    elif curr_elem == 'J':
        if going_towards == Direction.DOWN:
            if next_elem not in ['-', 'L', 'F']:
                return False
        if going_towards == Direction.UP:
            if next_elem not in ['|', '7', 'F']:
                return False
    elif curr_elem == '|':
        if going_towards == Direction.DOWN:
            if next_elem not in ['|', 'L', 'J']:
                return False
        if going_towards == Direction.UP:
            if next_elem not in ['|', 'F', '7']:
                return False
    elif curr_elem == 'L':
        if going_towards == Direction.DOWN:
            if next_elem not in ['-', 'J', '7']:
                return False
        if going_towards == Direction.UP:
            if next_elem not in ['|', 'F', '7']:
                return False

    return True


def move(rows, curr_row, curr_col, curr_elem: str, going_towards: Direction) -> Optional[Tuple[int, int]]:
    """
    Moves from the given coordinates (curr_row, curr_col) in the
    direction given by going_towards. If this move is possible, it
    returns the coordinates of the next step, otherwise it returns None
    """
    if curr_elem == '.':
        return None
    if going_towards == Direction.UP:
        next_cell_coords = go_up(curr_row, curr_col, rows)
    elif going_towards == Direction.DOWN:
        next_cell_coords = go_down(curr_row, curr_col, rows)
    elif going_towards == Direction.LEFT:
        next_cell_coords = go_left(curr_row, curr_col, rows)
    elif going_towards == Direction.RIGHT:
        next_cell_coords = go_right(curr_row, curr_col, rows)
    else:
        raise ValueError()

    # If it is not a valid move, return None
    if next_cell_coords is None:
        return None
    else:
        next_row, next_col = next_cell_coords
        next_elem = rows[next_row][next_col]
        if validate_next_cell(curr_elem, next_elem, going_towards) is False:
            return None
        else:
            return next_cell_coords


def get_prev_elem_position(curr_row, curr_col, prev_row, prev_col):
    if curr_col == prev_col:
        if prev_row == curr_row - 1:
            return Direction.UP
        if prev_row == curr_row + 1:
            return Direction.DOWN

    elif prev_row == curr_row:
        if prev_col == curr_col - 1:
            return Direction.LEFT
        elif prev_col == curr_col + 1:
            return Direction.RIGHT


def get_direction(curr_elem: str, curr_row, curr_col, prev_row, prev_col):
    prev_elem_position = get_prev_elem_position(curr_row, curr_col, prev_row, prev_col)
    if curr_elem == 'F':
        if prev_elem_position == Direction.RIGHT:
            return Direction.DOWN
        elif prev_elem_position == Direction.DOWN:
            return Direction.RIGHT

    elif curr_elem == 'L':
        if prev_elem_position == Direction.UP:
            return Direction.RIGHT
        elif prev_elem_position == Direction.RIGHT:
            return Direction.UP

    elif curr_elem == 'J':
        if prev_elem_position == Direction.UP:
            return Direction.LEFT
        elif prev_elem_position == Direction.LEFT:
            return Direction.UP

    elif curr_elem == '7':
        if prev_elem_position == Direction.LEFT:
            return Direction.DOWN
        elif prev_elem_position == Direction.DOWN:
            return Direction.LEFT

    elif curr_elem == '|':
        if prev_elem_position == Direction.UP:
            return Direction.DOWN
        elif prev_elem_position == Direction.DOWN:
            return Direction.UP

    elif curr_elem == '-':
        if prev_elem_position == Direction.LEFT:
            return Direction.RIGHT
        elif prev_elem_position == Direction.RIGHT:
            return Direction.LEFT

    elif curr_elem == 'S':
        return Direction.RIGHT

    else:
        raise ValueError()


def puzzle_1_solution(input_str):
    rows = input_str.split('\n')
    curr_row, curr_col = get_start_coordinates(rows)
    curr_elem = 'S'
    for direction in list(Direction):
        can_move = True
        n_steps = 1
        while can_move:
            result = move(rows, curr_row, curr_col, curr_elem, going_towards=direction)
            if result is None:
                can_move = False
            else:
                n_steps += 1
                prev_row = curr_row
                prev_col = curr_col
                curr_row, curr_col = result
                curr_elem = rows[curr_row][curr_col]
                direction = get_direction(curr_elem, curr_row, curr_col, prev_row, prev_col)
                if curr_elem == 'S':
                    return n_steps

if __name__ == '__main__':
    n_steps = puzzle_1_solution(day_10_example_2)
    print(n_steps / 2)