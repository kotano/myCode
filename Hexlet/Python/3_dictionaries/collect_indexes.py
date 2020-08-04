# MASTER BEGIN
from collections import defaultdict


def m_collect_indexes(items):
    result = defaultdict(list)
    for index, item in enumerate(items):
        result[item].append(index)
    return result
# END


def collect_indexes(iterable):
    dic = {}
    for index, element in enumerate(iterable):
        dic.setdefault(element, []).append(index)
    return dic


if __name__ == "__main__":
    print(collect_indexes([]) == {})
    print(collect_indexes([1]) == {1: [0]})
    print(collect_indexes([1, 2]) == {1: [0], 2: [1]})
    print(collect_indexes('lol') == {'l': [0, 2], 'o': [1]})
    print(collect_indexes('coco') == {'c': [0, 2], 'o': [1, 3]})
