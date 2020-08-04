from math import sqrt


def calculate_distance(p1, p2):
    lenx = abs(p1[0] - p2[0])
    leny = abs(p1[1] - p2[1])
    return sqrt(lenx**2 + leny**2)


# MASTER BEGIN
def m_calculate_distance(point1, point2):
    delta_x = point2[0] - point1[0]
    delta_y = point2[1] - point1[1]

    return sqrt((delta_x ** 2) + (delta_y ** 2))
# END
