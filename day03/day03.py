import argparse
import math
import re

match_numbers = re.compile("\D*(\d+)\D*")
match_symbols = re.compile("[^0-9.]")


def process_file(file_path, debug):
    part_numbers = []
    possible_gears = {}

    with open(file_path, "r") as file:
        file_contents = file.read()

    # Split into lines
    lines = file_contents.splitlines()

    # Create a matrix of characters
    char_matrix = [list(line) for line in lines]

    # Find numbers in each line
    for line_number, line in enumerate(lines, 0):
        matches = re.finditer(match_numbers, line)
        for match in matches:
            number_found = match.group(1)
            number_start = match.start(1)
            number_end = match.end(1) - 1

            if debug:
                print(
                    f"Found number {number_found} on line {line_number}, spans {number_start} -> {number_end}"
                )

            # Check the appropriate "coordinates" in the matrix to see if there's an "adjacent" symbol
            x_coords_range = range(number_start - 1, number_end + 2)
            coords_to_check = (
                # Left + Right
                [
                    (line_number, number_start - 1),
                    (line_number, number_end + 1),
                ]
                # Above + Below + Diag
                + [(line_number - 1, i) for i in x_coords_range]
                + [(line_number + 1, i) for i in x_coords_range]
            )

            for x, y in coords_to_check:
                if 0 <= x < len(char_matrix) and 0 <= y < len(char_matrix[x]):
                    char_at_coord = char_matrix[x][y]
                    if re.match(match_symbols, char_at_coord):
                        if char_at_coord == "*":
                            if debug:
                                print(f"Possible gear found at ({x}, {y})")
                            gear_map_key = f"{x}-{y}"
                            gear_values = possible_gears.get(gear_map_key, [])
                            gear_values.append(int(number_found))
                            possible_gears[gear_map_key] = gear_values

                        part_numbers.append(number_found)
                        break

    part_numbers_int = [int(value) for value in part_numbers]
    print(f"{len(part_numbers)} part numbers found!")
    print(f"Sum of part numbers: {sum(part_numbers_int)}")

    # Filter out any gears that don't have exactly two values
    gears_actual = {
        key: value
        for key, value in possible_gears.items()
        if isinstance(value, list) and len(value) == 2
    }
    gear_ratios = {key: math.prod(value) for key, value in gears_actual.items()}
    gear_sum = sum(gear_ratios.values())
    print(f"Sum of gear ratios: {gear_sum}")


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2023: Day 3")
    parser.add_argument("input_file_path", help="Path to input data file")
    parser.add_argument(
        "-d",
        "--debug",
        help="Show debugging output",
        action="store_true",
        default=False,
    )
    args = parser.parse_args()

    process_file(args.input_file_path, args.debug)


if __name__ == "__main__":
    main()
