class Person:

    def metod1(self, a, b, c):
        self.var1 = a
        self.var2 = b
        self.var3 = c


class Employee(Person):
    pass


def main():

    obj1 = Person()
    obj2 = Employee()

    obj1.metod1(1, 2, 3)
    print(obj1.var1, obj1.var2, obj1.var3)

    obj2.metod1(5, 6, 7)
    print(obj2.var1, obj2.var2, obj2.var3)


if __name__ == '__main__':
    main()
