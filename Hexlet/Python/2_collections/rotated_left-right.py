def rotated_left(itr):
    return itr[1:] + itr[:1]


def rotated_right(itr):
    return itr[-1:] + itr[:-1]


if __name__ == "__main__":
    itr = [1, 2, 3, 4]
    print(rotated_left(itr))
    print(rotated_right(itr))
