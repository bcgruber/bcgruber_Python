'''
>Finish walking through this lecture to copy/paste the beginning of the script you will need for your homework.
(Links to an external site.)Links to an external site.

>Finish the user option to delete an entry from the dictionary by removing the "pass" statements and adding code to
delete a user by name (extra challenge: can you figure out how to delete a user by name OR username?)

>Finish the user option to lookup a username by name by removing the "pass" statement and adding code to find a user by name

>Run the script and make sure each option works

>Add exception handling to each user input option.

>Add doc strings to the script and comment the code.

Push your finished script to your personal, publicly accessible Github repo.

Submit a link to the Github repo containing your script on canvas.

'''

import re
from sortedcontainers import SortedDict


def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a Phone Number')
    print('5. Quit')
    print()


# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

# display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user

    #exception handling for initial user input
    while True:
        try:
            menu_choice = int(input("Type in a number (1-5): "))
            break
        except ValueError:
            #Display error message when input is not numeric
            print("Numbers pls.")

    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x, y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x, y))

    # add an entry
    elif menu_choice == 2:
        print("Add User")
        #Exception handling for user name (only letters accpeted)
        while True:
            name = input("Name: ")
            if re.match('^[A-Za-z_-]*$',name):
                break
            else:
                #Name can only consist of letters
                print("Letters pls.")
        username = input("User Name: ")
        usernames[name] = username


    # remove an entry
    elif menu_choice == 3:
        print("Remove User")
        # Exception handling for user name (only letters accpeted)
        while True:
            name = input("Name: ")
            if re.match('^[A-Za-z_-]*$',name):
                break
            else:
                # Name can only consist of letters
                print("Letters pls.")
        if name in usernames:
            usernames.pop(name)
        else:
            print(name,"is not in the dictionary")

    # view user name
    elif menu_choice == 4:
        print("Lookup User")
        # Exception handling for user name (only letters accpeted)
        while True:
            name = input("Name: ")
            if re.match('^[A-Za-z_-]*$',name):
                break
            else:
                # Name can only consist of letters
                print("Letters pls.")
        if name in usernames:
            for key, value in usernames.items():
                if name == key:
                    print("The username for ",key,"is",value)
        else:
            print("username not found")

    # is user enters something strange, show them the menu
    elif menu_choice != 5:
        print_menu()