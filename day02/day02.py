import argparse
import regex as re

grab_color_pattern = re.compile("(\d+)(red|green|blue)")
cube_inventory = {"red": 12, "green": 13, "blue": 14}


def parse_line(line):
    # Clean up the line a bit and make it easier to parse
    line = line.strip().replace(" ", "")

    # Split out game ID from game details
    game_parts = re.split(":", line)
    game_details = game_parts[1]

    # Extract Game ID
    game_id = re.search("^Game(\d+)", game_parts[0]).group(1)

    # Split out each "grab" from the game details
    game_grabs = game_details.split(";")

    # Parse the grabs, seeing if there are any that violate the established count
    for grab in game_grabs:
        sets = grab.split(",")
        for roll in sets:
            roll_seen = re.search(grab_color_pattern, roll)
            count = roll_seen.group(1)
            color = roll_seen.group(2)
            if int(count) > cube_inventory[color]:
                # BAD ROLL
                print(
                    f"Found impossible roll in game {game_id}: {count} {color} seen, but only {cube_inventory[color]} in inventory"
                )
                return 0

    return int(game_id)


def process_file(file_path):
    id_sum = 0

    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            id_sum += parse_line(line)

    return id_sum


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2023: Day 2")
    parser.add_argument("input_file_path", help="Path to input data file")
    args = parser.parse_args()

    results = process_file(args.input_file_path)

    print(f"Sum of possible game IDs: {results}")


if __name__ == "__main__":
    main()
