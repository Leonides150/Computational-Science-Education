#1 Multiple Inheritance

class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)

#2 Multiple Inheritance with constructor and method
class A:
   def __init__(self):
       self.a = 1
class B:
   def __init__(self):
       self.b = 2
class C(A, B):
   def __init__(self):
       A.__init__(self)
       B.__init__(self)
c = C()
print(c.a, c.b)

#3 Multi-level Inheritance
#The output is 2 because C derives from the immediate super class of C, and that's B. Even though class A is the top-level base 
# class, class C does not directly inherit from A but instead inherits the attribute a from B and B has the attribute value of 
# its member a = 2.
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)

#4 Multi-level Inheritance with constructor and method
class A:
   def __init__(self):
       self.a = 1
class B(A):
   def __init__(self):
       A.__init__(self)
       self.a = 2
class C(B):
   def __init__(self):
       B.__init__(self)
c = C()
print(c.a)
