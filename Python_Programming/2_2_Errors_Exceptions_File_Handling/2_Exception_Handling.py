
def division(a,b):
    return a/b

try:
    result = division(4,0)
#except Exception as err:                       try this first, output the class, then replace this by the next error message
#    print("There is an issue:", err)
#    print(err.__class__)
except ZeroDivisionError as err:
    print(err, " Divsion by 0 not permissible")

#continue with further error messages to progressively isolate errors
except Exception as err:
    print("There is an issue:", err)

###Other examples
#1
try:
    items = [1,2,3,4,5]
    item = items[6]
except IndexError as e:
    print(e, "Item does not exist in the list")
    print(e.__class__)

#2
try:        
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except Exception as e:
    print("File Cannot be Accessed", e)