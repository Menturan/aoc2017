def read_file_to_string(filename, with_lines=False):
    with open('../puzzle_input/' + filename) as f:
        text = f.read()
        if not with_lines:
            text = text.replace('\n', '')
        return text


def read_file_to_list(filename):
    with open('../puzzle_input/' + filename) as f:
        return f.read().splitlines()
