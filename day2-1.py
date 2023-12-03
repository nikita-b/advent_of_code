MAX_CUBES= {"red": 12,
            "green": 13,
            "blue": 14
            }


def check_game(game):
    game_number, steps = game.split(":")
    for take in steps.split(";"):
        for cube in take.split(","):
            number, color = cube.split()
            if MAX_CUBES[color] < int(number):
                return 0

    return game_number.split()[1]


if __name__ == '__main__':
    contents = open("day2-1-input.txt", "r").read()

    result = 0
    for game in contents.split("\n"):
        result += int(check_game(game))

    print("RESULT: ", result)