from functools import reduce

visited = set()

def get_number(y, x, lines):
    line = lines[y]
    number = [line[x]]
    left_x = x - 1
    right_x = x + 1
    visited.add((x, y))
    while True:
        if line[left_x].isdigit():
            number.insert(0, line[left_x])
            visited.add((left_x, y))
            left_x -= 1
        else:
            break
    while True:
        if line[right_x].isdigit():
            number.append(line[right_x])
            visited.add((right_x, y))
            right_x += 1
        else:
            break

    return number


def check_number(x, y, lines):
    if lines[y][x].isdigit() and (x, y) not in visited:
        return get_number(y, x, lines)
    else:
        return None


options = ()

if __name__ == '__main__':
    contents = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    contents = open("day3-1-input.txt", "r").read()
    lines = contents.split("\n")
    lines.append("." * len(lines[0]))
    lines.insert(0, "." * len(lines[0]))

    for index, line in enumerate(lines):
        lines[index] = '.' + line + "."
    result = []
    all_numbers = []
    current_numbers = []
    amount_of_found = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "*":
                options = [
                    (x, y-1),
                    (x, y+1),
                    (x-1, y),
                    (x+1, y),

                    (x, y+1),
                    (x, y-1),
                    (x+1, y+1),
                    (x+1, y-1),
                    (x-1, y+1),
                    (x-1, y-1)
                ]
                for option in options:
                    number = check_number(option[0], option[1], lines)
                    if number:
                        current_numbers.append(number)

                if len(current_numbers) == 2:
                    current_numbers_as_int = [int(''.join(n)) for n in current_numbers]
                    all_numbers.append(current_numbers_as_int[0] * current_numbers_as_int[1])
                print(current_numbers)

                current_numbers = []


    print("RESULT: ", sum(all_numbers))

