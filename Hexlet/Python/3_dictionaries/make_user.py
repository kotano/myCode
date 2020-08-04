def make_user(name, age):
    return {'name': name, 'age': age}


def format_user(dic):
    # return f'{dic["name"]}, {dic["age"]}'
    # return dic["name"]+', ' + str(dic["age"])
    return '{}, {}'.format(dic['name'], dic['age'])


if __name__ == "__main__":
    phil = make_user('Phil', 25)
    print(format_user(phil))
