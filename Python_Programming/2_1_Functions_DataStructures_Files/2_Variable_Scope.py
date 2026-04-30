# Four types of variable scopes in Python:
# 1. Local Scope: Variables defined inside a function are in the local scope and can only be accessed within that function.
'''
def get_total(a, b):
    #local variable declared inside a function
    total = a + b;
    return total

print(get_total(5, 2))
7

# Accessing variable outside of the function:
print(total)
'''

# 2. Enclosed Scope: Variables defined in an enclosing function can be accessed by inner functions, but not by the global scope.
'''
def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        number = total * 2
        print(number)

    double_it()
    #number variable will not be accessible
    #print(number)
    return total
get_total(5, 2)
'''

# 3. Global Scope: Variables defined at the top level of a script or module are in the global scope and can be accessed from 
# anywhere in the code.
'''
special = 5

def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        #local variable
        double = total * 2
        print(special)

    double_it()
    return total
get_total(5,2)
'''

# 4. Built-in Scope: This scope contains built-in functions and exceptions that are always available in Python.
'''
global_var = 10

def my_func_1():
    enclosed_var = 8

    def my_func_2():
        local_var = 5
        print('Global variable:', global_var)  # Accessing global variable
        print('Enclosed variable:', enclosed_var)  # Accessing enclosed variable
        print('Local variable:', local_var)  # Accessing local variable
    my_func_2()

#print(enclosed_var)  # This will raise an error because enclosed_var is not defined in the global scope
#print(local_var)  # This will raise an error because local_var is not defined in the global scope
'''
