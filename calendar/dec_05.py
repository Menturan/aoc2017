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
                position += jumps[position]
                jumps[position] += 1
                no_of_jumps += 1
        except IndexError:
            no_of_jumps += 1
            break
    return no_of_jumps


def part1_test():
    test1 = part1([0, 3, 0, 1, -3])
    assert test1 == 5, 'Returnerade inte 5 var {}.'.format(test1)



def part2(input) -> int:
    """
Puzzle
    :return sum:
    """

    pass


def part2_test():
    pass


print(tree)
print('### Part 1 ###')
part1_test()
print('Resultat: ' + str(part1(read_file_to_list_of_numbers('dec_05_jumps.txt'))))
print('### Part 2 ###')
part2_test()
print('Resultat: ' + str(part2("")))
