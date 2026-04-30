'''
## There are three main objectives of this activity:
1. Create a function to read in a file.
2. Create a function for writing specific contents to a file.
3. Use lists to store file contents for easier data manipulation.
<br><br>

## Exercise Instructions:
<br>

1. Verify that the `sampletext.txt` and `file_ops.py` files exist and are present inside the project folder.  You can run the `file_ops.py` file by opening a terminal and executing the following command:
    ```
    python3 file_ops.py 
    ```


2. Modify the `file_ops.py` script to complete the `read_file()` function. This function should:
   - Open and read the contents of `sampletext.txt`.
   - Return the entire contents of the file as a string.<br></br>

3. Modify the `file_ops.py` script to complete the `read_file_into_list()` function. This function should:
   - Read `sampletext.txt` line-by-line.
   - Store each line as an element in a list and return this list.<br></br>

4. Modify the `file_ops.py` script to complete the `write_first_line_to_file()` function. This function should:
   - Accept two arguments:
     - **file_contents** (a string with multiple lines of content).
     - **output_filename** (the name of the output file).
   - Write only the first line of `file_contents` into the specified output file.  
     (Identify the first line as everything before the first newline character, `\n`).<br></br>

5. Modify the `file_ops.py` script to complete the `read_even_numbered_lines()` function. This function should:
   - Read `sampletext.txt` line-by-line.
   - Return a list containing only the even-numbered lines (lines 2, 4, 6, etc.) based on the line number in the file.<br></br>

6. Complete the `read_file_in_reverse()` function. This function should:
   - Read `sampletext.txt` and store its lines in reverse order.
   - Return a list of the lines in reverse order.
'''

'''
def create_file():
    f = open('/home/coder/project/sampletext.txt', 'w')
    f.writelines(["Because I could not stop for Death,", "\nHe kindly stopped for me;",
                 "\nThe carriage held but just ourselves", "\nAnd Immortality."])
'''
def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        #print(data)
        return data
    '''
    f = open('sampletext.txt', 'r')
    f_contents = f.read()
    f.close()
    return(f_contents)
    '''
    ### WRITE SOLUTION HERE
    

def read_file_into_list(file_name):
    """ Reads a file and returns a list where each element is a line in the file.

    [IMPLEMENT ME]
        1. Open the given file.
        2. Read the file line-by-line and append each line to a list.
        3. Return the list.

    Args:
        file_name (str): Name of the file to be read.

    Returns:
        list: List where each item is a line from the file.
    """
    with open(file_name, 'r') as file:
        f_content = file.readlines()
        return(f_content)
    ### WRITE SOLUTION HERE
    


def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a given string to an output file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents.
        2. Use the File write() function to write the first line into a file
           with the name from output_filename.

        The first line is everything in a string before the first newline ('\n') character.

    Args:
        file_contents (str): String containing multiple lines of text.
        output_filename (str): Name of the file to write the first line into.
    """
    #first_line = file_contents.split("\n")[0] - this and replace first_line[0] with first_line in write statement OR existing one
    first_line = file_contents.split("\n")
    with open(output_filename, 'w') as file:
        file.write(first_line[0])
    ### WRITE SOLUTION HERE
    


def read_even_numbered_lines(file_name):
    """ Reads even-numbered lines of a file and returns them as a list.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable.
        2. Read the file line-by-line and add the even-numbered lines to a list.
        3. Return the list.

    Args:
        file_name (str): Name of the file to be read.

    Returns:
        list: List of even-numbered lines in the file (2, 4, 6, etc.).
    """
    count = 1
    even_list = []
    with open(file_name, 'r') as file:
        f_content = file.readlines()
        for x in f_content:
            if count % 2 == 0:
                #print(x)
                even_list.append(x)
            count += 1
        return(even_list)

    ### WRITE SOLUTION HERE
    


def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of its lines in reverse order.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable.
        2. Read the file line-by-line and store the lines in a list in reverse order.
        3. Print the list.
        4. Return the list.

    Args:
        file_name (str): Name of the file to be read.

    Returns:
        list: List of lines from the file in reverse order.
    """
    count = 0
    rev_list = []
    with open(file_name, 'r') as file:
        f_content = file.readlines()
        count = len(f_content)
        #print(f_content[count-1])
        for x in f_content:
            #print(f_content[count-1])
            rev_list.append(f_content[count-1])
            count = count - 1
        return(rev_list)



    ### WRITE SOLUTION HERE
    


# Sample commands to run/test your implementations.
def main():
 
    #create_file()
    file_contents = read_file("sampletext.txt")
    print("File Contents:\n", file_contents)
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "output.txt")
    print(read_even_numbered_lines("sampletext.txt"))    
    print(read_file_in_reverse("sampletext.txt"))
   

if __name__ == "__main__":
    main()
