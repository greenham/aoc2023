DAY = 7
import argparse

card_value_map = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}

# Reading a stream of characters
# Keeping track of how many of each char we've seen
# Sort that list, check the max

hand_rankings = {
    "five-of-a-kind": 7,
    "four-of-a-kind": 6,
    "full-house": 5,
    "three-of-a-kind": 4,
    "two-pair": 3,
    "one-pair": 2,
    "high-card": 1,
}


class Card:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return card_value_map[self.value] < card_value_map[other.value]

    def __gt__(self, other):
        return card_value_map[self.value] > card_value_map[other.value]

    def __eq__(self, other):
        return self.value == other.value


class Hand:
    def __init__(self, value, ref):
        self.value = value
        self.ref = ref
        self.chars = list(value)
        self.cards = [Card(char) for char in self.chars]

        char_count = {}
        for char in self.chars:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        sorted_counts = sorted(
            char_count.items(), key=lambda item: item[1], reverse=True
        )
        best_count = sorted_counts[0][1]
        if best_count == 5:
            self.hand_type = "five-of-a-kind"
        elif best_count == 4:
            self.hand_type = "four-of-a-kind"
        elif best_count == 3:
            # max = 3, we have _at least_ 3 of a kind, maybe a full house
            # check for full house
            if (sorted_counts[1][1]) == 2:
                self.hand_type = "full-house"
            else:
                self.hand_type = "three-of-a-kind"
        elif best_count == 2:
            # max = 2, we have _at least_ a pair, maybe 2 pair
            # check for 2 pair
            if (sorted_counts[1][1]) == 2:
                self.hand_type = "two-pair"
            else:
                self.hand_type = "one-pair"
        elif best_count == 1:
            self.hand_type = "high-card"

        self.rank = hand_rankings[self.hand_type]

    def __lt__(self, other):
        # compare ranks first
        if self.rank < other.rank:
            return True

        if self.rank > other.rank:
            return False

        compare_cards = list(zip(self.cards, other.cards))
        for self_card, other_card in compare_cards:
            if self_card < other_card:
                return True

            if self_card > other_card:
                return False
        else:
            return False

    def __gt__(self, other):
        # compare ranks first
        if self.rank > other.rank:
            return True

        if self.rank < other.rank:
            return False

        compare_cards = list(zip(self.cards, other.cards))
        for self_card, other_card in compare_cards:
            if self_card > other_card:
                return True
            if self_card < other_card:
                return False
        else:
            return False

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"<Hand:{self.ref}>: 'value': '{self.value}', 'hand_type': '{self.hand_type}', rank: '{self.rank}' | "


def process_file(file_path):
    with open(file_path, "r") as file:
        file_contents = file.read()
        file.close()

    lines = file_contents.split("\n")
    data = [line.split() for line in lines]
    data_by_columns = list(zip(*data))

    hands = [
        Hand(hand_string, ref) for ref, hand_string in enumerate(data_by_columns[0])
    ]
    bids = list(map(int, data_by_columns[1]))
    # Tie these together via in ID or something since they're gonna get sorted

    sorted_hands = sorted(hands, reverse=True)

    hand_final_rank = len(sorted_hands)
    ranked_hands = []
    for hand in sorted_hands:
        hand.final_rank = hand_final_rank
        hand.bid = bids[hand.ref]
        hand.winnings = hand.final_rank * hand.bid
        print(
            f"winnings for <Hand:{hand.ref}> [{hand.value}]: {hand.winnings} (final rank: {hand.final_rank}, bid: {hand.bid})"
        )
        ranked_hands.append(hand)
        hand_final_rank -= 1

    # print(ranked_hands)
    print(f"Total winnings: {sum(hand.winnings for hand in ranked_hands)}")


def main():
    parser = argparse.ArgumentParser(description=f"Advent of Code 2023: Day {DAY}")
    parser.add_argument("input_file_path", help="Path to input data file")
    args = parser.parse_args()
    process_file(args.input_file_path)


if __name__ == "__main__":
    main()
