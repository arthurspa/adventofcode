from io import TextIOWrapper

"""
--- Part Two ---

Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?

"""


def solve(input):
    ranges = []
    layers = []
    reading_layer = False
    layer_id = -1
    for line in input:
        if "seeds" in line:
            values = [int(x) for x in line.split(":")[1].strip().split(" ")]
            for i in range(len(values)):
                if (i + 1) % 2 == 0:
                    ranges.append([values[i - 1], values[i]])

        if line.strip() == "":
            reading_layer = False
            continue

        if "map" in line:
            reading_layer = True
            layer_id += 1
            layers.append([])
            continue

        if reading_layer:
            map = [int(x) for x in line.split(" ")]
            layers[layer_id].append(map)

    for layer in layers:
        layer.sort()

        # add missing ranges
        to_append = []
        for i in range(len(layer) - 1):
            next_start = layer[i][0] + layer[i][2]
            if layer[i + 1][0] != next_start:
                to_append.append([next_start, next_start, layer[i + 1][0]])

        layer.extend(to_append)
        layer.sort()
        if layer[0][0] != 0:
            layer.append([0, 0, layer[0][0]])

        layer.sort()
        ranges = process(layer, ranges)

    min = 999999999999999999999999999999
    for r in ranges:
        if r[0] < min:
            min = r[0]

    # final answer 31161857
    print(min)


def process(layer, ranges):
    next_layer_ranges = []
    for src_range in ranges:
        map_found = False
        for map in layer:
            src_range_map = map[1:]
            overlaping_src_range = get_overlapping_range(src_range_map, src_range)
            if overlaping_src_range:
                map_found = True
                map_dest_start = map[0]
                map_src_start = map[1]
                overlap_dest_start = (
                    map_dest_start + overlaping_src_range[0] - map_src_start
                )
                overlap_dest_length = overlaping_src_range[1]
                next_layer_ranges.append([overlap_dest_start, overlap_dest_length])

        if not map_found:
            next_layer_ranges.append(src_range)

    return next_layer_ranges


def get_overlapping_range(range_a, range_b):
    a_start = range_a[0]
    a_length = range_a[1]
    a_end = a_start + a_length
    b_start = range_b[0]
    b_length = range_b[1]
    b_end = b_start + b_length

    if a_start >= b_end or a_end <= b_start:
        return None

    start = a_start
    if a_start < b_start:
        start = b_start

    end = a_end
    if a_end > b_end:
        end = b_end

    return [start, end - start]
