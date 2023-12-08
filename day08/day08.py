DAY = 8
import argparse


def process_file(file_path):
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

    steps_to_take = directions[:]
    current_node_id = next(iter(node_map))
    steps_taken = 0
    for step in steps_to_take:
        next_element_map = node_map[current_node_id]
        print(f"Current node: {current_node_id}, going {step}, map: {next_element_map}")

        current_node_id = next_element_map[0] if step == "L" else next_element_map[1]
        steps_taken += 1
        print(f"Next node is {current_node_id}! Steps taken: {steps_taken}")
        if current_node_id == "ZZZ":
            print("We made it!")
            break

        # handle reaching the end
        if steps_taken == len(directions):
            print(f"Reached the end, repeating {len(directions)} directions")
            steps_to_take.extend(directions)

    print(f"Total steps taken: {steps_taken}")


def main():
    parser = argparse.ArgumentParser(description=f"Advent of Code 2023: Day {DAY}")
    parser.add_argument(
        "input_file_path", help="Path to input data file", default="example-input"
    )
    args = parser.parse_args()
    process_file(args.input_file_path)


if __name__ == "__main__":
    main()
