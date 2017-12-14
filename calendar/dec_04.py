from christmas_tree import tree
from util.read_file import read_file_to_string


def part1(passphrase: str):
    """
A valid passphrase must contain no duplicate words
    :return no of valid passphrases:
    """
    list_of_passphrases = passphrase.splitlines(keepends=False)
    no_of_valid_phrases = 0
    for phrase in list_of_passphrases:
        list_of_words = phrase.split(sep=' ')
        if len(list_of_words) - len(set(list_of_words)) == 0:
            no_of_valid_phrases += 1
    return no_of_valid_phrases


def part1_test():
    assert part1('aa bb cc dd ee') == 1
    assert part1('aa bb cc dd aa') == 0
    assert part1('aa bb cc dd aaa') == 1
    assert part1('aa bb cc dd aaa\naa bb cc dd aa\naa bb cc dd aaa') == 2


def part2(passphrase):
    """
A passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.
    :return no of valid passphrases:
    """
    list_of_passphrases = passphrase.splitlines()
    no_of_valid_phrases = 0
    for phrase in list_of_passphrases:
        list_of_words = phrase.split(sep=' ')
        list_of_uniqe_words = list(set(list_of_words))
        list_of_uniqe_words_flipped = reversed(list_of_uniqe_words)
        print(list_of_uniqe_words_flipped)
        no_of_valid_phrases += 1
    return no_of_valid_phrases


def part2_test():
    assert part2('abcde fghij') == 1


print(tree)
print('### Part 1 ###')
part1_test()
print('Resultat: ' + str(part1(read_file_to_string('dec_04_passphrases.txt', with_lines=True))))

print('### Part 2 ###')
part2_test()
print('Resultat: ' + str(part2("")))
