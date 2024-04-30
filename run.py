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
        """ 
        since you can´t delete all worksheets
        this function will not include
        the first worksheet and start
        counting the list from 1 instead of 2
        """
        for index, worksheet in enumerate(worksheets[1:], start=1): 
            print(f"# {index} - {worksheet.title.capitalize()}")
    else:
        print("You have no packing lists.")
        """
        If there are no packing list to be shown 
        there will be 2 options for the user
        either to create a packing list or
        go back to the main menu
        """
    while True:
        print("----------------------------------------------\n")    
        print("# 1. Create a new packing list")
        print("# 2. Back to main menu\n\n")
        choice = input("What do you want to do?\n")
            
        if choice == "1":
            createNewPackingList()
            break  
        elif choice == "2":
            mainMenu()
            break  
        else:
            print(f"{choice} was not an option. Please try again.")
                

"""
This function creates a new packing
list (worksheet) in the spreadsheet 
that are connected to this app.

When created, the user will get options
on what to do next.
"""
def createNewPackingList():
    print("\n")
    print("Oh! So you are planning to travel again\n")
    new_worksheet = input("What's the name of your new packing list?: \n")

    SPREADSHEET.add_worksheet(title=f"{new_worksheet}", rows="100", cols="10")
    print("\n\n")
    print(f"Packing list {new_worksheet} created successfully...")
    print("\n\n")
    """
    When you have created a packing list
    this menu will be shown
    with options for the user
    """
    while True:
        print("----------------------------------------------\n")
        print("1. Create a new packing list")
        print("2. Edit a packing list")
        print("3. Go back to main menu\n\n")
        choice = input("What do you want to do now? ")

        if choice == "1":
            createNewPackingList()
        elif choice == "2":
            editExistingPackingList()
        elif choice == "3":
            mainMenu()
        else: 
            print("That was not an option, please try again") 

"""
This function displays all the items 
in the selected packing list
"""
def check_list(worksheet):
    items_list = worksheet.col_values(1)
    packed_list = worksheet.col_values(2)
    print("\n\n\n\n")
    if len(items_list) == 0:
        print("You have no items in this packing list!\n\n")
        while True:
            print("Here are some options for you:\n")
            print("1. Add an item to this list")
            print("2. Edit another packing list")
            print("3. Go back to main menu\n")
            choice = input("What do you want to do?\n")
            if choice == "1":
                addNewItem(worksheet)
            elif choice == "2":
                allPackingLists()
            elif choice == "3":
                mainMenu()
            else:
                print(f"{choice} was not an option, please try again\n\n\n")
    else:
        print("Here are your items to pack:")
        print("----------------------------")
        
        """
        This is the format that the
        items will be shown in the list.
        Since all items that are added
        to the list aren´t packed since
        the user changing status on the 
        item in another function.
        """
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
    print("\n\n\n")
    item = input("Enter the item you want to add: ")

    # format how the items are added in the list
    selected_worksheet.append_row([item, "No"])
    print("\n\n\n")
    print(f"Item '{item}' added to the packing list.")
    print("\n\n\n")
    

def deleteItem(worksheet):
    print("Delete an item")
    items_list = worksheet.col_values(1)
    packed_list = worksheet.col_values(2)
    print("\n\n\n\n")
    if items_list < 1:
        print("You have no items in this packing list!\n")
        while True:
            print("1. Add an item to this list")
            print("2. Edit another packing list")
            print("3. Go back to main menu")
            choice = input("What do you want to do?\n")
            if choice == "1":
                addNewItem()
            elif choice == "2":
                allPackingLists()
            elif choice == "3":
                mainMenu()
            else:
                print(f"{choice} was not an option, please try again\n\n\n")
    else:
        print("Here are your items to pack:")
        print("----------------------------")
        
        """
        This is the format that the
        items will be shown in the list.
        Since all items that are added
        to the list aren´t packed since
        the user changing status on the 
        item in another function.
        """
        for items, packed in zip(items_list, packed_list):
            print(f"{items.capitalize()}, Is it packed?: {packed}")
        print("\n\n")

def changeStatusOnItem():
    print("Change status on item")


"""
This function lets the user
decide whether to add, delete 
or list the items in the selected
packing list
"""
def editItemsOnExistingList(selected_worksheet):
    # Menu that will be shown
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
        print("\n\n\n")
        print("These are your current packing lists: \n")
        for index, worksheet in enumerate(worksheets[1:], start=1):
            print(f"# {index} - {worksheet.title.capitalize()}")
        
        choice = input("Enter the number of the packing list you want to work on: \n")
        try:
            choice_index = int(choice)
            if 0 < choice_index <= len(worksheets) - 1:
                selected_worksheet = worksheets[choice_index]
            else:
                print("\n\n")
                print(f"{choice} was not an option. Please enter a valid option.")
                editExistingPackingList()
        except ValueError:
            print("\n\n")
            print(f"{choice} was not an option. Please enter a valid option.")
            editExistingPackingList()

    elif len(worksheets) == 2:
        print("You have only one packing list: \n")
        print(f"{worksheets[1].title.capitalize()}")
        selected_worksheet = worksheets[1]
    # Menu to be shown if there are no lists created
    else:
        print("You have no packing lists.")
        print("\n\n")
        print("1. Create a new packing list")
        print("2. Go back to main menu\n")
        choice = input("What do you want to do?\n")
        if choice == "1":
            createNewPackingList()
        elif choice == "2":
            mainMenu()
        else:
            print(f"{choice} was not an option, try again\n")
            print("Taking you back to the main menu instead")
            mainMenu()


    check_list(selected_worksheet)
    editItemsOnExistingList(selected_worksheet)


"""
This function will delete an 
existing packing list
"""
def deletePackingList():
    print("Delete packing list")   

def quit():
    print("\n\n\n")
    print("Goodbye and have a nice trip! :)")
    print("\n\n\n")
    


def mainMenu(): # Main menu 
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
# Calling the main menu at startup
mainMenu()
