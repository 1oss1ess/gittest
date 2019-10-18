class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Pesho', 'Petrov', 400)
emp_2 = Employee('Gosho', 'Goshev', 250)

emp_str_1 = 'John-Doe-300'
emp_str_2 = 'Steve-Smith-220'
emp_str_3 = 'Jane_Doe-900'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime

my_date = datetime.date(2018, 4, 5)
print(Employee.is_workday(my_date))
