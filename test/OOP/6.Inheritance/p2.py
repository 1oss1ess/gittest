class Person:
    pass


class Employee(Person):
    pass


def main():
    print(issubclass(Employee, Person))


if __name__ == '__main__':
    main()
