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


def sort_chars_in_words(list_of_words):
    list_of_char_sorted_words = []
    for word in list_of_words:
        list_of_chars = list(word)
        list_of_chars.sort()
        char_sorted_word = ''.join(list_of_chars)
        list_of_char_sorted_words.append(char_sorted_word)
    return list_of_char_sorted_words


def part2(passphrase):
    """
A passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.
    :return no of valid passphrases:
    """
    list_of_passphrases = passphrase.splitlines()
    no_of_valid_phrases = 0
    for phrase in list_of_passphrases:
        list_of_words_in_phrase = phrase.split(sep=' ')
        list_of_words_in_phrase_sorted = sort_chars_in_words(list_of_words_in_phrase)
        if (len(list_of_words_in_phrase) - len(set(list_of_words_in_phrase_sorted))) == 0:
            no_of_valid_phrases += 1
    return no_of_valid_phrases


def part2_test():
    assert part2('abcde fghij') == 1
    assert part2('abcde xyz ecdab') == 0
    assert part2('a ab abc abd abf abj') == 1
    assert part2('iiii oiii ooii oooi oooo') == 1
    assert part2('oiii ioii iioi iiio') == 0
    assert part2('oiii ioii iioi iiio\niiii oiii ooii oooi oooo\niiii oiii ooii oooi oooo') == 2


print(tree)
print('### Part 1 ###')
part1_test()
puzzel_input = read_file_to_string('dec_04_passphrases.txt', with_lines=True)
print('Resultat: ' + str(part1(puzzel_input)))

print('### Part 2 ###')
part2_test()
print('Resultat: ' + str(part2(puzzel_input)))
