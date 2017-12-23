from christmas_tree import tree
from util.read_file import read_file_to_list_of_numbers


def part1(jumps: list) -> int:
    """
Puzzle
    :return sum:
    """
    no_of_jumps = 0
    position = 0
    while True:
        try:
            if jumps[position] == 0:
                jumps[position] += 1
                no_of_jumps += 1
                continue
            else:
                value_at_current_position = jumps[position]
                jumps[position] += 1
                position += value_at_current_position
                no_of_jumps += 1
        except IndexError:
            break
    return no_of_jumps


def part1_test():
    test1 = part1([0, 3, 0, 1, -3])
    assert test1 == 5, 'Summan är inte 5 var {}.'.format(test1)


def part2(jumps) -> int:
    """
Puzzle
    :return sum:
    """
    no_of_jumps = 0
    position = 0
    while True:
        try:
            if jumps[position] == 0:
                jumps[position] += 1
                no_of_jumps += 1
                continue
            else:
                value_at_current_position = jumps[position]
                if value_at_current_position >= 3:
                    jumps[position] -= 1
                else:
                    jumps[position] += 1
                position += value_at_current_position
                no_of_jumps += 1
        except IndexError:
            break
    return no_of_jumps


def part2_test():
    test1 = part2([0, 3, 0, 1, -3])
    assert test1 == 10, 'Summan är inte 10 var {}.'.format(test1)


print(tree)
print('### Part 1 ###')
part1_test()
print('Resultat: ' + str(part1(read_file_to_list_of_numbers('dec_05_jumps.txt'))))
print('### Part 2 ###')
part2_test()
print('Resultat: ' + str(part2(read_file_to_list_of_numbers('dec_05_jumps.txt'))))
