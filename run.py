import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SPREADSHEET = GSPREAD_CLIENT.open('packing_list_app')

# PACKING_LIST = SPREADSHEET.worksheet("packing_list")  
# ITEMS_LIST = PACKING_LIST.col_values(1)  
# PACKED_LIST = PACKING_LIST.col_values(2)
# PACKING_LISTS = .get_all_values()

"""
This function will display all packing list that have been created
"""
def allPackingLists():
    worksheets = SPREADSHEET.worksheets()

    if len(worksheets) > 1:
        print("These are your current packing lists: \n")
        for index, worksheet in enumerate(worksheets[1:], start=1):
            print(f"# {index} - {worksheet.title.capitalize()}")
    elif len(worksheets) <= 1:

        print("You have no packing lists.")




"""
def check_list():
    print("Here are your items to pack:")
    print("----------------------------")
    
    for (items, packed) in zip(ITEMS_LIST, PACKED_LIST):
        print(f"{items.capitalize()}, Is it packed?: {packed}")
"""


"""
This function will create a new packing list for the user.

def createNewPackingList():
    new_worksheet = input("Whats the name of your new packing list?: \n")

    SPREADSHEET.add_worksheet(title=f"{new_worksheet}", rows="100", cols="10")

    print(f"Worksheet {new_worksheet} created successfully...")
"""

# def startApp():
allPackingLists()