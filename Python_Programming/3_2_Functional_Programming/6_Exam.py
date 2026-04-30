'''
## Exercise Instructions:

1. **Open the `comprehensions.py` file** under the **PROJECT** folder.

2. **Run the script**.
   - Open a terminal by navigating to `Terminal > New Terminal`.
   - Execute the following command to run the script:
     ```bash
     python3 comprehensions.py
     ```

3. **Implement the `to_mod_list()` function**. 
   - Use the `map()` function to apply the `mod()` function to each element in `employee_list`.
   - Store the result in a variable called `map_emp`, convert it to a list, and return it.
   - **Note:** The `mod()` function formats each entry as `name_department`, for example, `"Lisa_Cold Storage"`.

4. **Implement the `generate_usernames()` function**.  
   - Use list comprehension and the `replace()` method to replace spaces with underscores (`_`) in `mod_list`.
   - Return the modified list of usernames.

5. **Implement the `map_id_to_initial()` function**.  
   - Use dictionary comprehension to map each employee's ID to the first letter of their name.
   - The resulting dictionary should use initials as keys and IDs as values.
'''

# Input data: List of dictionaries
employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Function to be passed to the map() function. Do not change this.
def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
   """ Modifies the employee list of dictionaries into list of employee-department strings

   [IMPLEMENT ME] 
      1. Use the map() method to apply mod() to all elements in employee_list

   Args:
      employee_list: list of employee objects

   Returns:
      list - A list of strings consisting of name + department.
   """
   ### WRITE YOUR CODE HERE ###
   map_emp = map(mod, employee_list)
   
   # Shortcut to convert map object to list
   mod_emp_list = list(map_emp) 

   #Full method to convert map object to list
   '''
   i=0
   mod_emp_list = []

   for x in map_emp:
      mod_emp_list.append(x)
   '''
   return(mod_emp_list)

def generate_usernames(mod_list):
   """ Generates a list of usernames 

   [IMPLEMENT ME] 
      1. Use list comprehension to replace space characters with underscores

   Args:
      mod_list: list of employee-department strings

   Returns:
      list - A list of usernames consisting of name + department delimited by underscores.
   """
   ### WRITE YOUR CODE HERE ###
   new_mod_list = [x.replace(" ", "_") for x in mod_list]
   return new_mod_list

def map_id_to_initial(employee_list):
   """ Maps employee id to first initial

   [IMPLEMENT ME] 
      1. Use dictionary comprehension to map each employee's id (value) to the first letter in their name (key)

   Args:
      employee_list: list of employee objects

   Returns:
      dict - A dictionary mapping an employee's id (value) to their first initial (key).
   """
   ### WRITE YOUR CODE HERE ###
   '''
   for x in employee_list:
      print(str(x["id"]) +" "+ x["name"][0])
   '''
   dict_employee = {x["name"][0]: x["id"] for x in employee_list}
   return dict_employee

def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Modified employee list: " + str(mod_emp_list) + "\n")

   print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

   print(f"Initials and ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
   main()

