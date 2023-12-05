import argparse
import re

numbers_pattern = re.compile("\D*(\d+)\D*")


def process_file(file_path, debug):
    with open(file_path, "r") as file:
        file_contents = file.read()
        file.close()

    # Split into lines
    lines = file_contents.splitlines()

    card_value_map = {}
    for line in lines:
        # Split out card info from numbers
        card_label, card_numbers = re.split(": ", line, 1)

        # Split out winning numbers from the Elf's
        card_winning_numbers, card_elf_numbers = [
            set(re.findall(numbers_pattern, number_set))
            for number_set in re.split(" \| ", card_numbers, 1)
        ]

        # Winners are the intersection of the sets
        num_winners = len(card_winning_numbers & card_elf_numbers)

        # TODO: Card copying

        # Calculate value and aggregate
        card_value = pow(2, num_winners - 1) if num_winners > 0 else 0
        print(f"{card_label} is worth {card_value}")

        card_value_map[card_label] = card_value

    print(f"Total value of all cards: {sum(card_value_map.values())}")


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
