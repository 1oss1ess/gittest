class Person:
    def assignbasic(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def assignemp(self, idno):
        self.idno = idno


class Programmer(Employee):
    def assignprog(self, lang):
        self.lang = lang


def main():
    obj1 = Programmer()
    obj1.assignbasic('Pesho', 22)
    obj1.assignemp(1002)
    obj1.assignprog('Python 3')
    print(obj1.name, obj1.age, obj1.idno, obj1.lang)


if __name__ == '__main__':
    main()
