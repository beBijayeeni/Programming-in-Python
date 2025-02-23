from abc import ABC
class Employee(ABC):
    name=""
    city=""
    salary=0
    def getvalues(self,name,city,salary):
        self.name=name
        self.city=city
        self.salary=salary
    def display(self):
        print("Employee Details")
    def detaiis(self):
        pass
class Name(Employee):
    def detaiis(self):
        print("My name is:",self.name)
class City(Employee):
    def detaiis(self):
        print("My city is:",self.city)
class Salary(Employee):
    def detaiis(self):
        print("My salary is:",self.salary)
e=Employee()
e.display()
n=Name()
n.name="Pankaj"
n.detaiis()
c=City()
c.city="Delhi"
c.detaiis()
s=Salary()
s.salary=55000
s.detaiis()