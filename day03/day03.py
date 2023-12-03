import argparse


def parse_game_line(line):
    return line


def process_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = parse_game_line(line)
            print(line)


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2023: Day 3")
    parser.add_argument("input_file_path", help="Path to input data file")
    args = parser.parse_args()

    process_file(args.input_file_path)


if __name__ == "__main__":
    main()
