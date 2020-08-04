import math


def get_square_roots(argument):
    if argument < 0:
        return []
    elif argument:
        root = math.sqrt(argument)
        return [-root, root]
    return [0]


def get_range(up_to):
    result = []
    counter = 0
    while counter < up_to:
        result.append(counter)
        counter += 1
    return result
