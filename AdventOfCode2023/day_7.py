from typing import List

from AdventOfCode2023.day_7_input import day_7_input

# Map the labels of the cards to other letters so that, if put in
# lexicographic order, the first card is also the winning one
mapping_to_lexicographic_order = {
    'A': 'E', 'K': 'D', 'Q': 'C', 'J': 'B', 'T': 'A', '9': '9', '8': '8',
    '7': '7', '6': '6', '5': '5', '4': '4', '3': '3', '2': '2'
}


def is_five_of_a_kind(counts: List[int]) -> bool:
    # If all the cards have the same label, return True
    if len(counts) == 1:
        return True
    return False


def is_four_of_a_kind(counts: List[int]) -> bool:
    if counts == [1, 4]:
        return True
    return False


def is_three_of_a_kind(counts: List[int]) -> bool:
    if counts == [1, 1, 3]:
        return True
    return False


def is_full_hand(counts: List[int]) -> bool:
    if counts == [2, 3]:
        return True
    return False


def is_two_pairs(counts: List[int]) -> bool:
    if counts == [1, 2, 2]:
        return True
    return False


def is_one_pair(counts: List[int]) -> bool:
    if counts == [1, 1, 1, 2]:
        return True
    return False


def is_high_card(counts: List[int]) -> bool:
    if counts == [1, 1, 1, 1, 1]:
        return True
    return False


def get_card_counts(hand: str) -> List[int]:
    """
    Counts the occurrences of each label in hand, and returns an ordered
    list of occurrences
    """
    # If all the cards but one have the same label, return True
    unique_labels = set(hand)
    counts = []
    for unique_labels in unique_labels:
        counts.append(hand.count(unique_labels))
    return sorted(counts)


def get_mapped_hand(hand: str) -> str:
    """
    Maps a hand using mapping_to_lexicographic_order
    """
    mapped_hand = ''

    for elem in hand:
        mapped_hand += mapping_to_lexicographic_order[elem]

    return mapped_hand


def get_hands_and_bids() -> dict:
    """
    Extracts the hands and the corresponding bids from the input
    """
    hands_and_bids = {}
    rows = day_7_input.split('\n')
    for row in rows:
        hand, bid_str = row.split(' ')

        # Get the mapped version of the hand (to allow lexicographic
        # ordering)
        hand = get_mapped_hand(hand)

        hands_and_bids[hand] = int(bid_str)
    return hands_and_bids


def sort_lexicographically(hands: list) -> list:
    return sorted(hands)


def puzzle_1_solution():
    hands_and_bids = get_hands_and_bids()

    five_of_a_kinds = []
    four_of_a_kinds = []
    full_hands = []
    three_of_a_kinds = []
    two_pairs = []
    one_pairs = []
    high_cards = []

    for hand in hands_and_bids.keys():
        counts = get_card_counts(hand=hand)
        if is_five_of_a_kind(counts):
            five_of_a_kinds.append(hand)
        elif is_four_of_a_kind(counts):
            four_of_a_kinds.append(hand)
        elif is_full_hand(counts):
            full_hands.append(hand)
        elif is_three_of_a_kind(counts):
            three_of_a_kinds.append(hand)
        elif is_two_pairs(counts):
            two_pairs.append(hand)
        elif is_one_pair(counts):
            one_pairs.append(hand)
        elif is_high_card(counts):
            high_cards.append(hand)

    # Sort in lexicographic order
    five_of_a_kinds = sort_lexicographically(five_of_a_kinds)
    four_of_a_kinds = sort_lexicographically(four_of_a_kinds)
    full_hands = sort_lexicographically(full_hands)
    three_of_a_kinds = sort_lexicographically(three_of_a_kinds)
    two_pairs = sort_lexicographically(two_pairs)
    one_pairs = sort_lexicographically(one_pairs)
    high_cards = sort_lexicographically(high_cards)

    rank = 1
    total_winnings = 0
    hands_types = [
        high_cards, one_pairs, two_pairs, three_of_a_kinds,
        full_hands, four_of_a_kinds, five_of_a_kinds
    ]
    for hands_type in hands_types:
        for hand in hands_type:
            bid = hands_and_bids[hand]
            total_winnings += bid * rank
            rank += 1

    return total_winnings

