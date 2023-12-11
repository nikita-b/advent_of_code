
from collections import defaultdict
def main():
    content = open("day7-input.txt", "r").read()
#     content = """\
# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""
    five_kind = []
    four_kind = []
    full_house = []
    three_kind = []
    two_pair = []
    one_pair = []
    high_card = []
    for hands_with_score in content.split("\n"):
        hand, score = hands_with_score.split()
        for index, symbol in enumerate(reversed(("A", "K", "Q", "T"))):
            hand = hand.replace(symbol, chr(ord("9") + (index + 1)))
        hand = hand.replace("J", "1")

        hand_with_score = (hand, score)
        symbols = defaultdict(int)
        for c in hand:
            symbols[c] += 1

        most_common_symbols = sorted(symbols.items(), key=lambda item: item[1], reverse=True)
        if most_common_symbols[0][0] == "1" and len(most_common_symbols) == 1:
            most_common_symbol = "0"
        elif most_common_symbols[0][0] == "1":
            most_common_symbol = most_common_symbols[1][0]
        else:
            most_common_symbol = most_common_symbols[0][0]

        print(most_common_symbols, most_common_symbol)


        if "1" in symbols:
            symbols[most_common_symbol] += symbols["1"]
            del symbols["1"]

        result = sorted(list(symbols.values()), reverse=True)
        #print(result, symbols, hand_with_score)

        match result:
            case [5]:
                five_kind.append(hand_with_score)
            case [4,1]:
                four_kind.append(hand_with_score)
            case [3,2]:
                full_house.append(hand_with_score)
            case [3,1,1]:
                three_kind.append(hand_with_score)
            case [2,2,1]:
                two_pair.append(hand_with_score)
            case [2,1,1,1]:
                one_pair.append(hand_with_score)
            case _:
                high_card.append(hand_with_score)

    five_kind.sort(key=lambda s: s[0])
    four_kind.sort(key=lambda s: s[0])
    full_house.sort(key=lambda s: s[0])
    three_kind.sort(key=lambda s: s[0])
    two_pair.sort(key=lambda s: s[0])
    one_pair.sort(key=lambda s: s[0])
    high_card.sort(key=lambda s: s[0])

    print("FIVE: ", five_kind)
    print("FOUR: ", four_kind)
    print("FULL HOUSE: ", full_house)
    print("THREE: ", three_kind)
    print("TWO: ", two_pair)
    print("ONE: ", one_pair)
    print("HIGH_CARD: ", high_card)
    ranked_hands = high_card + one_pair + two_pair + three_kind + full_house + four_kind + five_kind
    result = 0
    for rank, hand in enumerate(ranked_hands):
        #print(rank + 1, " * ", int(hand[1]))

        result += (rank + 1) * int(hand[1])

    print(result)
    # 252898370


if __name__ == "__main__":
    main()
