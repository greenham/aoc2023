DAY = 8
import argparse
import re


def process_file(file_path, ghost=False):
    with open(file_path, "r") as file:
        file_contents = file.read()
        file.close()

    lines = file_contents.split("\n")
    directions = list(lines[0])
    nodes = lines[2::]
    node_map = {}

    for node in nodes:
        key, value = map(str.strip, node.split("="))
        value_tuple = tuple(map(str.strip, value.strip("()").split(",")))
        node_map[key] = value_tuple

    current_step = 0
    steps_taken = 0

    # Part 1
    if not ghost:
        current_node_id = "AAA"
        while True:
            next_element_map = node_map[current_node_id]
            print(
                f"Current node: {current_node_id}, map: {next_element_map}, going {directions[current_step]}"
            )
            current_node_id = (
                next_element_map[0]
                if directions[current_step] == "L"
                else next_element_map[1]
            )

            steps_taken += 1

            if current_node_id == "ZZZ":
                print("We made it!")
                break

            # handle incrementing + reaching the end of the directions without having found the end
            current_step = (current_step + 1) % len(directions)

            print(
                f"Next node is {current_node_id}, total steps taken so far: {steps_taken}, current step: {current_step}"
            )
    # Part 2
    else:
        current_nodes = {
            key: value for key, value in node_map.items() if re.match("^.*A$", key)
        }
        print(f"Starting nodes: {current_nodes}")
        while True:
            # get the next set of nodes to follow
            next_maps = current_nodes.values()
            follow_index = 0 if directions[current_step] == "L" else 1
            next_node_keys = [item[follow_index] for item in next_maps]
            steps_taken += 1

            print(f"taking {directions[current_step]} path")
            print(f"next_node_keys: {next_node_keys}")
            print(f"steps taken so far: {steps_taken}")

            # see if they all end in Z
            if all(re.match("^.*Z$", key) for key in next_node_keys):
                print("We made it!")
                break

            current_nodes = {
                key: value for key, value in node_map.items() if key in next_node_keys
            }

            # handle incrementing + reaching the end of the directions without having found the end
            current_step = (current_step + 1) % len(directions)

    print(f"Total steps taken: {steps_taken}")


def main():
    parser = argparse.ArgumentParser(description=f"Advent of Code 2023: Day {DAY}")
    parser.add_argument(
        "input_file_path", help="Path to input data file", default="example-input"
    )
    parser.add_argument(
        "-g",
        "--ghost",
        help="Move like a ghost!",
        action="store_true",
        default=False,
    )
    args = parser.parse_args()
    process_file(args.input_file_path, args.ghost)


if __name__ == "__main__":
    main()
