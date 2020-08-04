from functools import reduce
from operator import getitem, truth, abs


def keep_truthful(iterable):
    def istrue(arg):
        if truth(arg):
            return arg

    res = map(istrue, iterable)
    return filter(bool, res)


def abs_sum(iterable):
    res = []
    for x in iterable:
        res.append(abs(x))
    return sum(res)


def walk(dic, iterable):
    li = list(iterable)
    back = dic.copy()
    path = list(back.keys())

    def inner(d):
        for k, v in d.items():
            if k == li[-1]:
                return v
            if isinstance(v, dict):
                return inner(v)
            else:
                prev = back.pop(path[-1])
                return inner(prev)

    return inner(back)


#Решение учителя
# BEGIN


def m_keep_truthful(items):
    return filter(truth, items)


def m_abs_sum(numbers):
    return sum(map(abs, numbers))


def m_walk(dictionary, path):
    return reduce(getitem, path, dictionary)

# test
if __name__ == "__main__":
    def test():
        print(list(keep_truthful([True, False, '', 'Foo'])))

    def test_walk():
        city = {
            'Pine': {
                '5': 'School #42',
            },
            'Elm': {
                '13': {
                    '1': 'Appartments #2, Elm st.13',
                },
            },
        }
        print(m_walk(city, ['Pine', '5'])) ##== city['Pine']['5'])
        path = ['Elm', '13', '1']
        print(m_walk(city, path)) ## == city['Elm']['13']['1'])

    test()
    test_walk()

