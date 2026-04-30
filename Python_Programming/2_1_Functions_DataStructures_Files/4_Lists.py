#Can store any data structure in a list, including other nested lists.
my_list = [1, 'Hello', 3.14, [2, 4, 6], True]

my_list_1 = [1, 2, 3, 4, 5]
print(my_list_1[0]) #Accessing the first element of the list
print(my_list_1) #Accessing the third element of the list
my_list_1.insert(len(my_list_1), 10) #Inserting a new element at the end of the list
print(my_list_1)
my_list_1.append(12) #Appending a new element at the end of the list
print(my_list_1)
my_list_1.remove(3) #Removing an element from the list
print(my_list_1)
my_list_1.pop(2) #Removing an element at a specific index
print(my_list_1)
my_list_1.extend([30, 20, 40]) #Extending the list with another list
print(my_list_1)
my_list_1.sort() #Sorting the list in ascending order
print(my_list_1)
my_list_1.sort(reverse=True) #Sorting the list in descending order
print(my_list_1)

for x in my_list_1:
    print("Value:", x)