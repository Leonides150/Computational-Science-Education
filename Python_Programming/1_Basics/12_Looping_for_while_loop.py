#For statement types

#Iterating over a string
string = 'Iterate over this string'
for x in string:
    print(x)

#Iterating over a list of numbers
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

#Iterating over a Range of numbers
#ZERO BASED INDEXING
for i in range(15):
    print(i)

#For and While loopcomparison
#For loop is used when you know the number of iterations beforehand, while while loop is used when you want to repeat a block of 
# code until a certain condition is met.

favorites = ['creme brulee', 'brownie', 'ice cream']

for item in favorites:
    print('I like ..', item)

count = 0
while count < len(favorites):
    print('I like ..', favorites[count])
    count += 1

#To get item and index together in a for loop, we can use the built-in function enumerate() which returns both the index 
# and the item in each iteration.

for index, item in enumerate(favorites):
    print(index, item)


#Placement of else in for loops 
#Break statement is used to exit a loop prematurely when a certain condition is met. When a break statement is encountered, 
# the loop is immediately terminated, and the program continues with the next statement after the loop.

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

#1. If the loop completes without a break, the else block will be executed.
for dessert in favorites:
    if dessert == 'Churros':
        print('Yes one of my favorite desserts is', dessert)
        break 
    else:
        print('No sorry, not a dessert on my list')

#2
for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes, one of my favorite desserts is', dessert)
        break
else:  # This else belongs to the for loop, not the if statement
    print('No sorry, not a dessert on my list')

#Continue statement is used to skip the current iteration of a loop and move on to the next iteration. When a continue 
# statement is encountered, the rest of the code inside the loop for that iteration is skipped, and the loop proceeds to 
# the next iteration.

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert) 

#Pass statement is a null operation that is used as a placeholder in situations where a statement is syntactically required 
#but no action is needed.

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert) 

