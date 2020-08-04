def make_decart_point(x, y):
    return {'x': x, 'y': y, }


def make_segment(point1, point2):
    return {'point1': point1, 'point2': point2, }


def get_mid_point_of_segment(segment):
    pnt1 = segment['point1']
    pnt2 = segment['point2']
    return {
        'x': (pnt1['x'] + pnt2['x']) / 2,
        'y': (pnt1['y'] + pnt2['y']) / 2,
    }


# BEGIN
# def m_make_segment(point1, point2):
#     return {"begin_point": point1, "end_point": point2}


# def m_get_begin_point(segment):
#     return segment["begin_point"]


# def m_get_end_point(segment):
#     return segment["end_point"]


# def m_get_mid_point_of_segment(segment):
#     begin_point = get_begin_point(segment)
#     end_point = get_end_point(segment)

#     x = (get_x(begin_point) + get_x(end_point)) / 2
#     y = (get_y(begin_point) + get_y(end_point)) / 2

#     return make_decart_point(x, y)
# END
