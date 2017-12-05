from christmas_tree import tree


def manhattan_distance(start, end):
    sx, sy = start
    ex, ey = end
    return abs(ex - sx) + abs(ey - sy)


def part1():
    """
Puzzle
    :return sum:
    """
    steps = 0
    value = 1
    matrix = [[value]]
    number_of_rings = 300
    searched_number = 1024  # 347991
    for i in range(1, number_of_rings):
        numbers_in_ring = 8 * i
        ring = []
        matrix.append(ring)
        for n in range(0, numbers_in_ring):
            value += 1
            ring.append(value)
    for ring_number, ring in enumerate(matrix, start=1):
        if searched_number in ring:
            ring_sides = list(zip(*[iter(ring)] * int((len(ring) / 4))))
            for side in ring_sides:
                if searched_number in side:
                    position_of_value_in_side = side.index(searched_number)
                    middle_idx_of_ring = int(len(side) / 2)
                    steps_from_searched_value_to_middle_of_ring = abs(position_of_value_in_side - middle_idx_of_ring)
                    steps = ring_number + steps_from_searched_value_to_middle_of_ring  # manhattan_distance((0, 0), (position_of_value_in_side, ring_number))
    return steps


def part2():
    """
Puzzle
    :return sum:
    """
    pass


print(tree)
print('### Part 1 ###')
print('NOT FINISHED!')
print('Resultat: ' + str(part1()))
print('### Part 2 ###')
print('Resultat: ' + str(part2()))
