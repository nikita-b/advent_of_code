

def get_value_of_index(d: dict, value):
    print(d, value)
    if value in d:
        return d[value]
    else:
        return value

if __name__ == '__main__':
    contents = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
    contents = open("day5-input.txt", "r").read()
    seeds = contents.split("\n")[0].split(":")[1].split()
    seed_to_soil = dict()
    soil_to_fertilizer = dict()
    fertilizer_to_water = dict()
    water_to_light = dict()
    light_to_temperature = dict()
    temperature_to_humidity = dict()
    humidity_to_location = dict()
    for deps in contents[2:].split("\n\n"):
        print(deps)
        deps_list = deps.split("\n")
        for dep in deps_list[1:]:
            d = dep.split()
            dest = int(d[0])
            source = int(d[1])
            length = int(d[2])
            one_to_one = zip(range(source, source + length), range(dest, dest + length))

            match deps_list[0].split()[0]:
                case "seed-to-soil":
                    for s, d in one_to_one:
                        seed_to_soil[s] = d
                case "soil-to-fertilizer":
                    for s, d in one_to_one:
                        soil_to_fertilizer[s] = d
                case "fertilizer-to-water":
                    for s, d in one_to_one:
                        fertilizer_to_water[s] = d
                case "water-to-light":
                    for s, d in one_to_one:
                        water_to_light[s] = d
                case "light-to-temperature":
                    for s, d in one_to_one:
                        light_to_temperature[s] = d
                case "temperature-to-humidity":
                    for s, d in one_to_one:
                        temperature_to_humidity[s] = d
                case "humidity-to-location":
                    for s, d in one_to_one:
                        humidity_to_location[s] = d

    all_location = []
    for s in seeds:
        value = get_value_of_index(soil_to_fertilizer, int(s))
        value = get_value_of_index(fertilizer_to_water, value)
        value = get_value_of_index(water_to_light, value)
        value = get_value_of_index(light_to_temperature, value)
        value = get_value_of_index(temperature_to_humidity, value)
        value = get_value_of_index(humidity_to_location, value)
        all_location.append(value)

    print(all_location)
    print(min(all_location))



