def count_all(iterable):
    dic = {}
    for element in iterable:
        if element in dic:
            dic[element] += 1
        else:
            dic[element] = 1
    return dic


# Master
def m_count_all(items):
    counters = {}
    for item in items:
        counters[item] = counters.get(item, 0) + 1
    return counters
#


if __name__ == "__main__":
    animals = ['cat', 'dog', 'horse', 'cat']
    print(count_all(animals))
