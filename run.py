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


def fetch_all_lists(worksheets):
    """
    This function will collect all
    packing lists that exists.

    If there are no lists created
    menu_if_no_list_exists()
    will be called

    Because you can´t delete all
    worksheets in a spreadsheet
    the list of all worksheets are
    spliced using:
    'enumerate(worksheets[1:], start=1'
    this will show worksheets starting
    with index 1 and start the list
    with 1.
    """
    if len(worksheets) > 1:
        print("These are your current packing lists: \n")

        for index, worksheet in enumerate(worksheets[1:], start=1):
            print(f"# {index} - {worksheet.title.capitalize()}")
    else:
        print(Fore.RED+"You have no packing lists.")
        menu_if_no_list_exists()


def all_packing_lists():
    """
    When user wants to list all
    packing lists this menu will
    be displayed with options
    to go further
    """
    clear()
    fetch_all_lists(worksheets)
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
        delete_packing_lists(worksheets)
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

    When created a new packing list
    the global worksheets
    will update and the user
    will get options
    on what to do next.

    When the user typed in a name
    it checks if:
    - the title already exists
    - it´s only alphabetic characters
    - 'exit' is typed to go back
    """
    clear()
    print(Fore.YELLOW + "Oh! So you are planning to travel again\n")
    while True:
        print(Fore.RED + "Enter 'exit' to go back to main menu")
        print(Fore.CYAN + "(max 20 characters)")
        print(Fore.CYAN + "(no special characters or digits)")
        new_worksheet_name = input(
            "What's the name of your new packing list?: \n")
        if new_worksheet_name.lower() == "exit":
            clear()
            main_menu()
        elif (new_worksheet_name.replace(" ", "").isalpha() and
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

    global worksheets
    worksheets = SPREADSHEET.worksheets()

    while True:
        print("----------------------------------------------\n")
        print("1. Create a new packing list")
        print(f"2. Add items to packing list '{new_worksheet_name}'")
        print("3. Delete a packing list")
        print("4. Go back to main menu\n\n")
        choice = input("What do you want to do now? \n")

        if choice == "1":
            print("\n")
            create_a_new_packing_list()
        elif choice == "2":
            add_new_item_to_packing_list(new_worksheet)
        elif choice == "3":
            clear()
            delete_packing_lists(worksheets)
        elif choice == "4":
            clear()
            main_menu()
            break
        else:
            print(Fore.RED + f"{choice} was not an option, please try again")


def fetch_all_items(worksheet):
    """
    This function will display
    the items that exists in
    the packing list or
    give a message that
    there are no items in
    the packing list
    """
    items_list = worksheet.col_values(1)
    packed_list = worksheet.col_values(2)
    if len(items_list) == 0:
        print(Fore.RED + "You have no items in")
        print(f"'{worksheet.title}'!\n\n")
    else:
        print(Fore.YELLOW+"Here are your items in")
        print(f"{worksheet.title}:")
        print("----------------------------")
        for index, (item, packed) in enumerate(zip(items_list, packed_list),
                                               start=1):
            print(f"# {index}: {item.capitalize()}, Packed?: {packed}")


def check_list(worksheet):
    """
    When a user wants to edit
    a packing list the function
    fetch_all_items will be
    called to display all items.
    edit_item_on_packing_list_menu
    will then be called to
    show the user options
    on how to go further with
    this packing list.
    """
    fetch_all_items(worksheet)
    edit_item_on_packing_list_menu(worksheet)


def add_new_item_to_packing_list(worksheet):
    """
    This funtion will add an item
    to the selected packing list
    and add "No" on the second column
    that indicates if it´s packed
    or not.
    It checks if the items name:
    - already exists
    - are alphabetic characters only
    - are 'exit' to go back
    """
    items_list = [item.lower() for item in worksheet.col_values(1)]
    clear()
    while True:
        print(Fore.YELLOW+"Adding items to")
        print(f"'{worksheet.title}'")
        print(Fore.CYAN + "(max 30 characters)")
        print(Fore.CYAN +"(no special characters or digits)")
        print(Fore.RED + "Enter 'exit' to go back")
        item = input("Enter the item you want to add: \n")
        if item.lower() == "exit":
            clear()
            check_list(worksheet)
        elif item.lower() in items_list:
            clear()
            print(Fore.RED + "An item with the name")
            print(f"'{item}'")
            print(Fore.RED + "already exists.")
            print("Please choose another item.\n")
        elif (item.replace(" ", "").isalpha() and
                len(item) <= 30):
            worksheet.append_row([item, "No"])
            clear()
            print(f"'{item}'")
            print(Fore.GREEN + f"added to {worksheet.title}\n ")
            check_list(worksheet)

        else:
            clear()
            print(Fore.RED + "Please use alphabetic characters only.")
            print(f"{item}")
            print(Fore.RED + "is not valid\n")


def delete_item_on_packing_list(worksheet):
    """
    This function will delete items
    in the packing lists

    First it checks if a digit
    is typed else it will
    show a message to try again.
    If a digit is typed a question
    will be displayed if they are
    sure to delete or not.
    """

    items_list = worksheet.col_values(1)
    if not items_list:
        print(Fore.RED + "There are no items to delete.")
        check_list(worksheet)
        return
    fetch_all_items(worksheet)
    while True:
        print("\n")
        print(Fore.RED + "Enter 'exit' to go back")
        item_index_input = input(Fore.CYAN + "Which # shall be deleted?\n")
        if item_index_input.lower() == "exit":
            clear()
            check_list(worksheet)
        elif item_index_input.isdigit():
            item_index = int(item_index_input)
            if 1 <= item_index <= len(items_list):
                print(Fore.YELLOW + "Are you sure you want to delete:")
                confirm = input(f"'{items_list[item_index - 1]}'? (y/n):\n")
                if confirm.lower() == "y":
                    worksheet.delete_rows(item_index)
                    clear()
                    print(f"'{items_list[item_index - 1]}'")
                    print(Fore.GREEN + "deleted successfully.")
                elif confirm.lower() == "n":
                    clear()
                    print(f"'{items_list[item_index - 1]}'")
                    print(Fore.RED + "was not deleted")
                else:
                    clear()
                    print(Fore.RED + f"{confirm} invalid")
                    continue
            else:
                clear()
                print(Fore.WHITE + f"'{item_index_input}'")
                print(Fore.RED+"is not a valid #. Please enter a valid #.")
        else:
            clear()
            print(Fore.WHITE + f"'{item_index_input}'")
            print(Fore.RED+"is not a valid #. Please enter a valid #.")
        check_list(worksheet)


def change_status_on_item(worksheet):
    """
    This function will change
    the packing status on
    the items that are in
    the packing lists.

    It will check:
    - if a correct index # is typed
    - if a digit is typed
    - if 'exit is typed it will go back
    """
    clear()
    fetch_all_items(worksheet)
    items_list = worksheet.col_values(1)
    packed_list = worksheet.col_values(2)
    while True:
        print(Fore.RED + "Enter 'exit' to go back")
        item_index_input = input(Fore.BLUE +
                                 "Enter # of the item to change status on:\n")
        if item_index_input.lower() == "exit":
            check_list(worksheet)
        elif item_index_input.isdigit():
            item_index = int(item_index_input)
            if 1 <= item_index <= len(items_list):
                item = items_list[item_index - 1]
                packed_status = packed_list[item_index - 1]
                new_status = "Yes" if packed_status == "No" else "No"
                worksheet.update_cell(item_index, 2, new_status)
                if new_status == "Yes":
                    clear()
                    print(Fore.GREEN + "You have packed")
                    print(f"'{item}'")
                else:
                    clear()
                    print(Fore.GREEN + "You have unpacked")
                    print(f"'{item}'")
                change_status_on_item(worksheet)
                return
            else:
                print(Fore.RED + "Invalid #. Please try again.")
        else:
            print(Fore.RED + "Invalid input. Please enter a number.")


def edit_item_on_packing_list_menu(worksheet):
    """
    This function shows a menu
    to lets the user decide
    whether to add, delete
    or change packing status
    on the items in the selected
    packing list.
    """
    print("\n")
    print(Fore.CYAN+"What do you want to do with this list?")
    print("------------------------------------------")
    print("1. Add a new item")
    print("2. Delete an item")
    print("3. Change packing status on item")
    print("4. Edit another packing list")
    print("5. Quit to main menu")

    choice = input(Fore.CYAN+"Enter your choice: \n")

    if choice == "1":
        clear()
        add_new_item_to_packing_list(worksheet)
    elif choice == "2":
        clear()
        delete_item_on_packing_list(worksheet)
    elif choice == "3":
        clear()
        change_status_on_item(worksheet)
    elif choice == "4":
        clear()
        edit_existing_packing_list_menu()
    elif choice == "5":
        clear()
        main_menu()
    else:
        print(f"{choice} is not a valid input. Please try again.")
        edit_item_on_packing_list_menu()


def edit_existing_packing_list_menu():
    """
    This function will first check
    if there are any packing lists
    Then provide a choice which
    packing list that shall
    be edited.
    """
    fetch_all_lists(worksheets)
    print(Fore.RED + "Enter 'exit' to go back to main menu")
    choice = input(Fore.CYAN+"Enter the list # you want to work on: \n")
    if choice.isdigit():
        choice_index = int(choice)
        if 0 < choice_index <= len(worksheets) - 1:
            selected_worksheet = worksheets[choice_index]
            clear()
            check_list(selected_worksheet)
            edit_item_on_packing_list_menu(selected_worksheet)
        else:
            print("\n")
            print(Fore.RED+f"{choice} was not an option.")
            print("Please enter a valid option.")
            edit_existing_packing_list_menu()
    elif choice.lower() == "exit":
        clear()
        main_menu()
    else:
        clear()
        print(Fore.RED+f"{choice} was not an option.")
        print("Please enter a valid option.")
        edit_existing_packing_list_menu()


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


def delete_packing_lists(worksheets):
    """
    This function will delete an
    existing packing list.
    First it will check if
    there are any lists created.

    If there are no lists, it will
    show a menu with options to go further.

    Because you can't delete
    all worksheets in a spreadsheet,
    index # 0 can't be deleted, using
    '0 < int(choice)' will disable
    choosing 0.

    There are also a confirmation
    if the chosen packing list
    should be deleted or not.
    """

    fetch_all_lists(worksheets)

    if len(worksheets) == 0:
        menu_if_no_list_exists()
        return

    while len(worksheets):
        print(Fore.RED + "Enter 'exit' to go back to main menu")
        choice = input(Fore.CYAN + "Enter the list # you want to delete: \n")
        if choice.isdigit() and 0 < int(choice) <= len(worksheets) - 1:
            removed_title = worksheets[int(choice)].title
            confirmation = input(Fore.YELLOW + 
                                 f"Delete '{removed_title}'? (y/n)\n")
            if confirmation.lower() == 'y':
                SPREADSHEET.del_worksheet(worksheets[int(choice)])
                clear()
                print(Fore.WHITE + f"\n'{removed_title}'")
                print(Fore.GREEN + "was deleted")
                worksheets = SPREADSHEET.worksheets()
                delete_packing_lists(worksheets)
            elif confirmation.lower() == 'n':
                clear()
                print(Fore.WHITE + f"'{removed_title}'")
                print(Fore.RED + "was not deleted.")
                delete_packing_lists(worksheets)
            else:
                clear()
                print(Fore.RED + "Invalid choice. Please enter 'y' or 'n'.")
                delete_packing_lists(worksheets)
        elif choice.lower() == "exit":
            clear()
            main_menu()
        else:
            clear()
            print(Fore.WHITE + f"'{choice}'")
            print(Fore.RED + "was not an option.")
            print(Fore.RED + "Please enter a valid #.")
            delete_packing_lists(worksheets)


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
    """
    This is the main menu and
    what options you can
    choose from here.
    """
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
        clear()
        delete_packing_lists(worksheets)
    elif choice == "3":
        all_packing_lists()
    elif choice == "4":
        clear()
        edit_existing_packing_list_menu()
    elif choice == "5":
        quit()
    else:
        print(Fore.RED + f"{choice} was not an option. Please try again.")
        main_menu()


if __name__ == "__main__":
    main_menu()
