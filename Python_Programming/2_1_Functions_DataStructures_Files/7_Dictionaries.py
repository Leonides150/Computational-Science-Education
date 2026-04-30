my_dict_1 = {1: "Tea", 2: "Coffee", 3: "Lassi", 4: "Mocktail"}
print(type(my_dict_1))

my_dict_1[2] = "Smoothie"
print(my_dict_1)

del my_dict_1[3]
print(my_dict_1)

my_dict_2 = {'Name': 'Asha', 'Designation': 'Manager', 'Salary': 10000}
print(my_dict_2)

for x, value in my_dict_1.items():
    #print(x, value)
    print(f'{x}: {value}')
