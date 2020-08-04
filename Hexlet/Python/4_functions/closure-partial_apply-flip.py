# BEGIN
from operator import add, mul


def partial_apply(function, *args):

    def inner(*second_arg):
        argums = args + second_arg
        return function(*argums)

    return inner


def flip(function):

    def inner(*args):
        flipped = args[::-1]
        return function(*flipped)

    return inner


def m_partial_apply(function, arg1):
    def inner(arg2):
        return function(arg1, arg2)
    return inner


def m_flip(function):
    def inner(arg1, arg2):
        return function(arg2, arg1)
    return inner
# END


def test():
    def test_partial_apply():
        print(list(
            map(partial_apply(add, 10), [1, 2, 3]),  # noqa: WPS221
        ) == [11, 12, 13])

        print(list(
            map(partial_apply(mul, '*'), [2, 3, 4]),  # noqa: WPS221
        ) == [
            '**',
            '***',
            '****',
        ])

    def test_flip():
        assert flip(mul)(3, '*') == '***'

    def test_both():
        assert list(
            map(partial_apply(flip(mul), 5), "!?&"),
        ) == [
            '!!!!!',
            '?????',
            '&&&&&',
        ]

        test_partial_apply()
        test_flip
        test_both()


# JUST EXAMPLES NOT FOR USE
def examples():

    # no closure
    printers = []
    for i in range(10):
        def printer():
            print(i)
        printers.append(printer)
    printers[0]()
    printers[5]()
    printers[9]()
    i = 42
    printers[0]()

    # with closure
    printers = []
    for i in range(10):
        def make_printer(arg):
            def printer():
                print(arg)
            return printer
        p = make_printer(i)
        printers.append(p)
    printers[0]()
    printers[5]()

    def make_closure():
        y = 1

        def inner(x):
            return x + y
        y = 42
        return inner

    make_closure()(100)
