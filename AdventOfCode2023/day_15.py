from typing import List

import numpy as np

from AdventOfCode2023.inputs.day_15_input import day_15_input

example = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'


def get_ascii_code(el: str) -> int:
    return ord(el)


def apply_hash_algorithm(input_str: str) -> int:
    """
    Determine the ASCII code for the current character of the string.
    Increase the current value by the ASCII code you just determined.
    Set the current value to itself multiplied by 17.
    Set the current value to the remainder of dividing itself by 256.
    """
    current_value = 0
    for el in input_str:
        current_value += get_ascii_code(el)
        current_value *= 17
        current_value = np.remainder(current_value, 256)
    return current_value


def puzzle_1_solution(input_str: List[str]) -> int:
    sum = 0
    for el in input_str:
        sum += apply_hash_algorithm(el)

    return sum


if __name__ == '__main__':

    # print(puzzle_1_solution(example.split(',')))
    print(puzzle_1_solution(day_15_input.split(',')))