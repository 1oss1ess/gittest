# Python Object-Oriented Programming


class Employee:

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)


emp_1 = Employee('Pesho', 'Petrov', 400)
emp_2 = Employee('Gosho', 'Goshev', 250)
print(emp_1.fullname())
print(Employee.fullname(emp_2))
