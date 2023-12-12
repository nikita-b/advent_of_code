def get_difference_between_elements_in_list(seq):
    diff = []
    previous = seq[0]
    for i in seq[1:]:
        diff.append(i - previous)
        previous = i
    return diff



def recursive(seq):
    if set(seq) == {0} or len(seq) == 0:
        return 0
    else:
        print(seq)
        return seq[-1] + recursive(get_difference_between_elements_in_list(seq))


def main():
    content = open("day9-input.txt", "r").read()
#     content = """\
# 0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""
    content = content.split("\n")
    result = []
    for seq in content:
        seq = seq.split()
        seq = [int(i) for i in seq]
        seq.reverse()
        print("----------")
        current_result = recursive(seq)
        result.append(current_result)
        print("CURRENT RESULT:", current_result)
        print("----------")


    print(result)
    print(sum(result))



if __name__ == "__main__":
    main()
