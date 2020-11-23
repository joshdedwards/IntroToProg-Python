# ------------------------------------------------------------------------ #
# Title: Assignment05.py
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
#   RRoot,1.1.2030,Created started script
#   JEdwards,11.22.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #


# -- Data -- #
# declare variables and constants
objFileName = "ToDoList.txt"   # An object that represents a file NAME STRING
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    objFile = open(objFileName, "x")
    objFile.close()
except FileExistsError:
    pass

objFile = open(objFileName, "r")
for row in objFile:
    row_list = row.split(",")
    dicRow = {"Task": row_list[0].strip(), "Priority": row_list[1].strip()}
    lstTable.append(dicRow)
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        if not lstTable:
            print("There's nothing here yet!")
        else:
            for row in lstTable:
                first_element = row["Task"]
                second_element = row["Priority"]
                print("Task: ", first_element, " | Priority: ", second_element, sep="")
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        new_task = input("New Task: ").lower()
        new_priority = input("What priority level is that task? ").lower()
        dicRow = {"Task": new_task.strip(), "Priority": new_priority.strip()}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        task_remove = input("What task should be removed? ").lower().strip()
        count = 0
        for row in lstTable:
            if task_remove == row["Task"]:
                lstTable.remove(row)
                count += 1
        if count == 0:
            print("I'm sorry, that task doesn't exist.")
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open(objFileName, "w")
        for row in lstTable:
            objFile.write(row["Task"].lower() + "," + row["Priority"].lower() + "\n")
        objFile.close()
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        break  # and Exit the program

    else:
        print("Invalid choice, please try again.")