
file = open('4_5_input_file.txt', mode = 'r')      
# options for mode are: r: open and read txt, rb: open and read binary, r+ open for read and write, w open for writing, a: open for
#editing or appending data

#file.read() returns the entire contents of the file or specified number of characters mentioned
#data = file.read(3)
#print(data)

#file.readline() returns a line, or specified characters from a line
#data = file.readline(10)
#print(data)

#file.readlines() reads entire content of file and returns an ordered list
data = file.readlines()
print(data)
print(len(data))

for x in data:
    print(x)

file.close()

###Alternative: Using with open

with open('4_5_input_file.txt', mode = 'r') as file:
    data = file.readline()

    print(data)

###Writing to a file, always overwrites!
with open('4_5_new_file_1.txt', mode = 'w') as file:
    data = file.write("Testing writing to file!")

###Writing with append so it adds to existing content
#Also testing writelines function which adds lists to a file
with open('4_5_new_file_2.txt', mode = 'a') as file:
    data = file.writelines(["\nTesting writing to file!2", "\nThis time with multiple lines at a time.", "\nThis is the last line."])

#With Open function always returns lists by default
with open('4_5_input_file.txt', mode = 'r') as file:
    for x in file:
        print(x)

#Splitting lines
with open('4_5_new_file_2.txt', mode = 'r') as file:
    data = file.read()
    lines = data.split("\n")
    print(lines)


#Picking a random line from a desired file mentioned by the user
import random

file_name = input("Type the file name: ")
file = open(file_name) # "r" omitted as it's the default
file_content = file.read()
file_content_list = file_content.split("\n")
file.close()
print(random.choice(file_content_list))
