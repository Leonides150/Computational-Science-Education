#Tuples are immutable sequences in Python, meaning that once a tuple is created, its elements cannot be changed. 
# They are defined using parentheses () and can contain elements of different data types.

my_tuple = (1, 'string', 3.14, [1, 2, 3], True)
print(my_tuple[0]) #Accessing the first element of the tuple
print(type(my_tuple)) #Checking the type of the variable
print(my_tuple.index('string')) #Finding the index of an element in the tuple
print(my_tuple.count(1)) #Counting the occurrences of an element in the tuple

for x in my_tuple:
    print("Value:", x)

