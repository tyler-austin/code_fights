import re


def variable_name(name):
    if name[0].isdigit():
        return False
    if re.match('^[A-Za-z0-9_]*$', name):
        return True
    return False
