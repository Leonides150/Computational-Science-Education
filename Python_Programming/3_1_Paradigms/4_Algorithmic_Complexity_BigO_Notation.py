#1. Constant Time
#Big O(1) - Time taken is constant regardless of the size of the input

drinks = {1: 'Coffee', 2: 'Tea', 3: 'Shake', 4: 'Juice'}
print(drinks[1])

#2. Linear Time
#Big O(n) - Time taken grows linearly with the size of the input

#Example 1
for x in range(1000000):
    #print(x)   only uncomment if sure to print such a large array!
    pass

#Example 2
#Linear Search

def number_search(num):
    i = 0
    for x in range(100):
        if x == num:
            print(f'Total Iterations: {i}')
            return x
        i += 1

number_search(95)


#3 Logarithmic time: Binary Search
#Big O(log n) - Time taken grows logarithmically with the size of the input. This is often seen in algorithms that divide the 
#input in half at each step, such as binary search.

def binary_search(num):
    itr = 0
    x = range(100)
    left = 0
    right = len(x) - 1

    while left <= right:
        itr += 1
        middle = int((left+right)/2)
        number = x[middle]

        if number == num:
            print(f'Total Iterations: {itr}')
            return number
        elif number < num:
            left = middle + 1
        else:
            right = middle - 1

number = binary_search(95)


#4 Quadratic Time: Nested Loops
#Big O(n^2) - Time taken grows quadratically with the size of the input. This is often seen in algorithms that involve nested loops, 
# where the inner loop runs n times for each iteration of the outer loop.

#Example 1
for x in range(100):
    for y in range(100):
        #print(x, y)  only uncomment if sure to print such a large array!
        pass

#Example 2
#Bubble Sort is an example of a quadratic time algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))


#5 Exponential Time: Recursive Fibonacci Sequence
#Big O(2^n) - Time taken grows exponentially with the size of the input. This is often seen in algorithms that solve problems by 
#recursively breaking them down into smaller subproblems, such as the Fibonacci sequence.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  

print(fibonacci(10))