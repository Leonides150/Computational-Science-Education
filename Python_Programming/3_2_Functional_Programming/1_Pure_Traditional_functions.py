#Is it s pure function? No! Since it modifies the global variable, it is not a pure function. 
# A pure function should not have side effects and should always return the same output for the same input.

global_list = [1, 2, 3]

def append_to_list(item):
    return global_list.append(item)
#append_to_list(4)  #comment out to check the usage of a traditional function vs a pure function
#print(global_list)

#Pure function benefits
#1. Predictability: Pure functions always produce the same output for the same input, making them easier to understand and debug.
#2. Testability: Pure functions can be easily tested in isolation since they do not depend  on external state.
#3. Reusability: Pure functions can be reused across different parts of a program without worrying about unintended side effects.
#4. Concurrency, Multi-threading: Pure functions can be safely executed in parallell without issues of shared state.

#Conversion of the above traditional function to a pure function

def append_to_list_pure(item, lst):
    new_list = lst.copy()  # Create a copy of the input list to avoid modifying the original
    new_list.append(item)   # Append the item to the new list
    return new_list        # Return the new list without modifying the original

new_list_1 = append_to_list_pure(4, [1, 2, 3])
print(new_list_1)  # Output: [1, 2, 3, 4]
print(global_list)  # Output: [1, 2, 3] - original list remains unchanged

