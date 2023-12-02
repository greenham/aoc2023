import argparse
import regex as re

number_word_map = {
    "zero": "0",
    "0": "0",
    "one": "1",
    "1": "1",
    "two": "2",
    "2": "2",
    "three": "3",
    "3": "3",
    "four": "4",
    "4": "4",
    "five": "5",
    "5": "5",
    "six": "6",
    "6": "6",
    "seven": "7",
    "7": "7",
    "eight": "8",
    "8": "8",
    "nine": "9",
    "9": "9",
}

number_pattern = "|".join(number_word_map.keys())


def extract_number_from_line(line, include_words=False):
    pattern = "\d" if include_words is False else number_pattern

    matches = list(re.findall(pattern, line, overlapped=True))

    if matches:
        first_value = number_word_map.get(matches[0], "0")
        last_value = number_word_map.get(matches[-1], "0")
        return int(first_value + last_value)
    else:
        return 0


def process_file(file_path, include_words=False):
    calibration_sum = 0

    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            calibration_sum += extract_number_from_line(line, include_words)

    return calibration_sum


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2023: Day 1")
    parser.add_argument("input_file_path", help="Path to input data file")
    parser.add_argument(
        "-w",
        "--include-words",
        help="If present, will check for word representation of numbers to include in sum",
        action="store_true",
    )
    args = parser.parse_args()

    results = process_file(args.input_file_path, args.include_words)

    print(f"Sum of calibration values: {results}")


if __name__ == "__main__":
    main()
