

def is_symbol(c):
    return not c.isdigit() and c != '.'
# ['467', '35', '633', '617', '755', '664', '598']
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
    current_number = []
    add_to_sum = False
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c.isdigit():
                current_number.append(c)
                if is_symbol(lines[y-1][x]):
                    add_to_sum = True
                if is_symbol(lines[y+1][x]):
                    add_to_sum = True
                if is_symbol(lines[y][x-1]):
                    add_to_sum = True
                if is_symbol(lines[y][x+1]):
                    add_to_sum = True
                if is_symbol(lines[y+1][x+1]):
                    add_to_sum = True
                if is_symbol(lines[y-1][x-1]):
                    add_to_sum = True
                if is_symbol(lines[y-1][x+1]):
                    add_to_sum = True
                if is_symbol(lines[y+1][x-1]):
                    add_to_sum = True
                if is_symbol(lines[y+1][x-1]):
                    add_to_sum = True
            elif current_number:
                if add_to_sum:
                    result.append(''.join(current_number))
                current_number = []
                add_to_sum = False

    print(result)
    print(sum([int(i) for i in result]))

