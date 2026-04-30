
menu = ["chicken tandoori", "chicken tikka masala", "goat curry", "buffalo paneer wings", "Fish biryani", "cauliflower pakora"]
print("Welcome to the Python Diner!")
print("Here's our menu:")
def find_item(entree):
    item_name = entree.split()  # Get the first word of the entree
    if item_name[0] == "chicken":
        return entree
    
map_menu = (map(find_item, menu))
print(map_menu)
#Convert the map object to a list to see the results
map_menu_list = list(map_menu)
print(map_menu_list)
#OR
for x in map_menu:
    print(x)

# Filter out None values from the map result

filtered_menu = filter(find_item, menu)
print(filtered_menu)
filtered_menu_list = list(filtered_menu)
print(filtered_menu_list)

#OR

filtered_menu = list(filter(lambda x: x is not None, map_menu_list))
print(filtered_menu)

