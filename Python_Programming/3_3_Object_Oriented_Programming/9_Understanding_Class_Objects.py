#Understanding Classes and statement execution via Objetcs and without them
'''
Algorithmically we can view the program consisting of the following:

1. Class definition of A     

    1.1 Constructor for A     

    1.2 Definition of local method alpha() 

2. Instantiating object a over class A 

3. Calling method alpha() over object of class A 

4. Class definition of B 

5. Constructor for B     

    5.1 Calling method alpha() over object of class A     

    5.2 Instantiating object a over class B *. 

Additional print statements distributed through the code.
'''  
'''
class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c

print(dir(A))
print("Instantiating A..")
a = A(1)
print(a.alpha())

class B:
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a

   print(a.alpha())
   d = 5
   print(d)
   print(a)

print("Instantiating B..")
b = B(a)
print(a)
'''

#Same code but with lines #13, 14, 21, 24, 27 and 28 commented out
# Note: Gives an error because of the print statements that are trying to access the method and 
# variable of class A without instantiating it.
# However, passing the object of class A to class B and then accessing the method and variable of 
# class A through that object works fine.

class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c

#print(dir(A))
print("Instantiating A..")
a = A(1)
print(a.alpha())

class B:
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a

   #print(a.alpha())
   d = 5
   print(d)
#   print(a)

print("Instantiating B..")
#b = B(a)
#print(a)

#Removing comment out from line 13 of the code makes it work fine
'''
Here are a few observations.

    When you try and print the ‘object’ of class A as in lines 21 and 28, you get the address of the object instead of the contents.

    Note how the address of object a is the same both inside class B and in the global scope of the program. It remains the same irrespective of from where it is called.

    The alpha() function is called twice in the program, but you still get the output as 2 every time and not 3. That's because the value is updated only temporarily and not assigned to anything.
    '''