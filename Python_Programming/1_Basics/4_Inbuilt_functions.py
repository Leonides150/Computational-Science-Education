#Print function is used to print the output on the console.
print("Hello")

#Input function is used to take input from the user.
'''
print("Where do you live?")
location = input()
print("So you live in " + location)
'''

#Len() function is used to find the length of a string, list, tuple, etc.
print(len("Hello"))

#str() function is used to convert a value to a string.
print(str(55) + str(2))
print(55+2)

#int() function is used to convert a value to an integer.
print(int(75.3))
print(int('123'))

#float() function is used to convert a value to a floating-point number.
some_int = 10
print(float(some_int))


#User-defined functions are defined using the def keyword in Python.
def say_hello():
    print("Hello there!")
say_hello()

def say_hello(you):
    print("Hello " + you)
say_hello("Arav")

