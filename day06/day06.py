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
    race_counter = 0
    for time, record in races:
        wins = get_possible_wins_in_race(time, record)
        race_counter += 1
        print(f"{wins} possible wins in race {race_counter}")
        ways_to_win.append(wins)

    print(f"Margin of error: {math.prod(ways_to_win)}")

    # hacky part 2
    clean_times = int(re.sub(r"\D+", "", lines[0]))
    clean_records = int(re.sub(r"\D+", "", lines[1]))
    print(
        f"Possible wins for big race: {get_possible_wins_in_race(clean_times, clean_records)}"
    )


def get_possible_wins_in_race(time, record):
    wins = 0
    hold_time = time - 1
    while hold_time > 0:
        distance = hold_time * (time - hold_time)
        hold_time -= 1
        if distance > record:
            wins += 1
    return wins


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2023: Day 6")
    parser.add_argument("input_file_path", help="Path to input data file")
    args = parser.parse_args()
    process_file(args.input_file_path)


if __name__ == "__main__":
    main()
