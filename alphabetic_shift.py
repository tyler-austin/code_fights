def alphabetic_shift(input_string):
    return ''.join(chr((ord(char) - ord('a') + 1) % 26 + ord('a')) for char in input_string)
