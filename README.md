https://docs.google.com/spreadsheets/d/1AV-nZAvPqpJ5bxexeTKuvK2YJYU36GT0OuKhUHCSzzk/edit?usp=sharing - Spreadsheet

# Flowchart
These flowchart was created before I started and are the blueprints I´ve worked after. 
### Main menu
<img src="readme/flowchart_main_menu.png">

### Editing existing list
<img src="readme/flowchart_editing_list.png">

# Testing
`Main menu`<br>
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Add a new packing list | Navigated to creation page | Choosed # 1 at main menu| Got to the create packing list page | Pass |
| Delete a packing list | Navigated to delete page | Choosed # 2 at main menu | Got to the delete packing list page | Pass |
| Show all packing lists | Navigated to page where all list will be shown | Choosed # 3 at main menu | Saw all created packing lists | Pass |
| Edit existing packing list | Navigated to edit packing list page | Choosed # 4 at main menu | Got to the edit packing list page | Pass |
| Quit | Program shutting down | Choosed # 5 at main menu | Program shut down | Pass |

`Create a packing list`<br>
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Create a list | Successfully add a list and a worksheet will be added in spreadsheet | Created a list called "Germany" | "Germany" was created as a worksheet | Pass |
| Create a list with existing name | A message shall tell me that the title already exists | Created "Germany" again | Message told me that "Germany" already exists | Pass |
| Create a list longer than 20 characters | A message shall tell me that the name is too long | Created a list called "GermanyGermanyGermanyGermany" | Message told me that it´s too long | Pass |
| Create list with special characters | A message shall tell me to only use alphabetic characters | Created a list called "Germany!" | Message told me to only use alphabetic characters | Pass |
| Create a list with digits | A message shall tell me to only use alphabetic characters | Created "Germany1" | A message told me to only use alphabetic characters | Pass |
<img src="readme/create_packing_list1.png">
<img src="readme/create_packing_list2.png">
<img src="readme/create_packing_list3.png">
<img src="readme/create_packing_list5.png">
<img src="readme/create_packing_list4.png">

# Bugs
### Bugs encountered when testing
- When you created a new packing list and wanted to delete a packing list directly after, it didn´t showed the newly created packing list.<br>- **Solution:** Update the worksheet list with "global worksheets" in the create new packing list function.
- If you typed a alphabetic character when the choice was a digit and vice versa, it did´t gave a message that it was a wrong choice.<br>- **Solution:** Added `if ____.isdigit/.isalpha` to the check if choice are made with right input.
- If you wanted to delete an item even if there wasn´t any in the list, the question which # to delete still showed up.<br>- **Solution:** Added `if not items_list:` to see if there are any items added to the list.
# Credits

- https://www.youtube.com/watch?v=aEIHZDv_23U - For basic structure of this application.<br>
- https://www.w3schools.com/ - Learning the meaning of the python codes.<br>
- https://developers.google.com/sheets/api/guides/concepts - How to work with spreadsheets/worksheets in python<br>
- https://www.flake8rules.com/ - Helping me with errors in "Python Linter".