
from collections import defaultdict
from functools import reduce
import math
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

def get_next_nodes(node_name, direction, maps_of_desert):
    point = maps_of_desert[node_name]
    if direction == "L":
        point_name = point.left
    else:
        point_name = point.right

    return point_name

def lcm(arr):

    l=reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
    return l

def main():
    content = open("day8-input.txt", "r").read()
#     content = """\
# LR
#
# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""
    content = content.split("\n")
    directions = content[0]
    maps_of_desert = {}
    for m in content[2:]:
        current_point = m.split("=")[0].strip()
        left_dir, right_dir = m.split("=")[1].split(',')
        maps_of_desert[current_point] = Node(left_dir.strip()[1:], right_dir.strip()[:-1])

    current_nodes = []
    for node_name in maps_of_desert.keys():
        if node_name.endswith("A"):
            current_nodes.append(node_name)

    result = 0
    total_result = []
    for current_node in current_nodes:
        for d in infinite_directions(directions):
            result += 1
            next_node = get_next_nodes(current_node, d, maps_of_desert)
            print(next_node)
            if next_node.endswith("Z"):
                total_result.append(result)
                break
            current_node = next_node
        result = 0

    print(lcm(total_result))



if __name__ == "__main__":
    main()
