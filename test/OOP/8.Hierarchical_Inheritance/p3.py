class A:
    def m(self):
        print('m() from A...')


class B:
    def m(self):
        print('m() from B...')


class C(A, B):
    def m(self):
        print('m() from C...')


def main():
    obj1 = C()
    obj1.m()


if __name__ == '__main__':
    main()
