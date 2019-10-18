class Class01:
    def __init__(self):
        print('Created an Object for class01')


class Class02:
    def __init__(self):
        print('Created an Object for class02')


def main():
    c1 = Class01()
    c2 = Class02()


if __name__ == '__main__':
    print('run directly...')
    main()
else:
    print('run the current module...')
