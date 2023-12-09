DAY = 9
import argparse


def process_file(file_path, ghost=False):
    with open(file_path, "r") as file:
        file_contents = file.read()
        file.close()

    lines = file_contents.split("\n")
    print(lines)


def main():
    parser = argparse.ArgumentParser(description=f"Advent of Code 2023: Day {DAY}")
    parser.add_argument(
        "input_file_path", help="Path to input data file", default="example-input"
    )
    args = parser.parse_args()
    process_file(args.input_file_path, args.ghost)


if __name__ == "__main__":
    main()
