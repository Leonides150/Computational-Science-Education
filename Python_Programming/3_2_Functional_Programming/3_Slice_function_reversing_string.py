#1 Simplest way to reverse a string using slicing
#string[start:stop:step]

def reverse_string(s):
    return s[::-1]

# Example usage
print(reverse_string("Hello, World!"))

#2 Using recusion to reverse a string
def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]     #alternatively: return s[-1] + reverse_string_recursive(s[:-1])
    
# Example usage
print(reverse_string_recursive("Hello, reverse this string!"))