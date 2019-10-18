class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Pesho', 'Petrov', 400)
emp_2 = Employee('Gosho', 'Goshev', 250)

print(emp_1.email)
print(emp_2.email)
