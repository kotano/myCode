from points import get_quadrant, make_decart_point, get_x, get_y


def make_rectangle(start_point, width, height):
    def make_decart_point(x, y):
        return {'x': x, 'y': y, }
    if isinstance(start_point, dict):   # had to use it because of wrong
        start_point = start_point['x'], start_point['y']          # type

    return {
        'start_point': make_decart_point(*start_point),
        'width': width,
        'height': height,
        'a': make_decart_point(*start_point),
        'b': make_decart_point(start_point[0]+width, start_point[1]),
        'c': make_decart_point(start_point[0]+width, start_point[1]-height),
        'd': make_decart_point(start_point[0], start_point[1]-height),
    }


def get_start_point(rectangle):
    return rectangle['start_point']


def get_width(rectangle):
    return rectangle['width']


def get_height(rectangle):
    return rectangle['height']


def contains_origin(rectangle):
    a = get_quadrant(rectangle['a'])
    b = get_quadrant(rectangle['b'])
    c = get_quadrant(rectangle['c'])
    d = get_quadrant(rectangle['d'])
    return len({a, b, c, d}) == 4


def test_rectangle():
    point = make_decart_point(0, 1)
    rectangle = make_rectangle(point, 4, 5)
    print(contains_origin(rectangle) is False)

    p = make_decart_point(-4, 3)
    rectangle1 = make_rectangle(p, 5, 4)
    print(contains_origin(rectangle1) is True)

    rectangle2 = make_rectangle(p, 5, 2)
    print(contains_origin(rectangle2) is False)

    rectangle3 = make_rectangle(p, 2, 2)
    print(contains_origin(rectangle3) is False)

    rectangle4 = make_rectangle(p, 4, 3)
    print(contains_origin(rectangle4) is False)


if __name__ == "__main__":
    test_rectangle()


# # #
# MASTER BEGIN
def m_make_rectangle(point, width, height):
    return {
        "point": point,
        "width": width,
        "height": height,
    }


def m_get_start_point(rectangle):
    return rectangle['point']


def m_get_width(rectangle):
    return rectangle['width']


def m_get_height(rectangle):
    return rectangle['height']


def m_contains_origin(rectangle):
    point1 = get_start_point(rectangle)
    point2 = make_decart_point(
        get_x(point1) + get_width(rectangle),
        get_y(point1) - get_height(rectangle),
    )

    return get_quadrant(point1) == 2 and get_quadrant(point2) == 4
# END
