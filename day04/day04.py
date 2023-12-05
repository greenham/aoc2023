import argparse
import re

numbers_pattern = re.compile("\D*(\d+)\D*")


def process_file(file_path, debug):
    with open(file_path, "r") as file:
        file_contents = file.read()

    # Split into lines
    lines = file_contents.splitlines()

    card_total_value = 0
    for line_number, line in enumerate(lines, 1):
        # Split out card info from numbers
        parts = re.split(": ", line)
        card_label = parts[0]
        card_numbers = parts[1]

        # Split out winning numbers from the Elf's
        card_numbers_split = re.split(" \| ", card_numbers)
        card_number_sets = [
            set(re.findall(numbers_pattern, number_set))
            for number_set in card_numbers_split
        ]
        card_winning_numbers = card_number_sets[0]
        card_elf_numbers = card_number_sets[1]
        card_winners = card_winning_numbers & card_elf_numbers
        card_value = pow(2, len(card_winners) - 1) if len(card_winners) > 0 else 0
        print(f"{card_label} is worth {card_value}")
        card_total_value += card_value

    print(f"Total value of all cards: {card_total_value}")


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2023: Day 4")
    parser.add_argument("input_file_path", help="Path to input data file")
    parser.add_argument(
        "-d",
        "--debug",
        help="Show debugging output",
        action="store_true",
        default=True,
    )
    args = parser.parse_args()

    process_file(args.input_file_path, args.debug)


if __name__ == "__main__":
    main()
