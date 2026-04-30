str1 = input('Enter your first name: ')
str2 = input('Enter your last name: ')

print('Hello ' + str1 + ' ' + str2 + '!')
print('Hello {} {}!'.format(str1, str2))
print(f'Hello {str1} {str2}!')

#Some more examples of concatenation:
print("Hello " + "World!")
print("Hello", "World!")
print("good", "morning", sep="-")
