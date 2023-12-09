DAY = 9
import argparse


def process_file(file_path, backwards=False):
    with open(file_path, "r") as file:
        file_contents = file.read()
        file.close()

    lines = file_contents.split("\n")
    histories = [line.split() for line in lines]

    values = []
    for history in histories:
        history = list(map(int, history))

        # find the difference in between each pair
        diffs = get_diffs(history.copy(), [])

        # form the pyramid
        diffs.insert(0, history)
        history_pyramid = diffs[::-1]

        # extrapolate
        next_value = get_next_value(history_pyramid, backwards)
        values.append(next_value)

    print(f"Total: {sum(values)}")


def get_diffs(history, acc):
    new_diffs = []
    while True:
        if len(history) < 2:
            break

        value1 = history.pop(0)
        value2 = history[0]
        new_diffs.append(value2 - value1)

    acc += [new_diffs]

    if all(d == 0 for d in new_diffs):
        return acc

    return get_diffs(new_diffs.copy(), acc)


def get_next_value(lists, backwards=False):
    if backwards:
        # Flip each list inside the history pyramid
        lists = [list(reversed(l)) for l in lists]

    for i in range(2, len(lists)):
        prev_value = lists[i - 1][-1] * -1 if backwards else lists[i - 1][-1]
        lists[i].append(prev_value + lists[i][-1])

    return lists[-1][-1]


def main():
    parser = argparse.ArgumentParser(description=f"Advent of Code 2023: Day {DAY}")
    parser.add_argument("input_file_path", help="Path to input data file")
    parser.add_argument(
        "-b",
        "--backwards",
        action="store_true",
        help="Extrapolate backwards",
        default=False,
    )
    args = parser.parse_args()
    process_file(args.input_file_path, args.backwards)


if __name__ == "__main__":
    main()
