import argparse
import math
import re


def process_file(file_path):
    with open(file_path, "r") as file:
        file_contents = file.read()
        file.close()

    lines = file_contents.splitlines()

    times = list(map(int, re.findall(r"\d+", lines[0])))
    records = list(map(int, re.findall(r"\d+", lines[1])))
    races = list(zip(times, records))

    ways_to_win = []
    for time, record in races:
        # Calculate wins for each possible time we can hold the button down
        # (except for 0 and time)
        wins = 0
        hold_time = time - 1
        while hold_time > 0:
            distance = hold_time * (time - hold_time)
            hold_time -= 1
            if distance > record:
                wins += 1

        ways_to_win.append(wins)

    print(math.prod(ways_to_win))


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2023: Day 5")
    parser.add_argument("input_file_path", help="Path to input data file")
    args = parser.parse_args()
    process_file(args.input_file_path)


if __name__ == "__main__":
    main()
