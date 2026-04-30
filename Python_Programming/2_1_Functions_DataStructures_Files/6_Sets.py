
my_set = {1, 2, 3, 4, 5, 5}
my_set.add(6)
my_set.add(3) #Duplicate values will not be added to the set
my_set.remove(2)
print(my_set)

my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {4, 5, 6, 7, 8}

print(my_set_1.union(my_set_2)) #Union of two sets  
print(my_set_1 | my_set_2) #Union of two sets using the | operator

print(my_set_1.intersection(my_set_2)) #Intersection of two sets
print(my_set_1 & my_set_2) #Intersection of two sets using the & operator

print(my_set_1.difference(my_set_2)) #Difference of two sets (elements in my_set_1 but not in my_set_2)
print(my_set_1 - my_set_2) #Difference of two sets using the - operator

print(my_set_1.symmetric_difference(my_set_2)) #Symmetric difference of two sets (elements in either my_set_1 or my_set_2 but not in both)
print(my_set_1 ^ my_set_2) #Symmetric difference of two sets using the ^ operator

print(my_set_1[1]) #Sets do not support indexing, this will raise a TypeError