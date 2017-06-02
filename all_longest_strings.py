def all_longest_strings(in_array: list):
    longest_len = _longest_string_size(in_array)
    result = list()
    for s in in_array:
        if len(s) == longest_len:
            result.append(s)
    return result


def _longest_string_size(in_array):
    longest_len = 0
    for s in in_array:
        s_len = len(s)
        if s_len > longest_len:
            longest_len = s_len
    return longest_len


if __name__ == '__main__':

    input_array = ["aba", "aa", "ad", "vcd", "aba"]

    print(all_longest_strings(input_array))
