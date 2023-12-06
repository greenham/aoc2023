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

    # Pair the numbers into tuples representing the ranges of seeds (start, length)
    seed_number_ranges_part1 = [(i, 1) for i in seed_numbers]
    seed_number_ranges_part2 = list(zip(seed_numbers[::2], seed_numbers[1::2]))
    print(
        f"Lowest location (Part 1): {get_lowest_location_for_seeds(seed_number_ranges_part1, number_maps)}"
    )
    print(
        f"Lowest location (Part 2): {get_lowest_location_for_seeds(seed_number_ranges_part2, number_maps)}"
    )


def get_lowest_location_for_seeds(seeds, maps):
    locations = []

    for seed_range in seeds:
        targets_to_check = [[seed_range[0], seed_range[1] + seed_range[0]]]
        results = []
        for m in maps.values():
            while targets_to_check:
                target_start, target_end = targets_to_check.pop()
                for dest_start, source_start, map_length in m:
                    source_end = source_start + map_length
                    dest_offset = dest_start - source_start

                    if source_end <= target_start or target_end <= source_start:
                        # Falls outside of range
                        continue

                    if target_start < source_start:
                        # Beginning of range comes before beginning of source
                        targets_to_check.append([target_start, source_start])
                        target_start = source_start

                    if source_end < target_end:
                        # End of range comes after end of source
                        targets_to_check.append([source_end, target_end])
                        target_end = source_end

                    results.append([target_start + dest_offset, target_end + dest_offset])
                    break
                else:
                    results.append([target_start, target_end])

            targets_to_check = results
            results = []
        locations += targets_to_check

    return min(location[0] for location in locations)


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2023: Day 5")
    parser.add_argument("input_file_path", help="Path to input data file")
    args = parser.parse_args()
    process_file(args.input_file_path)


if __name__ == "__main__":
    main()
