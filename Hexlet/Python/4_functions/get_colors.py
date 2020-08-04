def rgb(red=0, green=0, blue=0):
    return 'rgb({}, {}, {})'.format(red, green, blue)


def get_colors():
    return {
        'red': rgb(red=255),
        'green': rgb(green=255),
        'blue': rgb(blue=255),
    }
