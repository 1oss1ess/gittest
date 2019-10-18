class A:
    def m(self):
        print('m() from class A...')


class B(A):
    def m(self):
        print('m() from class B...')
        super().m()


class C(A):
    def m(self):
        print('m() from class C...')
        super().m()


class D(B, C):
    def m(self):
        print('m() from class D...')
        super().m()


def main():
    obj1 = D()
    obj1.m()


if __name__ == '__main__':
    main()
