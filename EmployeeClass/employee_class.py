from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def calculate_salary(self):
        return 20_000

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 70_000

class ContractEmployee(Employee):
    def calculate_salary(self):
        return 30_000

i = Intern()
print(i.calculate_salary())

f = FullTimeEmployee()
print(f.calculate_salary())

c = ContractEmployee()
print(c.calculate_salary())
