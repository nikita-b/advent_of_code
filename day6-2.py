

def main():
    content = open("day6-input.txt", "r").read()
#     content = """\
# Time:      7  15   30
# Distance:  9  40  200"""
    time, distance = content.split("\n")
    t = int(''.join((time.split(":")[1].split())))
    d = int(''.join(distance.split(":")[1].split()))
    total_ways = []

    result = []
    for i in range(1, t - 1):
        passed_distance = (t - i) * i
        #print(t, "-", i, "*", i, "==", passed_distance, "d", d)

        if passed_distance > d:
            result.append(passed_distance)
    #print(result)
    total_ways.append(len(result))

    #print(total_ways)
    answer = 1
    for i in total_ways:
        answer = answer * i
    print(answer)





if __name__ == "__main__":
    main()
