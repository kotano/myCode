def find_index(value, items):
    for index, item in (enumerate(items)):
        if item == value:
            return index


# BEGIN (write your solution here)
def find_second_index(value, items):
    iterator = iter(items)
    first = find_index(value, iterator)
    second = find_index(value, iterator)
    if second == 0 or second:
        return second + first + 1

# END


def test():
    print(find_second_index('!', '') is None)
    print(find_second_index('!', '!') is None)
    print(find_second_index('n', 'clone') is None)
    print(find_second_index('n', 'banana') == 4)
    print(find_second_index('n', 'cannon') == 3)


if __name__ == "__main__":
    test()
