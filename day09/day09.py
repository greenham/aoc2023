DAY = 9
import argparse


def process_file(file_path):
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
        next_value = get_next_value(history_pyramid)
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

    if sum(new_diffs) == 0:
        return acc

    return get_diffs(new_diffs.copy(), acc)


def get_next_value(lists):
    for i in range(2, len(lists)):
        lists[i].append(lists[i - 1][-1] + lists[i][-1])

    return lists[-1][-1]


def main():
    parser = argparse.ArgumentParser(description=f"Advent of Code 2023: Day {DAY}")
    parser.add_argument("input_file_path", help="Path to input data file")
    args = parser.parse_args()
    process_file(args.input_file_path)


if __name__ == "__main__":
    main()
