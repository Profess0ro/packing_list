# **Packing list planner**
This packing list planner are created to help the user keep track what and what they haven´t packed before going on a trip. In this planner the user can create packing lists and add items to the lists. Multiple packing lists can be created since every list is a worksheet in the spreadsheet. While the user are packing they can come back and change packing status on the item. This will help the user keep track on what they have and haven´t packed. This planner will be available wherever you are and you can´t loose it as you can do with a paperlist.<br><br>
<img src="readme/main_menu.png">


[Link to spreadsheet](https://docs.google.com/spreadsheets/d/1AV-nZAvPqpJ5bxexeTKuvK2YJYU36GT0OuKhUHCSzzk/edit?usp=sharing)<br>
[Link to application](https://projectprofessoro-7c74b3018064.herokuapp.com)

# Content
- [Developer´s goal](#developers-goal)<br>
- [User´s goal](#users-goal)<br>
- [User stories](#user-stories)<br>
- [Design](#design)<br>
- [Existing features](#existing-features)<br>
- [Future features](#future-features)<br>
- [Flowchart](#flowchart)<br>
- [Testing](#testing)<br>
- [Bugs](#bugs)<br>
- [Validation](#validation)<br>
- [Technologies](#technologies)<br>
- [Imports](#imports)<br>
- [Deployment](#deployment)<br>
- [Resources](#resources)<br>
- [Credits](#credits)<br>
<hr>

### Developer's goal

1.	*Create a Simple Interface* 
	- Make this application easy for all users to handle, with instructions readable and very clear how to go further/backwards in every step.

2.	*Implement Core Functions*
	- Create this application with functions such as creating multiple packing lists that you can edit with:<br>- adding items<br>- deleting items<br>- list all items<br>- change packing status between "yes" and "no"<br>
    Other functions that can be used are: delete packing list and show all packing lists

3.	*Store Created Packing Lists*
	- Incorporate Google Sheets for managing the data that has been entered by the user. This makes the data accessible wherever the user are located. So they can keep up by adding items if something that they want to pack pops up at work or on the bus.

4.	*Easy User Experience*
	- This application is made to fit every kind of user with easy options and easy formed input validation. If something is enter invalid, messages will show what was wrong and how to enter valid data for the user.
    
5.	*Learn and Apply New Skills*
	- With this project it was a great opportunity to learn the python language. And with Google sheets API connected it was a experience to work with this data management.

[Back to Content](#content)

### User's goal

With this application the user´s goal is to make their planning before a trip easier than using pen and paper. Papers are easy to loose and on that piece of paper could have been items they forgets to pack when leaving on a trip. Therefor this application are made to help them organize the packing before leaving on a trip. 


1.	*Organized before leaving on a trip*
	- When you have several places to visit in a short time, the user can create multiple packing list with the items for each place to visit.
	
2.	*Packing progress*
	- On every packing list the user can provide items that should be packed for each visit and change status whether the item is packed or not. So that nothing is forgotten when leaving home.

4.	*Easy to use*
	- Interaction with this application is easy since the information, validation and feedback provides helpfully to complete the tasks.

[Back to Content](#content)

# User stories

### **First time visitor goals**
- When visiting this application for the first time it´s easy to understand what the functions are in this packing list planner so I can start prepare for my trips. <br>- ***Achived by:*** Providing the user easy navigation through all functions with validation and error messages when invalid data are entered.

### **Returning visitor goals**
- When returning to this application I can check how my packing progress are going before going to my trip. I can change status if some items are packed and also add and delete items to my existing list. <br>- ***Achieved by:*** The user can go in and edit a packing list and with functions as change packing status on every item, add and delete items on the list. 

### **Frequently visitor goals**
- If I´m going to prepare packing lists for multiple trips in a short time there´s an option for me to create multiple packing lists so I can keep track on every trips packing lists. <br>- ***Achieved by:*** Let the user add additional packing list and add items to each and every single packing list with their unique items.

[Back to Content](#content)

# Design

### Colorscheme

- For this application I´ve tried to have the same color to the similar information. Here is how I have used the colors:

**Cyan**<br>
This color are applied to:<br>- the input questions<br>- descriptions on how to enter the data

**Green**<br>
This color are applied to:<br>- messages that confirms decisions that where made (adding items/packing lists, changing status and deletion of items/packing lists)

**Red**<br>
This color are applied to:<br>- error messages when data entered invalid<br>- guidance on how the user exits when they don´t want to enter any data

**Yellow**<br>
This color are applied to: <br>- the welcome and goodbye text of this application<br>- The guidance to the user which packing list they are editing<br>- The question when they are going to confirm a deletion of an item or a packing list

**White**<br>
This color are applied to:<br>- the options of every menu<br>- the items and packing lists when they are listed

[Back to Content](#content)

# Existing features

### Create a new packing list
When a packing list have been created with a valid name, a submenu will be shown with options for the user how to continue with this application.<br>
<img src="readme/creating_packing_list1.png"><br>
<img src="readme/creating_packing_list2.png">

### Add items to packing lists
When items have been added with valid data, the item will appear on the packing list with 'No' as packing status. There will be a submenu appearing underneith the list with options how the user wants to continue with this application.<br><br>
<img src="readme/add_items1.png"><br>
<img src="readme/add_items2.png">

### Change packing status on items
When the user wants to change an items packing status, first all the items will appear that is on the packing list. Then the user will choose which item they want to change status on. A confirmation message will then be visual that you either have packed or unpacked an item.<br><br>
<img src="readme/change_status1.png"><br>
<img src="readme/change_status2.png"><br>
<img src="readme/change_status3.png">

### Deleting an item
When the user wants to delete an item from the packing list, first all the items will appear. After a choice of item has been made a confirmation of deleting that item will appear for the user. Either if the deletion has been confirmed or not, a message will be shown what decision has been made.<br><br>
<img src="readme/deleting_item1.png"><br>
<img src="readme/deleting_item3.png"><br>
<img src="readme/deleting_item2.png">

### Delete a packing list
When the user wants to delete a packing list, first the packing lists that are created will be shown for the user before choosing which list they want to delete. After a choice has been made the user have to confirm the deletion. Either if the deletion has been confirmed or not, a message will be shown what decision has been made.<br><br>
<img src="readme/deleting_packing_list1.png"><br>
<img src="readme/deleting_packing_list2.png"><br>
<img src="readme/deleting_packing_list3.png">

### Show all packing lists
When the user wants to see what packing lists they have created a submenu will be shown with options on how to go further<br><br>
<img src="readme/show_all_lists.png">

[Back to Content](#content)

# Future features

- **Item quantity:** For example if the user wants to pack 4 pair of pants there will be a choice when adding items that they can choose to also add the amount of pairs that they want to pack. The user would also when editing this item add how many that has been packed.
- **Countdown timer:** Add a countdown timer so the user can add which date they are traveling and see how many days there are left to pack the items.

[Back to Content](#content)

# Flowchart
These are the flowcharts that was created before starting this project and are the blueprints for this planner. 
### Main menu
<img src="readme/flowchart_main_menu.png">

### Editing existing list
<img src="readme/flowchart_editing_list.png">

[Back to Content](#content)

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

`Deleting a packing list`<br>
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Delete an existing packing list | Delete chosen # list and confrimed | Chosed to delete # 2 and confirmed | The chosed packing list was deleted | Pass |
| Declining a deletion | When declining a deletion, the packing list shall not be deleted | 
| Trying to delete a # that doesn´t exist | A message shall tell me that # doesn´t exist | Tried to delete # 0 | Message told me that # 0 was not an option | Pass |
| Deleting the last existing packing list | Menu shall shown that no packing list exists | Deleted the last packing list | Message told me there are no more packing lists and menu with options shown | Pass |
<img src="readme/delete_packing_list1.png">
<img src="readme/delete_packing_list2.png">
<img src="readme/delete_packing_list5.png">
<img src="readme/delete_packing_list3.png">
<img src="readme/delete_packing_list4.png">

`Adding items to packing list`<br>
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Adding an item | Item successfully added to list and shows up on worksheet in with 'No' in second column | Added "Passport" | "Passport" was created and showed up with "No" in second column | Pass |
| Adding same item that exists | A message shall tell me that the item already exists on the list | Adding "Passport" again | Message told me that "Passport" already exists | Pass |
| Adding item with special characters | A message shall tell me to only use alphabetic characters | Adding "Passport!" | A message told me to only use alphabetic characters | Pass |
| Adding item with digits | A message shall tell me to only use alphabetic characters | Adding "Passport1" | A message told me to only use alphabetic characters | Pass |
<img src="readme/adding_item1.png">
<img src="readme/adding_item2.png">
<img src="readme/adding_item3.png">
<img src="readme/adding_item4.png">
<img src="readme/adding_item5.png">

`Deleting items from packing list`<br>
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Delete an item | When deleting an item, a confirmation question shall be shown. When confirmed the item shall be deleted | Delete "Toothpaste" and confirmed | After confirmation a message shown that "Toothpaste" was deleted and it disappeared from the list | Pass |
| Declining deletion of an item | When you declining a deletion of an item, the item shall not be deleted and you get back to edit menu | Declining deletion of "City map" | When declined the deletion of "City map" a message shown that the item wasn´t deleted and got back to edit menu | Pass |
| Delete an index not existing | When trying to delete an index not shown in list a message shall tell me that index doesn´t exist | Tried deleting #7 and 't' | Message told me that #7 and 't' was a invalid input | Pass |
| Deleting the last item | When deleted the last item a message shall tell me that there are no items in the packing list | Deleted all items | A message told me that there are no items in the packing list | Pass |
<img src="readme/delete_item1.png">
<img src="readme/delete_item2.png">
<img src="readme/delete_item3.png">
<img src="readme/delete_item4.png">
<img src="readme/delete_item5.png">
<img src="readme/delete_item6.png">

`Changing packing status on item`<br>
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Changing from 'No' to 'Yes' | When changing status a message shall tell me that the item has been packed | Changed "Passport" status | A message told me that the item has been packed and it changed 'No' to 'Yes' | Pass |
| Changing from 'Yes' to 'No' | When changing status a message shall tell me that the item has been unpacked | Changed "Passport" status | A message told me that the item has been unpacked and changed 'Yes' to 'No' | Pass |
| Enter wrong choices | When enter wrong choices a message shall tell me that wrong choice has been made | Entered wrong index in different kinds ('t', '0', '!') | Message told me that the value entered is invalid | Pass |
| Change item when packing list is empty | When chosing to change status on an empty packing list you will brought back to edit menu | Tried to change status on empty list | Brought back to edit menu page and it says that I don´t have any items on the list | Pass |
<img src="readme/changing_status1.png">
<img src="readme/changing_status2.png">
<img src="readme/changing_status3.png">
<img src="readme/changing_status4.png">
<img src="readme/changing_status5.png">

[Back to Content](#content)

# Bugs
### Bugs encountered when testing
- When you created a new packing list and wanted to delete a packing list directly after, it didn´t showed the newly created packing list.<br>- **Solution:** Update the worksheet list with "global worksheets" in the create new packing list function.
- If you typed a alphabetic character when the choice was a digit and vice versa, it did´t gave a message that it was a wrong choice.<br>- **Solution:** Added `if ____.isdigit/.isalpha` to the check if choice are made with right input.
- If you wanted to delete an item even if there wasn´t any in the list, the question which # to delete still showed up.<br>- **Solution:** Added `if not items_list:` to see if there are any items added to the list.
- If there are no items to be changed, it still asked which item to be changed.<br>- **Solution:** added `if len(items_list) == 0:` before asking which item that shall be changed.

[Back to Content](#content)

# Validation
Extracted the code in to the pep8 validation and found no errors in the code:<br><br>
<img src="readme/pep8_validation.png">

[Back to Content](#content)

# Technologies

- [Python Linter](https://pep8ci.herokuapp.com/#) - Code Institutes code checker to see if there are errors with the style conventions in PEP8.
- [Draw.io](https://www.drawio.com/) - Planning tool that was used to create the flowcharts for this application that I had as blueprints.
- [Git](https://git-scm.com/) - Used to export the code with `git add` `git commit` `git push`
- [Visual Studio Code](https://code.visualstudio.com/) - The EDI that I used for coding this application. Very easy to use EDI and in this EDI you can debug your code with extensions such as 'python debugger', that was very useful when coding.
- [Github](https://github.com/) - Online storage of the code with repositories. Here you can go back and follow your changes if you notice a problem that has occured with your code.
- [Heroku](https://id.heroku.com/login) - The page where this application are deployed and hosted.

[Back to Content](#content)

# Imports

- [OS](https://www.geeksforgeeks.org/os-module-python-examples/?ref=lbp) - With this module the application can operate with the operation system for the `clear()` function.
- [Colorama](https://pypi.org/project/colorama/) - This module are used to add textcolor to this application.
- [Gspread](https://pypi.org/project/gspread/) - API module to help this application collaborate with Google Spreadsheets.

**To install these imports:** `pip install _name of import_`<br>
**To generate modules to requirements.txt:** `pip freeze > requirements.txt` 

[Back to Content](#content)

# Deployment

This application was created using VS Code, GitHub and Heroku. 

- [Python](https://www.python.org/) - First of all, ensure that python are installed onto your system.

### GitHub
1. Log in to your GitHub account.
2. Create a repository by click on 'New' at the repositories page.
3. Go into your repository [This repository](https://github.com/Profess0ro/packing_list) and click on 'Code' and copy the link.
4. Open VS code and choose 'Clone git repository..' now paste the link in the command file at the top: `https://github.com/Profess0ro/packing_list.git` and choose a local storage in the window that pops up.

### Google spreadsheets API
1. Go to [Google Cloud platform](https://console.cloud.google.com/) and log in to your account.
2. Next to the **'Google Cloug logo'** click on the scrollbar and choose **'New project'** and type in a name for the project.
3. Go in to **'APIs and services'** and scroll down to **'Google drive'** and click onto it and then click on **'Enable'**. Do the same thing with **'Google Sheets'**.
4. In **'APIs and services'** click on **'Credentials'** in the menu to the right. <br>- "From which API are you using?" select **'Google Drive API'**<br>- "Which data will you be accessing?" select **'Application data'**<br>- "Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions?" select **'No, I'm not using them'**<br>- Then click **'Next'**<br>- Enter a **'Service account name'**<br>- "Grant this service account access to project" select **'Role': Editor**<br>- Click **'Done'**
5. In **'Credentials'** Scroll down to **'Service Accounts'** and click on your account.
6. Now click on **'KEYS'** in the top menu<br>- Click on **'Add Key'** dropdown and select **'Create New Key'**<br>- Select **'JSON'** and then click **'Create'**<br>- Now a **'json file'** has been downloaded to your computer. Locate the file and rename it to **'creds.json'** and add it to your repository location.
7. Now you will be adding personal info to this spreadsheet so ensure that **creds.json** are in your `.gitignore`
8. Open your **'creds.json'** file in VS Code and copy the value of **'clients_email'** 
9. Open your spreadsheet [My spreadsheet](https://docs.google.com/spreadsheets/d/1AV-nZAvPqpJ5bxexeTKuvK2YJYU36GT0OuKhUHCSzzk/edit#gid=1870814311).<br>- Then click on **'Share'** in the top right corner.<br>- Paste the value of **'clients_email'** and make sure **'Editor'** are selected and unmark **'Notify people'**<br>- Now click **'Share'** so that you are allowing the application to make changes to the spreadsheet.


### Heroku
1. Log in to your Heroku account
2. Go to the **'Heroku dashboard'** and click **'New'** and then **'Create new app'**
3. Choose a unique name for this application, then choose region (EU or USA)
4. Now go to **'Settings'** -> **'Reaveal config vars'** and add **'KEY'** `PORT` with **value** of `8000` then add **'KEY'** `CREDS` with the **value** of `the text inside your 'creds.json'`
5. In **'Settings'** click on **'Add buildpack'** and add following packs in the right order: 1. `Python` 2. `Node.js`
6. To install requirements use `pip install -r requirements.txt` at the terminal in VS Code.
7. To create the Procfile use `echo web: node index.js > Procfile` at the terminal in VS Code.
8. To deploy your repository to your Heroku account there are two ways. First go to **'Deploy'** in your Heroku application then scroll down and choose one of these options:<br>- **'Enable Automatic Deploys':** If you want that everytime you use `git push` in VS Code that it deploys to Heroku<br>- **'Deploy Branch':** If you want to manually deploy your changes and have control when the code should or shouldn´t been deployed.

[Back to Content](#content)

# Resources

- [The Basic structure of this application](https://www.youtube.com/watch?v=aEIHZDv_23U) - This tutorial helped me start with this project<br>
- [W3schools](https://www.w3schools.com/) - Learning the meaning of the python codes<br>
- [API Guides](https://developers.google.com/sheets/api/guides/concepts) - How to work with spreadsheets/worksheets in python<br>
- [Flake8rules](https://www.flake8rules.com/) - Helping me explaining the  errors in "Python Linter".<br>
- [Clear function](https://www.geeksforgeeks.org/clear-screen-python/) - How to install and use the `clear()` function<br>
- [Main block function](https://medium.com/@adheremo65/what-is-the-main-block-in-python-if-name-main-d9f7410ef2f2#:~:text=Why%20do%20we%20need%20to,a%20module%20into%20another%20script) - Explaining `if __name__ == "__main__":` code<br>
- [Python strings](https://www.tutorialspoint.com/python/python_strings.htm) - How to use `.isdigit`and `.isalpha`<br>

[Back to Content](#content)

# Credits 

- Rohit Sharma - My mentor
- [Jaqi´s Readme](https://github.com/JaqiKal/task-master?tab=readme-ov-file#objectives) - This helped me write this Readme.

[Back to Content](#content)