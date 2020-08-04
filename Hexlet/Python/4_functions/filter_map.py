from math import sqrt


def filter_map(function, iterable):
    res = []
    for pair in (function(x) for x in iterable):  # for k, v in (f(x) ...
        if pair[0]:
            res.append(pair[1])
    return res


def m_filter_map(f, l):
    return [
        pair[1] for pair in (
            f(x) for x in l
        ) if pair[0]
    ]


def test_filter_map():
    def safe_sqrt(x):
        if x < 0:
            return False, 0
        return True, sqrt(x)

    print(filter_map(safe_sqrt, []) == [])
    print(filter_map(safe_sqrt, [4, -5, -2, 9]) == [2.0, 3.0])


if __name__ == "__main__":
    test_filter_map()
