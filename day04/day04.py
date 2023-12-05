import argparse
import re

numbers_pattern = re.compile("\D*(\d+)\D*")


def process_file(file_path):
    with open(file_path, "r") as file:
        file_contents = file.read()
        file.close()

    # Split into lines
    lines = file_contents.splitlines()

    card_map = [{"copies": 0, "value": 0}] * len(lines)
    for index, line in enumerate(lines, 0):
        # Split out card info from numbers
        card_label, card_numbers = re.split(": ", line, 1)

        # Split out winning numbers from the Elf's
        card_winning_numbers, card_elf_numbers = [
            set(re.findall(numbers_pattern, number_set))
            for number_set in re.split(" \| ", card_numbers, 1)
        ]

        # Winners are the intersection of the sets
        num_winners = len(card_winning_numbers & card_elf_numbers)

        # Calculate "points" value
        card_value = pow(2, num_winners - 1) if num_winners > 0 else 0

        card_map[index] = {
            "label": card_label,
            "points": card_value,
            "matches": num_winners,
            "num_copies": 1,
        }

    print(
        f"Total points value of all cards: {sum(card.get('points', 0) for card in card_map)}"
    )

    for index, card in enumerate(card_map):
        num_matches = card.get("matches", 0)
        num_copies = card.get("num_copies", 1)
        print(
            f"Processing Card {index+1} ({num_matches} matches) <has {num_copies} copies>"
        )
        if num_matches <= 0:
            continue

        start = index + 1
        end = start + num_matches

        while start < end:
            card_map[start]["num_copies"] += num_copies
            start += 1

    print(f"Total cards won: {sum(card.get('num_copies', 0) for card in card_map)}")


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2023: Day 4")
    parser.add_argument("input_file_path", help="Path to input data file")
    args = parser.parse_args()
    process_file(args.input_file_path)


if __name__ == "__main__":
    main()
