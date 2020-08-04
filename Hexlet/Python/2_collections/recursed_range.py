def get_range1(limit):
    def inner(counter, accumulator):
        if counter < limit:
            # конкатенация списков порождает новый список
            return inner(counter + 1, accumulator + [counter])
        return accumulator
    return inner(0, [])


def get_range2(limit):
    range = []

    def inner(counter):
        if counter < limit:
            range.append(counter)
            return inner(counter + 1)
    inner(0)
    return range


def test():
    print(get_range1(limit=-1))
    print(get_range1(limit=0))
    print(get_range1(limit=1))
    print(get_range1(limit=5))
    print(get_range2(limit=-1))
    print(get_range2(limit=0))
    print(get_range2(limit=1))
    print(get_range2(limit=5))


if __name__ == "__main__":
    test()
