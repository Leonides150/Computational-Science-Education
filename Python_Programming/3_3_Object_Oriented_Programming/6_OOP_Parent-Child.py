#Demonstrates usage of Parent-Child Class, Inheritance

#Basic example of Parent-Child class, Inheritance
class A:
    def __init__(self):
        self.val = 7
class B(A):
    pass

b = B()
print(b.val)

#Example2: Parent-Child class, Inheritance with constructor and method

class Employees:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last
    
class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days?"
    
adrian = Supervisors("Adrian", "A", "apple")

emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")      

print(emily.leave_request(3))
print(adrian.password)
print(emily.name)

#Example 3: Parent-Child class, Inheritance with constructor and method

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days?"

li = Chefs("Li", "L")

print(li.leave_request(5))

#2
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

class Manager(Employee):
    def __init__(self, first, last, code):
        super().__init__(first, last)
        self.code = code

class Developer(Employee):
    def task_report(self, count):
        return "completed " + str(count) + " tasks"

maria = Manager("Maria", "Lopez", "ZX9")
li = Developer("Li", "Chen")

print(li.task_report(4), maria.first, maria.code)


#Example 4: Parent-Child class, Inheritance with constructor and method

class Employee:
    def __init__(self, name, last):
        self.name = name
        self.last = last

class Manager(Employee):
    def __init__(self, name, last, code):
        super().__init__(name, last)
        self.code = code

maria = Manager("Maria", "M", "blue123")

print(maria.code)

#Example 5: Parent-Child class, Inheritance with constructor and method

class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels


class Car(Vehicle):
    def __init__(self, brand, wheels, doors):
        #super().__init__(brand, wheels)
        self.brand = brand
        self.wheels = wheels
        self.doors = doors


bike = Vehicle("Roadster", 2)
sedan = Car("FamilyCar", 4, 4)

print(bike.brand, bike.wheels, sedan.brand, sedan.wheels, sedan.doors)

