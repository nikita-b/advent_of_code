import functools

def check_game(game):
    max_cubes = {"green": 0, "red": 0, "blue": 0}
    game_number, steps = game.split(":")
    for take in steps.split(";"):
        for cube in take.split(","):
            number, color = cube.split()
            if max_cubes[color] < int(number):
                max_cubes[color] = int(number)

    return functools.reduce(lambda i, j: i*j, max_cubes.values())


if __name__ == '__main__':

    contents = open("day2-1-input.txt", "r").read()

#     contents = """\
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    result = 0
    for game in contents.split("\n"):
        result += int(check_game(game))

    print("RESULT: ", result)