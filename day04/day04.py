import argparse


def process_file(file_path, debug):
    with open(file_path, "r") as file:
        file_contents = file.read()
        if debug:
            print(file_contents)


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
