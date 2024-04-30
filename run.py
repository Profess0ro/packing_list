import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SPREADSHEET = GSPREAD_CLIENT.open("packing_list_app")


"""
This function displaying all
packing lists that has been
created by the user
"""
def allPackingLists():
    print("\n\n\n\n\n\n\n")
    worksheets = SPREADSHEET.worksheets()

    if len(worksheets) > 1:
        print("These are your current packing lists: \n")
        for index, worksheet in enumerate(worksheets[1:], start=1):
            print(f"# {index} - {worksheet.title.capitalize()}")
    else:
        print("You have no packing lists.")
        return None
    print("----------------------------------------------\n")    
    print("# A. Add a new packing list")
    print("# B. Delete a packing list")
    print("# C. Edit a packing list")
    print("# D. Back to main menu\n\n")
    choice = input("What do you want to do now?\n")
    

    if choice.lower() == "a":
        createNewPackingList()
    elif choice.lower() == "b":
        deletePackingList()
    elif choice.lower() == "c":
        editExistingPackingList()
    elif choice.lower() == "d":
        print("\n\n\n\n\n\n\n")
        mainMenu()
    else:
        print("Invalid input. Please try again.")
        allPackingLists()


"""
This function creates a new packing
list (worksheet) in the spreadsheet 
that are connected to this app.
"""
def createNewPackingList():
    print("\n")
    print("Oh! So you are planning to travel again\n")
    new_worksheet = input("Whats the name of your new packing list?: \n")

    SPREADSHEET.add_worksheet(title=f"{new_worksheet}", rows="100", cols="10")
    print("\n\n")
    print(f"Packing list {new_worksheet} created successfully...")
    print("\n\n")


"""
This function displays all the items 
in the selected packing list
"""
def check_list(worksheet):
    items_list = worksheet.col_values(1)
    packed_list = worksheet.col_values(2)
    print("\n\n\n\n")
    print("Here are your items to pack:")
    print("----------------------------")
    
    
    for items, packed in zip(items_list, packed_list):
        print(f"{items.capitalize()}, Is it packed?: {packed}")
    print("\n\n")
    
    editItemsOnExistingList(worksheet)

"""
This funtion will add an item
to the selected packing list
and add "No" on the second column
that indicates if it´s packed
or not
"""

def addNewItem(selected_worksheet):
    item = input("Enter the item you want to add: ")


    selected_worksheet.append_row([item, "No"])
    print(f"Item '{item}' added to the packing list.")
    

def deleteItem():
    print("Delete an item")

def changeStatusOnItem():
    print("Change status on item")


"""
This function lets the user
decide whether to add, delete 
or list the items in the selected
packing list
"""
def editItemsOnExistingList(selected_worksheet):
    print("*                                            *")
    print("*   What do you want to do with this list?   *")
    print("*                                            *")
    print("* Please select one of the following options *")
    print("* ------------------------------------------ *")
    print("* 1. Add a new item                          *")
    print("* 2. Delete an item                          *") 
    print("* 3. List items                              *")
    print("* 4. Change status on item                   *")
    print("* 5. Quit to main menu                       *")
    print("**********************************************")

    choice = input("Enter your choice: ")

    if choice == "1":
        addNewItem(selected_worksheet)
    elif choice == "2":
        deleteItem()
    elif choice == "3":
        check_list(selected_worksheet)
    elif choice == "4":
        changeStatusOnItem()
    elif choice == "5":
        print("\n\n\n\n\n\n\n")
        mainMenu()
    else:
        print("Invalid input. Please try again.")
        

"""
This function wants the user to select
which packing list that wants to be
edited.
"""
def editExistingPackingList():
    worksheets = SPREADSHEET.worksheets()
    if len(worksheets) > 1:
        print("These are your current packing lists: \n")
        for index, worksheet in enumerate(worksheets[1:], start=1):
            print(f"# {index} - {worksheet.title.capitalize()}")

        choice = input("Enter the number of the packing list you want to work on: ")
        try:
            choice_index = int(choice)
            if 0 < choice_index <= len(worksheets) - 1:
                selected_worksheet = worksheets[choice_index]
            else:
                print("Invalid choice. Please enter a valid number.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

    elif len(worksheets) == 1:
        print("You have only one packing list: \n")
        print(f"{worksheets[0].title.capitalize()}")
        selected_worksheet = worksheets[0]

    else:
        print("You have no packing lists.")
        return

    print("\n")
    print("Editing the selected packing list...\n")
    check_list(selected_worksheet)
    editItemsOnExistingList(selected_worksheet)


"""
This function will delete an 
existing packing list
"""
def deletePackingList():
    print("Delete packing list")   

def mainMenu():
    print("**********************************************")
    print("*                                            *")
    print("*    Welcome to your packing list planner    *")
    print("*                                            *")
    print("* Please select one of the following options *")
    print("* ------------------------------------------ *")
    print("* 1. Add a new packing list                  *")
    print("* 2. Delete a packing list                   *") 
    print("* 3. Show all packing lists                  *")
    print("* 4. Edit existing packing list              *")
    print("* 5. Quit                                    *")
    print("**********************************************")

    choice = input("Enter your choice: ")

    if choice == "1":
        createNewPackingList()
    elif choice == "2":
        deletePackingList()
    elif choice == "3":
        allPackingLists()
    elif choice == "4":
        editExistingPackingList()
    elif choice == "5":
        quit()
    else:
        print("Invalid input. Please try again.")
        mainMenu()

mainMenu()
