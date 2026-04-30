#1 Basic class definition
'''
class MyClass():
    #pass
    print("Hello. This is a class")
myclass = MyClass()
#print(type(myclass))
'''
#2 Class with attributes and methods
'''
class MyClass():
    a = 5
myc = MyClass()
print(myc.a)
'''

#3 Class with methods
#The keyword self is used to refer to the instance of the class. #It allows us to access the methods of the class. 
#It is used to differentiate between the instance variables and the local variables in the method.
'''
class MyClass():
    a = 5
    def hello(self):
        print("Hello. This is a method in MyClass")
myc = MyClass()
print(myc.a)
myc.hello()
'''

#4 Class with methods and attributes
class House:
    
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self, rate):
        # Functionality to calculate the costs from the area of the house
        cost = rate * self.num_rooms
        return cost



house = House()
print(house.num_rooms)
print(House.num_rooms)
house.num_rooms = 7
# House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)
