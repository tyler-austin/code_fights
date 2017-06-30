import re


def first_digit(input_string: str):
    return re.search(r'\d', input_string).group()
