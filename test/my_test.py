def find_number(array, number):
    result = []
    for index in range(len(array)):
        for element in array[index + 1:]:
            if number == array[index] + element:
                result.append((array[index], element))

    if len(result) > 0:
        return True
    else:
        return False


# print(find_number([1, 2, 3, 4], 9))


def check_sum_of_four_numbers(data, target):
    result = []
    for i in range(len(data)):
        for idx, val in enumerate(data[i + 1:]):
            for idz, value in enumerate(data[idx + i + 2:]):
                for z in data[idx + i + idz + 3:]:
                    if target == data[i] + val + z + value:
                        result.append((data[i], val, z, value))

    if len(result) > 0:
        print(result)
        return True
    else:
        return False


# print(check_sum_of_four_numbers([1, 2, 3, 4, 5, 6, 7, 8], 15))

def my_args_and_kwargs(*args, **kwargs):
    for i in args:
        print(i)
    print('===')
    for i, j in kwargs.items():
        print(i, j)


my_args_and_kwargs('asd', 1, 'gh', client="John", sketch="Cheese Shop Sketch")


# def fib(n):
#     print(0)
#     a, b = 1, 1
#
#     while n:
#         yield a
#         a, b = b, a + b
#         n -= 1
#
#
# for f in fib(5):
#     print(f)


def get_kangaroo(size):
    print(size)  # 50

    def get_baby_kangaroo():
        size = 10
        print(size)  # 10

    get_baby_kangaroo()
    print(size)  # 50


get_kangaroo(50)
