#Recursion is a programming technique where a function calls itself in order to solve a problem. It typically involves a base case 
#that stops the recursion and a recursive case that breaks the problem into smaller subproblems.


#1 Factorial of a number
###By recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

### By looping
def factorial_loop(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial_loop(5))

#2 Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))

#3 Power of a number
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
print(power(2, 10))

#3. Towers of Hanoi

# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself.
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)

# Driver code: Initializing and calling the function
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')
    
