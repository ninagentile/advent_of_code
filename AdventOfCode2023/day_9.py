from typing import List

from AdventOfCode2023.inputs.day_9_input import day_9_example, day_9_input


def get_report(input_str: str):
    rows_str = input_str.split('\n')
    rows = []
    for row in rows_str:
        rows.append([int(i) for i in row.split(' ')])

    return rows


def generate_next_sequence(history: List[int]) -> List[int]:
    next_sequence = []
    for i in range(0, len(history) - 1):
        curr = history[i]
        next = history[i + 1]
        next_sequence.append(next - curr)

    return next_sequence


def extract_end_of_sequence(sequences: List[List[int]]) -> int:
    # start from the last sequence
    for i in range(len(sequences) - 1, 0, -1):
        current_sequence = sequences[i]
        prev_sequence = sequences[i - 1]
        new_value = prev_sequence[-1] + current_sequence[-1]
        prev_sequence.append(new_value)

    return new_value


def puzzle_1_solution():
    report = get_report(day_9_input)
    values = []
    for line in report:
        prev_sequence = line
        sequences = [line]
        while True:
            next_sequence = generate_next_sequence(prev_sequence)
            sequences.append(next_sequence)
            prev_sequence = next_sequence

            # If all elements are 0, find the end of each sequence
            if set(next_sequence) == {0}:
                # extract the end of each sequence
                final_value = extract_end_of_sequence(sequences)
                values.append(final_value)
                break
    return sum(values)


def extract_start_of_sequence(sequences: List[List[int]]) -> int:
    # start from the last sequence
    new_value = None
    for i in range(len(sequences) - 1, 0, -1):
        current_sequence = sequences[i]
        prev_sequence = sequences[i - 1]
        new_value = prev_sequence[0] - current_sequence[0]
        prev_sequence.insert(0, new_value)

    return new_value


def puzzle_2_solution():
    report = get_report(day_9_input)
    values = []
    for line in report:
        prev_sequence = line
        sequences = [line]
        while True:
            next_sequence = generate_next_sequence(prev_sequence)
            sequences.append(next_sequence)
            prev_sequence = next_sequence

            # If all elements are 0, find the end of each sequence
            if set(next_sequence) == {0}:
                # extract the end of each sequence
                final_value = extract_start_of_sequence(sequences)
                values.append(final_value)
                break
    print(values)
    return sum(values)


if __name__ == '__main__':
    print(puzzle_2_solution())
