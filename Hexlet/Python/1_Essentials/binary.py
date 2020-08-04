# BEGIN (write your solution here)
def binary(number):
    try:
        number = int(number)
    except ValueError:
        print("Нужно ввести число..")
    else:
        res = []
        if not number:
            return '0'
        while number:   
            modulo = number % 2
            res.append(str(modulo))
            number = number // 2
            if number == 0:
                return ''.join(res)[::-1]


# while True:
#     print(binary(input('Введите число для представления в бинарный вид: ')) or '0')
