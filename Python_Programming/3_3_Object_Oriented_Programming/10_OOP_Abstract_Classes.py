#1 Abstract classes are classes that cannot be instantiated and are meant to be subclassed. They can contain abstract methods, 
# which are methods that are declared but not implemented in the abstract class. The child classes that inherit from the abstract 
# class must implement the abstract methods.

#2 Example of abstract class and method
'''
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self):
        pass

class CardPayment(Payment):
    def process(self):
        return "card processed"

try:
    base_payment = Payment()
    print("base created")
except TypeError:
    card = CardPayment()
    print(card.process())
'''
#This hits a Type Error because we cannot instantiate an object of an abstract class. 
# We can only instantiate objects of the child class that implements the abstract method of the 
# parent class. However, we can instantiate the child class.

#3
'''
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    pass

class Square(Shape):
    def area(self):
        return 25

try:
    c = Circle()
    print("Circle created")
except TypeError:
    print("Circle error")

s = Square()
print("Square area is", s.area()) 
'''
#This throws a Type Error because the Circle class does not implement the abstract method area() 
# of the Shape class. But the Square class implements the area() method and hence we can create an 
# object of the Square class and call the area() method over it.

#4
'''
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class RectangleBase(Shape):
    def area(self):
        return 20

class Rectangle(RectangleBase):
    def perimeter(self):
        return 18

print(isinstance(Shape, ABC))
print(isinstance(RectangleBase, ABC))
obj = Rectangle()
print(obj.area())
print(obj.perimeter())
'''
#Shape and RectangleBase are abstract classes and not instances of ABC.

#5

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def donate(self):
        pass

class Donation(Employee):
    def donate(self):
        return 50

alice = Donation()
bob = Donation()

amounts = []
amounts.append(alice.donate())
amounts.append(bob.donate())

print(amounts)

'''
#6
#Here Child Class overrides the abstract method of the Parent Class and implements it. 
# Hence we can create an object of the Child Class and call the method over it.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

c = Circle()
c.draw()

#7 A complete example of abstract classes and methods and how they can be used to enforce a 
# certain structure in the child classes.

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def describe_role(self):
        pass

class Manager(Employee):
    def describe_role(self):
        print("Manages team")

class Developer(Employee):
    def describe_role(self):
        print("Writes code")

boss = Manager()
engineer = Developer()

boss.describe_role()
engineer.describe_role()
'''