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

    print(seed_numbers)
    print(number_maps)

    # {
    #     "seed-to-soil": [[50, 98, 2], [52, 50, 48]],
    #     "soil-to-fertilizer": [[0, 15, 37], [37, 52, 2], [39, 0, 15]],
    #     "fertilizer-to-water": [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]],
    #     "water-to-light": [[88, 18, 7], [18, 25, 70]],
    #     "light-to-temperature": [[45, 77, 23], [81, 45, 19], [68, 64, 13]],
    #     "temperature-to-humidity": [[0, 69, 1], [1, 0, 69]],
    #     "humidity-to-location": [[60, 56, 37], [56, 93, 4]],
    # }
    # How to iterate over this with keys and values?

    # dest_start, source_start, length

    lowest_location = None
    current_target = None

    for seed_number in seed_numbers:
        current_target = seed_number
        for key, maps in number_maps.items():
            for dest_start, source_start, length in maps:
                if current_target in range(source_start, source_start + length + 1):
                    print(f"Found target {current_target} in map {key}!")
                    # This corresponds to the matching entry in the destination range
                    new_target = dest_start + current_target - source_start
                    print(f"Maps to destination: {new_target}")
                    current_target = new_target
                    continue


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2023: Day 5")
    parser.add_argument("input_file_path", help="Path to input data file")
    args = parser.parse_args()
    process_file(args.input_file_path)


if __name__ == "__main__":
    main()
