# MRO stands for Method Resolution Order. It is the order in which Python looks for a method in a hierarchy of classes. 
# When we call a method on an object, Python first looks for the method in the class of the object. If it does not find it there, 
# it looks for it in the parent class, and so on, until it finds the method or reaches the end of the hierarchy.  

#Types of inheritance: Single Inheritance, Multiple Inheritance, Multilevel Inheritance, Hierarchical Inheritance and Hybrid 
# Inheritance.

#MRO says order of inheritance is bottom to top and left to right. So, if there are multiple classes in the inheritance hierarchy, 
# then the method is searched first in the class itself, then in the parent class, and so on, until it finds the method or reaches 
# the end of the hierarchy.

#Example
class A:
    num = 5
class B(A): 
    num = 10
class C(B):
    pass
print(C.num)
print(C.mro())
#print(help(C))
#The output is 10 because C derives from the immediate super class of C, and that's B. 
# Even though class A is the top-level base class, class C does not directly inherit from

# Example 1
class A:
   def a(self):
       return "Function inside A"

class B:
    def a(self):
        return "Function inside B"

class C(B,A):
    pass

# Driver code
c = C()
print(c.a())

#2
class A:
    def b(self):
        return "Function inside A"

class B:
    def b(self):
        return "Function inside B"

class C(A, B):
    #def b(self):
    #    return "Function inside C"
    pass

class D(C):
    pass

d = D()
print(d.b())

#3
'''
class A:
    def c(self):
        return "Function inside A"

class B:
    def c(self):
        return "Function inside B"

class C(A, B):
    def c(self):
        return "Function inside C"

class D(A, C):
    pass

d = D()
print(d.c())
#Throws error because of the ambiguity in the method resolution order (MRO) of class D.
'''
#4
class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d())
print(F.mro())

#5
class A:
    def b(self):
        return "Function inside A"

class B:
    pass

class C:
    def b(self):
        return "Function inside C"

class D(B, C, A):
    pass

class D(C):
    pass

d = D()
print(d.b(), 'here')
#The output is "Function inside C" because of the method resolution order (MRO) of class D. The MRO of class D is [D, C, A, B], 
# which means that when we call the method b() on an object of class D, Python first looks for the method in class D, then in 
# class C, then in class A, and finally in class B. Since class C has the method b(), it is called and the output is 
# "Function inside C".

#6
class A:
    def c(self):
        return "Function inside A"

class B(A):
    def c(self):
        return "Function inside B"

class C(A,B):
    pass

class D(C):
    pass

d = D()
print(d.c())
#Throws error because of the ambiguity in the method resolution order (MRO) of class D. The MRO of class D is [D, C, B, A], 
# which means that when we call the method c() on an object of class D, Python first looks for the method in class D, then in 
# class C, then in class B, and finally in class A. Since both class B and class A have the method c(), it is ambiguous which 
# method should be called and hence it throws an error.