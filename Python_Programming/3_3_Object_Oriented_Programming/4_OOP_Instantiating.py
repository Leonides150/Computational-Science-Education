#1 Instantiating a class with the __init__ method

class Recipe:
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
    
    def contents(self):
        print("The " + self.dish + " has " + str(self.items) + \
              " and takes" + str(self.time) + " minutes to make")

pizza = Recipe("Pizza", ["Cheese", "Dough", "Tomato"], 45)
pasta = Recipe("Pasta", ["Penne", "Sauce"], 35) 

print(pizza.items)
print(pasta.items)

pizza.contents()
print(pizza.contents())


#Exercise: Instantiate a custom Object
'''
Step 1

1.1 Define a class called MyFirstClass.

1.2 Add a print statement inside it such as “Who wrote this?”.
Step 2

Create a string variable named index and initialize it with a string “Author-Book”.
Step 3

3.1 Define a function called hand_list() with the help of def keyword. 

3.2 Pass the parameter  self to it. And then pass two parameters, philosopher and book to it.
Step 4

4.1 Write a print statement using the print() function and pass the class variable by accessing it. 

Hint: Class variables are accessed directly by calling it over the class name using dot notation.

4.2 Write a print statement that will give output such as: “Plato wrote the book: Republic” where “Plato” is the philosopher and “Republic” is the book. 

Hint: You can make use of the built-in (+) concatenation operator to join these strings. 
Step 5

5.1 Create and instantiate an object of that class, called whodunnit

5.2 Call method hand_list() over this object “whodunnit” and pass two values to it namely “Sun Tzu” and “The Art of War”.
'''

#First approach
class MyFirstClass:
    
    print("Who wrote this?")
    index = "Author-Book"
        
    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)    
        print(philosopher + " wrote the book " + book)
    
whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")

#Second approach

class MyFirstClass:
    def __init__(self, philosopher, book) -> None:
        self.philosopher = philosopher
        self.book = book

    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self):
        print(MyFirstClass.index)    
        print(self.philosopher + " wrote the book " + self.book)
    
whodunnit = MyFirstClass("Sun Tzu", "The Art of War")
whodunnit.hand_list()
