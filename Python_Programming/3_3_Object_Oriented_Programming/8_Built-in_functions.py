#issubclass() and isinstance() are built-in functions in Python that are used to check class relationships and object types, 
#respectively. issubclass() checks if a class is a subclass of another class, while isinstance() checks if an object is an 
# instance of a specific class or a subclass thereof.

#ssubclass(class A, class B) 
# Returns True if class A is a subclass of class B, and False otherwise. 
# It checks the inheritance relationship between two classes.

class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()

print(issubclass(A,B))
print(issubclass(B,A))

#Example of isinstance() that determines if some object is an instance of some class

class A:
	pass
class B(A):
	pass

b = B()
print(isinstance(b,B))
print(isinstance(b,A))

#The super() function is a built-in function that can be called inside the derived class and gives access to the methods and 
# variables of the parent classes or sibling classes. Sibling classes are the classes that share the same parent class. 
# When you call the super() function, you get an object that represents the parent class in return.

class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()

