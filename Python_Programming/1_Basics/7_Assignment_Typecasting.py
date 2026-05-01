#ASSIGNMENT 1
# Using explicit type conversion, change the following 
# inputs so the types match with the following below
#  
# name = type string
# age = type int
# height = type float
# loyalty = type boolean

# Modify the line below
name = input('What is your name? ')

print(f"Type of name variable is: {type(name)}. It should be <class 'str'>")

# Modify the line below
age = int(input('What is your age? '))
#age = int(age)
print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")

# Modify the line below
height = float(input('What is your height in meters? '))
#height = float(height)
print(f"Type of height variable is: {type(height)}. It should be <class 'float'>")

# Modify the line below
loyalty = bool(input('Are you part of our loyalty program? '))
#loyalty = bool(loyalty)
print(f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")

#ASSIGNMENT 2

# The below script will ask for 3 inputs. Each input will be based
# on the price of the items - the price is determined by you. The output
# should print the total of the 3 inputs rounded to 2 decimal places e.g
#
#   1 coffee @ $ 2.00
#   1 sandwich @ $ 4.99
#   1 cake @ $ 2.75
#
#   Your total bill is $ 9.74

# Modify the line below
coffee = float(input('1 coffee @: $ '))

# Modify the line below
sandwich = float(input('1 sandwich @: $ '))

# Modify the line below
cake = float(input('1 cake @: $ '))

bill_total = coffee + sandwich + cake

print('Your total bill is $', bill_total)