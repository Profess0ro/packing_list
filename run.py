import gspread
from google.oauth2.service_account import Credentials
from colorama import init
from colorama import Fore, Back
init(autoreset=True)
init()


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SPREADSHEET = GSPREAD_CLIENT.open("packing_list_app")



def all_packing_lists():
    """
    This function displaying all
    packing lists that has been
    created by the user

    ----------------------

    Since you can´t delete all worksheets
    this function will not include
    the first worksheet and start
    counting the list from 1 instead of 2
    
    ----------------------

    If there are no packing list to be shown 
    there will be 2 options for the user
    either to create a packing list or
    go back to the main menu

    """
    worksheets = SPREADSHEET.worksheets()
    clear()
    if len(worksheets) > 1:
        print("These are your current packing lists: \n")

        for index, worksheet in enumerate(worksheets[1:], start=1): 
            print(f"# {index} - {worksheet.title.capitalize()}")
    else:
        print("You have no packing lists.")

        while True:
            menu_if_no_list_exists()
                


def create_a_new_packing_list():
    """
    This function creates a new packing
    list (worksheet) in the spreadsheet 
    that are connected to this app.

    When created, the user will get options
    on what to do next.

    ---------------------------------------
    
    When you have created a packing list
    a menu will be shown
    with options for the user asking
    what to do next
    """
    clear()
    print(Fore.YELLOW + "Oh! So you are planning to travel again\n")
    while True:

        new_worksheet_name = input("What's the name of your new packing list?: \n")
        worksheet_titles = [worksheet.title.lower() for worksheet in SPREADSHEET.worksheets()]
        if new_worksheet_name.lower() in worksheet_titles:
            print(Fore.RED + f"A packing list with the name '{new_worksheet_name}' already exists. Please choose a different name.\n")
        else:
            new_worksheet = SPREADSHEET.add_worksheet(title=new_worksheet_name, rows="100", cols="2")
            clear()
            print(Fore.GREEN + f"Packing list '{new_worksheet_name}' created successfully...")
            break
    while True:
        print("----------------------------------------------\n")
        print("1. Create a new packing list")
        print(f"2. Add items to packing list '{new_worksheet_name}'")
        print("3. Go back to main menu\n\n")
        choice = input("What do you want to do now? ")

        if choice == "1":
            print("\n")
            create_a_new_packing_list()
        elif choice == "2":
            add_new_item_to_packing_list(new_worksheet)
            
        elif choice == "3":
            clear()
            main_menu()
            break
        else: 
            print(Fore.RED + f"{choice} was not an option, please try again")
            


def check_list(worksheet):
    """
    This function displays all the items 
    in the selected packing list
    
    ------------------------------------
        
    This is the format that the
    items will be shown in the list.
        itemname | Packed: No
    Since all items that are added
    to the list aren´t packed since
    the user changing status on the 
    item in another function.
    
    """
    items_list = worksheet.col_values(1)
    packed_list = worksheet.col_values(2)
    clear()
    if len(items_list) == 0:
        print(Fore.RED, Back.WHITE+f"You have no items in '{worksheet.title}' packing list!\n\n")
        while True:
            print("Here are some options for you:\n")
            print("1. Add an item to this list")
            print("2. Edit another packing list")
            print("3. Go back to main menu\n")
            choice = input(Fore.CYAN+"What do you want to do?\n")
            print(Fore.RESET)
            if choice == "1":
                add_new_item_to_packing_list(worksheet)
                break
            elif choice == "2":
                all_packing_lists()
                break
            elif choice == "3":
                clear()
                main_menu()
                break
            else:
                print(f"{choice} was not an option, please try again\n\n\n")
    else:
        print(Fore.YELLOW+f"Here are your items in '{worksheet.title}':")
        print("----------------------------")
        

        for items, packed in zip(items_list, packed_list):
            print(Fore.BLUE+f"{items.capitalize()}, Is it packed?: {packed}\n\n")
        
        
        edit_item_on_packing_list(worksheet)




def add_new_item_to_packing_list(worksheet):
    """
    This funtion will add an item
    to the selected packing list
    and add "No" on the second column
    that indicates if it´s packed
    or not
    """
    clear()
    print(Fore.YELLOW+f"Adding items to '{worksheet.title}'")
    item = input("Enter the item you want to add: ")

    # format how the items are added in the list
    worksheet.append_row([item, "No"])
    clear()
    print(f"Item '{item}' added to the packing list.\n ")
    check_list(worksheet)

    

def delete_item_on_packing_list(worksheet):
    items_list = worksheet.col_values(1)
    
    if len(items_list) == 0:
        print("There are no items in this packing list to delete.\n")
        return
    
    print(Fore.YELLOW + "Here are the items in the packing list:")
    print("--------------------------------------")
    for index, item in enumerate(items_list, start=1):
        print(Fore.BLUE+f"{index}. {item.capitalize()}")
        
    
    while True:
        try:
            print("\n\n")
            item_index = int(input(Fore.CYAN + "Enter the number of the item you want to delete: "))
            print(Fore.RESET)
            if 1 <= item_index <= len(items_list):
                confirmation = input(f"Are you sure you want to delete '{items_list[item_index - 1]}'? (y/n): ")
                if confirmation.lower() == "y":
                    worksheet.delete_rows(item_index)
                    print(Fore.GREEN+f"Item '{items_list[item_index - 1]}' deleted successfully.")
                else:
                    clear()
                    print("Deletion canceled.")                    
                return
            else:
                print(Fore.RED+"Invalid item number. Please enter a valid number.")
        except ValueError:
            print(Fore.RED+"Invalid input. Please enter a number.")

def change_status_on_item():
    print("Change status on item")



def edit_item_on_packing_list(worksheet):
    """
    This function lets the user
    decide whether to add, delete 
    or list the items in the selected
    packing list
    """


    print(Fore.CYAN+"What do you want to do with this list?")

    print("------------------------------------------")
    print("1. Add a new item")
    print("2. Delete an item") 
    print("3. List items")
    print("4. Change status on item")
    print("5. Quit to main menu\n\n")


    choice = input(Fore.CYAN+"Enter your choice: ")

    if choice == "1":
        add_new_item_to_packing_list(worksheet)
    elif choice == "2":
        delete_item_on_packing_list(worksheet)
    elif choice == "3":
        check_list(worksheet)
    elif choice == "4":
        change_status_on_item(worksheet)   
    elif choice == "5":
        clear()
        main_menu()
    else:
        print("Invalid input. Please try again.")
        


def edit_existing_packing_list():
    """
    This function wants the user to select
    which packing list that wants to be
    edited.
    """
    clear()
    worksheets = SPREADSHEET.worksheets()
    if len(worksheets) > 1:
        print("These are your current packing lists: \n")
        for index, worksheet in enumerate(worksheets[1:], start=1):
            print(f"# {index} - {worksheet.title.capitalize()}")
        
        choice = input("Enter the number of the packing list you want to work on: \n")
        try:
            choice_index = int(choice)
            if 0 < choice_index <= len(worksheets) - 1:
                selected_worksheet = worksheets[choice_index]
                check_list(selected_worksheet)
                edit_item_on_packing_list(selected_worksheet)
            else:
                print("\n\n")
                print(f"{choice} was not an option. Please enter a valid option.")
                edit_existing_packing_list()
        except ValueError:
            print("\n\n")
            print(f"{choice} was not an option. Please enter a valid option.")
            edit_existing_packing_list()

    elif len(worksheets) == 2:
        print("You have only one packing list: \n")
        print(f"{worksheets[1].title.capitalize()}")
        selected_worksheet = worksheets[1]

    else:
        print("\n\nThere is no packing list to be edited...\n\n")
        menu_if_no_list_exists()





def menu_if_no_list_exists():
    """
    This menu will be shown if 
    no packing list has been
    created so far.
    """
    print("----------------------------------------------\n")    
    print("# 1. Create a new packing list")
    print("# 2. Back to main menu\n\n")
    choice = input("What do you want to do?\n")
            
    if choice == "1":
        create_a_new_packing_list()
          
    elif choice == "2":
        main_menu()
         
    else:
        print(f"{choice} was not an option. Please try again.")  


def delete_packing_lists():
    """
    This function will delete an 
    existing packing list
    """
    clear()
    worksheets = SPREADSHEET.worksheets()

    if len(worksheets) > 1:
        print("These are your current packing lists: \n")

        for index, worksheet in enumerate(worksheets[1:], start=1): 
            print(f"# {index} - {worksheet.title.capitalize()}\n\n")
            title = worksheet.title
        choice = int(input("Enter the number of the packing list you want to delete: "))
        
        if 0 < choice <= len(worksheets) - 1:
            SPREADSHEET.del_worksheet(worksheets[choice])
            print(f"\n\n {title} was removed")
        else:
            print(f"\n{choice} was not an option. Please enter a valid number.")
    else:
        print("You have no packing lists.")
        menu_if_no_list_exists()



def quit():
    """
    Saying goodbye to the user when they quit.
    """
    clear()
    print(Fore.YELLOW + "Goodbye and have a nice trip! :)")
    import sys
    sys.exit()
def clear():
    """
    This function will clear the screen
    from all that has been written
    in the screen earlier

    It works on Windows, mac and Linux.
    """
    import os
    os.system('cls')
    from os import system, name
    
    if name == 'nt':
        _ = system('cls')
 
    
    else:
        _ = system('clear')



def main_menu(): 

    print(Fore.YELLOW+"Welcome to your packing list planner\n")
    print(Fore.CYAN+"Please select one of the following options")
    print("------------------------------------------")
    print("1. Add a new packing list")
    print("2. Delete a packing list") 
    print("3. Show all packing lists")
    print("4. Edit existing packing list")
    print("5. Quit\n")

    choice = input(Fore.CYAN+"Enter your choice:                             \n")

    if choice == "1":
        create_a_new_packing_list()
    elif choice == "2":
        delete_packing_lists()
    elif choice == "3":
        all_packing_lists()
    elif choice == "4":
        edit_existing_packing_list()
    elif choice == "5":
        quit()
    else:
        print(Fore.RED + f"{choice} was not an option. Please try again.")
        main_menu()


if __name__ == "__main__":
    main_menu()
