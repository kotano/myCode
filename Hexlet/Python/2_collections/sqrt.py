import math


def get_square_roots(num):
    if num < 0:
        return []
    elif num:
        root = math.sqrt(num)
        return [-root, root]
    return [0]


def get_range(num):
    res = []
    # if num <= 0:
    #     return res
    # elif num > 0:
    while len(res) < num:
        res.append(len(res))
    return res


# factorial recursive example
def fact(num):
    if num == 0:
        return 1
    elif num < 0:
        return 0
    else:
        return fact(num - 1) * num


# {  Using recursive !need to rebuild
RES = []


def get_range2(num):
    RES.append(num-1)
    if num == 1:
        return sorted(RES)
    elif num > 1:
        return get_range2(num-1)
    else:
        return []
# }


#  => rebuilded =>
def get_range_recursively(num):
    res = []
    if num <= 0:
        return []
    elif num > 0:
        def recursion(num):
            if num == 0:
                return sorted(res)
            else:
                res.append(num-1)
                return recursion(num-1)
        return recursion(num)


def recursive(arg):
    print(arg, get_range_recursively(arg), 'getrange_recursively')
    print(str(arg)+'!', fact(arg), 'factorial recursive')


if __name__ == "__main__":
    # print(get_square_roots(-1))
    print(get_range(5))
    recursive(arg=-1)
    recursive(arg=0)
    recursive(arg=1)
    recursive(arg=2)
    recursive(arg=5)
