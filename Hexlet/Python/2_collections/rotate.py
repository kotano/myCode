def rotate(lst):
    if lst:
        lst.insert(0, lst.pop())


example = [1, 2, 3]
rotate(example)
print(example)
