import gspread
from google.oauth2.service_account import Credentials
from colorama import init
from colorama import Fore
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
worksheets = SPREADSHEET.worksheets()


def edit_packing_list_menu():
    while True:
        print("----------------------------------------------\n")
        print("1. Create a new packing list")
        print("2. Add items to a packing list")
        print("3. Go back to main menu\n\n")
        choice = input("What do you want to do now? ")

        if choice == "1":
            print("\n")
            create_a_new_packing_list()
        elif choice == "2":
            edit_existing_packing_list()
        elif choice == "3":
            clear()
            main_menu()
            break
        else:
            print(Fore.RED + f"{choice} was not an option, please try again")


def fetch_all_lists():
    """
    This function will collect all
    packing lists that exists.

    If there are no lists created
    menu_if_no_list_exists()
    will be called
    """
    clear()
    if len(worksheets) > 1:
        print("These are your current packing lists: \n")

        for index, worksheet in enumerate(worksheets[1:], start=1):
            print(f"# {index} - {worksheet.title.capitalize()}")
    else:
        print(Fore.RED+"You have no packing lists.")
        menu_if_no_list_exists()


def all_packing_lists():
    """

    """
    fetch_all_lists()
    print("\n")
    print("-------------------------------------")
    print("# 1. Add another packing list")
    print("# 2. Delete a packing list")
    print("# 3. Edit a packing list")
    print("# 4. Go back to the main menu")
    choice = input(Fore.CYAN+"What do you want to do now?\n")
    if choice == "1":
        clear()
        create_a_new_packing_list()
    elif choice == "2":
        clear()
        delete_packing_lists()
    elif choice == "3":
        clear()
        edit_existing_packing_list_menu()
    elif choice == "4":
        clear()
        main_menu()
    else:
        print(Fore.RED+f"{choice} was not a option. Try again")


def create_a_new_packing_list():
    """
    This function creates a new packing
    list (worksheet) in the spreadsheet
    that is connected to this app.

    When created, the user will get options
    on what to do next.

    ---------------------------------------

    When you have created a packing list,
    a menu will be shown with options for
    the user asking what to do next.
    """
    clear()
    print(Fore.YELLOW + "Oh! So you are planning to travel again\n")
    while True:
        print(Fore.CYAN + "(max 20 characters and no special characters)")
        new_worksheet_name = input(
            "What's the name of your new packing list?: \n")
        if (new_worksheet_name.replace(" ", "").isalpha() and
                len(new_worksheet_name) <= 20):
            worksheet_titles = [worksheet.title.lower() for
                                worksheet in SPREADSHEET.worksheets()]
            if new_worksheet_name.lower() in worksheet_titles:
                clear()
                print(Fore.RED + "A packing list with the name")
                print(f"'{new_worksheet_name}'")
                print(Fore.RED + "already exists.")
                print("Please choose a different name.\n")
            else:
                new_worksheet = SPREADSHEET.add_worksheet(
                    title=new_worksheet_name, rows="100", cols="2")
                clear()
                print(Fore.GREEN + "Packing list")
                print(f"'{new_worksheet_name}'")
                print(Fore.GREEN + "created successfully...")
                break
        elif len(new_worksheet_name) > 20:
            clear()
            print(Fore.RED + "It´s more than 20 characters in:")
            print(f"'{new_worksheet_name}'")
            print(Fore.RED + "Please try again.\n")
        else:
            clear()
            print(Fore.RED + "Please use alphabetic characters only.\n")
            print(f"'{new_worksheet_name}' is invalid.")
            print(Fore.RED + "Please try again.\n")

    while True:
        print("----------------------------------------------\n")
        print("1. Create a new packing list")
        print(f"2. Add items to packing list '{new_worksheet_name}'")
        print("3. Go back to main menu\n\n")
        choice = input("What do you want to do now? \n")

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


def fetch_all_items(worksheet):
    items_list = worksheet.col_values(1)
    packed_list = worksheet.col_values(2)
    clear()
    if len(items_list) == 0:
        print(Fore.RED + "You have no items in")
        print(f"'{worksheet.title}'!\n\n")
    else:
        print(Fore.YELLOW+"Here are your items in")
        print(f"{worksheet.title}:")
        print("----------------------------")
        for items, packed in zip(items_list, packed_list):
            print(Fore.YELLOW+f"{items.capitalize()}, Packed?: {packed}")


def check_list(worksheet):

    fetch_all_items(worksheet)
    while True:
        print(Fore.CYAN+"Here are some options for you:\n")
        print("1. Add an item to this list")
        print("2. Edit another packing list")
        print("3. Go back to main menu\n")
        choice = input(Fore.CYAN+"What do you want to do?\n")
        print(Fore.RESET)
        if choice == "1":
            add_new_item_to_packing_list(worksheet)
        elif choice == "2":
            all_packing_lists()
        elif choice == "3":
            clear()
            main_menu()
            break
        else:
            print(f"{choice} was not an option, please try again\n\n\n")


def add_new_item_to_packing_list(worksheet):
    """
    This funtion will add an item
    to the selected packing list
    and add "No" on the second column
    that indicates if it´s packed
    or not
    """
    clear()
    while True:
        print(Fore.YELLOW+f"Adding items to '{worksheet.title}'")
        print(Fore.CYAN + "(max 30 characters and no special characters)")
        item = input("Enter the item you want to add: \n")
        if (item.replace(" ", "").isalpha() and
                len(item) <= 30):
            worksheet.append_row([item, "No"])
            clear()
            print(f"Item '{item}' added to the packing list.\n ")
            check_list(worksheet)
        else:
            print(Fore.RED + "Please use alphabetic characters only.\n")


def delete_item_on_packing_list(worksheet):
    """
    items_list = worksheet.col_values(1)
    clear()
    if len(items_list) == 0:
        print("There are no items in this packing list to delete.\n")
        return

    print(Fore.YELLOW + "Here are the items in the packing list:")
    print("--------------------------------------")
    for index, item in enumerate(items_list, start=1):
        print(Fore.BLUE+f"{index}. {item.capitalize()}")
    """
    items_list = worksheet.col_values(1)
    fetch_all_items(worksheet)
    while True:
        try:
            print("\n\n")
            item_index = int(input(Fore.CYAN + "Which item # to delete: "))
            print(Fore.RESET)
            if 1 <= item_index <= len(items_list):
                print(Fore.YELLOW + "Are you sure you want to delete:")
                confirm = input(f"'{items_list[item_index - 1]}'? (y/n):\n")
                if confirm.lower() == "y":
                    worksheet.delete_rows(item_index)
                    clear()
                    print(Fore.GREEN+f"Item '{items_list[item_index - 1]}'")
                    print(Fore.GREEN+"deleted successfully.")
                elif confirm.lower() == "n":
                    clear()
                    print("Deletion canceled.")
                return
            else:
                print(Fore.RED+"Invalid item #. Please enter a valid number.")
        except ValueError:
            print(Fore.RED+"Invalid input. Please enter a number.")


def change_status_on_item(worksheet):
    items_list = worksheet.col_values(1)
    packed_list = worksheet.col_values(2)
    clear()
    print(Fore.YELLOW + f"Items in {worksheet.title}:\n")
    for index, (item, packed) in enumerate(zip(items_list, packed_list),
                                           start=1):
        print(f"# {index}: {item.capitalize()}, Packed?: {packed}\n")

    while True:
        item_index = input(Fore.BLUE + "Enter # of the item to change:\n")
        if item_index.isdigit():
            item_index = int(item_index)
            if 1 <= item_index <= len(items_list):
                break
            else:
                print(Fore.RED + "Invalid #. Please try again.")
        else:
            print(Fore.RED + "Invalid input. Please enter a number.")

    packed_status = packed_list[item_index - 1]
    new_status = "Yes" if packed_status == "No" else "No"
    worksheet.update_cell(item_index, 2, new_status)
    if new_status == "Yes":
        print(Fore.GREEN + f"You have packed {item}\n")
    else:
        print(Fore.RED + f"You have unpacked {item}\n")
    check_list(worksheet)


def edit_item_on_packing_list_menu(worksheet):
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


def edit_existing_packing_list_menu():
    worksheets = SPREADSHEET.worksheets()
    if len(worksheets) > 1:
        print("These are your current packing lists: \n")
    for index, worksheet in enumerate(worksheets[1:], start=1):
        print(f"# {index} - {worksheet.title.capitalize()}")
    choice = input("Enter the list # you want to work on: \n")
    try:
        choice_index = int(choice)
        if 0 < choice_index <= len(worksheets) - 1:
            selected_worksheet = worksheets[choice_index]
            check_list(selected_worksheet)
            edit_item_on_packing_list_menu(selected_worksheet)
        else:
            print("\n\n")
            print(Fore.RED+f"{choice} was not an option.")
            print("Please enter a valid option.")
            edit_existing_packing_list()
    except ValueError:
        print("\n\n")
        print(Fore.RED+f"{choice} was not an option.")
        print("Please enter a valid option.")
        edit_existing_packing_list()


def edit_existing_packing_list():
    """
    This function wants the user to select
    which packing list that wants to be
    edited.
    """
    clear()
    fetch_all_lists()
    choice = input("Enter the list # you want to work on: \n")
    choice_index = int(choice)
    if 0 < choice_index <= len(worksheets) - 1:
        selected_worksheet = worksheets[choice_index]
        check_list(selected_worksheet)
        edit_item_on_packing_list_menu(selected_worksheet)
    else:
        print("\n\n")
        print(Fore.RED+f"{choice} was not an option.")
        print("Please enter a valid option.")
        edit_existing_packing_list()


def menu_if_no_list_exists():
    """
    This menu will be shown if
    no packing list has been
    created so far.
    """
    print("----------------------------------------------\n")
    print("# 1. Create a new packing list")
    print("# 2. Back to main menu\n\n")
    choice = input(Fore.CYAN+"What do you want to do?\n")

    if choice == "1":
        clear()
        create_a_new_packing_list()
    elif choice == "2":
        clear()
        main_menu()
    else:
        print(Fore.RED+f"{choice} was not an option. Please try again.")


def delete_packing_lists():
    """
    This function will delete an
    existing packing list
    """
    clear()
    fetch_all_lists()
    title = worksheets.title
    choice = int(input("Enter the list # you want to delete: "))

    if 0 < choice <= len(worksheets) - 1:
        SPREADSHEET.del_worksheet(worksheets[choice])
        clear()
        print(Fore.GREEN+f"\n {title} was removed")
    else:
        print(Fore.RED+f"\n{choice} was not an option.")
        print("Please enter a valid number.")


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

    choice = input(Fore.CYAN+"Enter your choice:\n")

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
