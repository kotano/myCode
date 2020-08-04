def find_index(search, iterable):
    for index, element in enumerate(iterable):
        if element == search:
            break
    else:
        index = None
    return index


# master
def m_find_index(value, items):
    for index, item in enumerate(items):
        if item == value:
            return index


print(m_find_index(42, [1, 2, 3]))

# both examples are good for reference
