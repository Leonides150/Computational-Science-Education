#1 Numeric

a = 10
print(type(a))

a = 3.14
print(type(a))

a= 1 + 2j
print(type(a))

#2 Sequence

a = "Hello, World!"
print(type(a))

a = [1, 2, 3, 4, 5]
print(type(a))
a = [1, "hello", 3.5, "A", 5+2j]
print(type(a))

a = (1, 2, 3, 4, 5)
print(type(a))
a = (1, "hello", 3.5, "A", 5+2j)
print(type(a))

#3 Dictionaries
a = {"name": "Arav", "age": 30, "city": "New Delhi"}
print(type(a))

b = {1: "Item No.", 2: "Item Name", 3: "Item Price"}
print(type(b))

#4 Boolean
a = type(True)
print(a)
a = type(False)
print(a)

#5 Set
a = {1, 2, 3, 4, 5}
print(type(a))
a = {1, "Gautam", 3.5, "A", 5+2j}
print(type(a))
