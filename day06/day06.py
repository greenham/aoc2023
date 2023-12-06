import argparse


def process_file(file_path):
    with open(file_path, "r") as file:
        file_contents = file.read()
        file.close()

    lines = file_contents.splitlines()
    print(lines)


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2023: Day 5")
    parser.add_argument("input_file_path", help="Path to input data file")
    args = parser.parse_args()
    process_file(args.input_file_path)


if __name__ == "__main__":
    main()
