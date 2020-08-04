from functools import wraps


# BEGIN (write your solution here)
def suppress(exceptions, *, or_return=None):
    def wrapper(function):

        @wraps(function)
        def inner(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except exceptions:
                return or_return

        return inner

    return wrapper


# END
try:
    res = 5 / 0
except Exception as e:
    print(e)


def walk(path, structure):
    """Walk down to structure using path."""
    if not path:
        return structure
    key, *rest_path = path
    return walk(rest_path, structure[key])


def test_walk():
    print(walk([0], 'Cat') == 'C')
    print(walk(['a', 1], {'a': ('foo', 'bar')}) == 'bar')
    print(walk(['x', 1, 0], {'x': ('foo', 'bar')}) == 'b')


def test_suppress():
    @suppress(ZeroDivisionError, or_return=0)
    def safe_div(a, b):
        return a // b

    print(safe_div(10, 3) == 3)
    print(safe_div(10, 0) == 0)


def test_suppress_walk():
    safe_walk = suppress((KeyError, IndexError))(walk)

    print(safe_walk([1], "") is None)
    print(safe_walk(['a'], {}) is None)
    print(safe_walk([0, 0, 1], (("?", 100), 200)) is None)


if __name__ == "__main__":
    # walk()
    test_walk()
    test_suppress_walk()
    test_suppress()
