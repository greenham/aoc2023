import argparse


def process_file(file_path):
    with open(file_path, "r") as file:
        file_contents = file.read()
        file.close()

    lines = file_contents.splitlines()

    seed_numbers = []
    number_maps = {}
    current_map = None

    for line in lines:
        if len(line) == 0:
            continue

        if line.startswith("seeds: "):
            seed_numbers.extend(map(int, line.split(":")[1].split()))
        elif line.endswith("map:"):
            current_map = line.replace(" map:", "").replace("-to-", ":")
            number_maps[current_map] = []
        elif current_map is not None:
            if line.endswith("map:"):
                current_map = None
            else:
                number_maps[current_map].append(tuple(map(int, line.split())))

    lowest_location = None
    current_target = None

    for seed_number in seed_numbers:
        print(f"Searching for location for seed {seed_number}...")
        current_target = seed_number
        for key, maps in number_maps.items():
            print(f"CHECKING MAP: {key} | TARGET: {current_target}")
            for dest_start, source_start, length in maps:
                if current_target in range(source_start, source_start + length + 1):
                    print(f"Found target {current_target} in map {key}!")

                    # This corresponds to the matching entry in the destination range
                    new_target = dest_start + current_target - source_start
                    print(f"Setting new target: {new_target}")
                    current_target = new_target
                    break

        if lowest_location is None or current_target < lowest_location:
            lowest_location = current_target

    print(f"Lowest location found: {lowest_location}")


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2023: Day 5")
    parser.add_argument("input_file_path", help="Path to input data file")
    args = parser.parse_args()
    process_file(args.input_file_path)


if __name__ == "__main__":
    main()
