
from collections import defaultdict


def infinite_directions(direction):
    while True:
        for i in direction:
            yield i

class Node():
    def __init__(self, left, right):
        self.right = right
        self.left = left
    def __repr__(self):
        return "[" + self.right + "][" + self.left + "]"

def main():
    content = open("day8-input.txt", "r").read()
#     content = """\
# LLR
#
# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)"""
    content = content.split("\n")
    directions = content[0]
    maps_of_desert = {}
    for m in content[2:]:
        current_point = m.split("=")[0].strip()
        left_dir, right_dir = m.split("=")[1].split(',')
        maps_of_desert[current_point] = Node(left_dir.strip()[1:], right_dir.strip()[:-1])

    point_name = "AAA"
    result = 0
    for d in infinite_directions(directions):
        result += 1
        point = maps_of_desert[point_name]
        print(point)
        if d == "L":
            point_name = point.left
        else:
            point_name = point.right

        if point_name == "ZZZ":
            print(result)
            break


if __name__ == "__main__":
    main()
