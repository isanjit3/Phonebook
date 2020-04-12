import os
import csv
from operator import itemgetter

header = ['Name', 'E-mail', 'Phone Number']
keys = ['name', 'email', 'number']
sort_by_key = "name"

def displayContacts(data, keys, header=None, sort_by_key=None, sort_order_reverse=False):

    # If header is not empty, add header to data
    if header:
        print("Contacts:")
        print("---------")

    column_widths = []

    try:
        for key in keys:
            column_widths.append(max(len(str(column[key])) for column in data))
    except:
        return

    # Create a tuple pair of key and the associated column width for it
    key_width_pair = zip(keys, column_widths)

    format = ('%-*s ' * len(keys)).strip() + '\n'
    formatted_data = ''
    for element in data:
        data_to_format = []
        # Create a tuple that will be used for the formatting in
        # width, value format
        for pair in key_width_pair:
            data_to_format.append(pair[1])
            data_to_format.append(element[pair[0]])
        formatted_data += format % tuple(data_to_format)
    return formatted_data

def lookUpContact():
    print("Search for a contact")
    print("How would you like to search?")
    print("1. Name")
    print("2. Email")
    print("3. Number")
    
    while True:
        searchBy = int(input("-> "))
        if (searchBy == 1): # Search by name
            nameFound = False
            while not(nameFound):
                name = raw_input("Which name do you want to search? ")
                nameDict = next((item for item in contacts if item["name"] == name), None)
                if (nameDict == None):
                    print("Name not found, try again")
                    continue
                nameFound = True;
            break
        elif (searchBy == 2): # Search by email address
            emailFound = False
            while not(emailFound):
                email =raw_input("Which email do you want to search? ")
                emailDict = next((item for item in contacts if item["email"] == email), None)
                if (emailDict == None):
                    print("Email not found, try again")
                    continue
                emailFound = True
            break
        elif (searchBy == 3): # Search by phone number
            numberFound = False
            while not(numberFound):
                number = raw_input("Which number do you want to search? ")
                numberDict = next((item for item in contacts if item["number"] == number), None)
                if (numberDict == None):
                    print("Number not found, try again")
                    continue
                numberFound = True
            break
        else:
            print("Not a valid input")
            continue
    
    contactToDisplay = []
    nameToDisplay = ""

    if (searchBy == 1):
        contactToDisplay.append(nameDict)
        nameToDisplay = nameDict["name"]
    elif (searchBy == 2):
        contactToDisplay.append(emailDict)
        nameToDisplay = emailDict["name"]
    elif (searchBy == 3):
        contactToDisplay.append(numberDict)
        nameToDisplay = numberDict["name"]
    
    print("")
    print(str(nameToDisplay) + "'s Contact Info:")
    print(displayContacts(contactToDisplay, keys))
    print("")

def addContact():
    name = str(raw_input("Enter the full name: "))
    email = str(raw_input("Enter the email: "))
    number = str(raw_input("Enter the phone number (###)###-####: "))

    contact = {
        "name": name,
        "email": email,
        "number": number
    }

    contacts.append(contact)

    print("")
    print(name + " was added to the phonebook")
    print("")

def updateContact():
    print("Search for a contact to update")
    
    contactDict = None
    name, email, number = None, None, None

    while True:
        print("How would you like to search?")
        print("1. Name")
        print("2. Email")
        print("3. Number")
        contactDict = None

        searchBy = int(input("-> "))
        if (searchBy == 1): # Search by name
            name = raw_input("Which name do you want to search? ")
            contactDict = next((item for item in contacts if item["name"] == name), None)
            if (contactDict == None):
                print("Name not found, try again")
                print("")
                continue
            break
        elif (searchBy == 2): # Search by email address
            email =raw_input("Which email do you want to search? ")
            contactDict = next((item for item in contacts if item["email"] == email), None)
            if (contactDict == None):
                print("Email not found, try again")
                continue
            break
        elif (searchBy == 3): # Search by phone number
            number =raw_input("Which number do you want to search? ")
            contactDict = next((item for item in contacts if item["number"] == number), None)
            if (contactDict == None):
                print("Number not found, try again")
                continue
            break
        else:
            print("Not a valid input")
            continue
    
    contactIndex = contacts.index(contactDict)
    print("Found Contact: ", contactDict)
    # Update contact name
    print("Do you want to update contact name? (Y/N)")
    updateNameBool =raw_input("-> ")
    if (updateNameBool.lower() == "y"):
        newName =raw_input("Change name to: ")
        contactDict["name"] = newName
        print("Contact name updated")
    print("")

    # Update email address
    print("Do you want to update email address? (Y/N)")
    updateEmailBool =raw_input("-> ")
    if (updateEmailBool.lower() == "y"):
        newEmail = raw_input("Change email to: ")
        contactDict["email"] = newEmail
        print("Email address updated")
    print("")

    # Update phone number
    print("Do you want to update phone number? (Y/N)")
    updateNumberBool =raw_input("-> ")
    if (updateNumberBool.lower() == "y"):
        newNumber =raw_input("Change phone number to: ")
        contactDict["number"] = newNumber
        print("Phone number updated")
    print("")

    contacts[contactIndex] = contactDict

    loadMenu()

def deleteContact():
    print("Search for a contact to update")
    print("How would you like to search?")
    print("1. Name")
    print("2. Email")
    print("3. Number")
    
    while True:
        searchBy = int(input("-> "))
        if (searchBy == 1): # Search by name
            nameFound = False
            while not(nameFound):
                name = raw_input("Which name do you want to search? ")
                nameDict = next((item for item in contacts if item["name"] == name), None)
                if (nameDict == None):
                    print("Name not found, try again")
                    continue
                nameFound = True;
            break
        elif (searchBy == 2): # Search by email address
            emailFound = False
            while not(emailFound):
                email =raw_input("Which email do you want to search? ")
                emailDict = next((item for item in contacts if item["email"] == email), None)
                if (emailDict == None):
                    print("Email not found, try again")
                    continue
                emailFound = True
            break
        elif (searchBy == 3): # Search by phone number
            numberFound = False
            while not(numberFound):
                number = raw_input("Which number do you want to search? ")
                numberDict = next((item for item in contacts if item["number"] == number), None)
                if (numberDict == None):
                    print("Number not found, try again")
                    continue
                numberFound = True
            break
        else:
            print("Not a valid input")
            continue

    contactToDisplay = []

    if (searchBy == 1):
        contactToDisplay.append(nameDict)
    elif (searchBy == 2):
        contactToDisplay.append(emailDict)
    elif (searchBy == 3):
        contactToDisplay.append(numberDict)

    print("")
    print("Do you want to delete this contact? (y/n)")
    print("")
    print(displayContacts(contactToDisplay, keys))
    deleteConfirmation = raw_input("-> ")

    if (deleteConfirmation.lower() == "y"):
        if (searchBy == 1):
            contacts.remove(nameDict)
            print(str(nameDict["name"]) + " was removed")
        elif (searchBy == 2):
            contacts.remove(emailDict)
            print(str(emailDict["name"]) + " was removed")
        elif (searchBy == 3):
            contacts.remove(numberDict)
            print(str(numberDict["name"]) + " was removed")
    
def saveContacts():
    with open('contacts.txt', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(contacts)

def loadMenu():
    print("--------------------------------")
    print("|             Menu             |")
    print("| -> Display Contacts  ('c')   |")
    print("| -> Look Up           ('l')   |")
    print("| -> Add Contact       ('a')   |")
    print("| -> Update Contact    ('u')   |")
    print("| -> Delete Contact    ('d')   |")
    print("| -> Save Contacts     ('s')   |")
    print("| -> Exit Program      ('e')   |")
    print("--------------------------------")

    #Different Menu options
    while True:
        choice = str(raw_input("Please enter a choice: "))
        print("")
        if (choice == "c"):
            dc = displayContacts(contacts, keys, header)
            if (dc == None):
                print("No contacts to display.")
                print("")
            else:
                print(dc)
            break
        elif (choice == "l"):
            lookUpContact()
            break
        elif (choice == "a"):
            addContact()
            break
        elif (choice == "u"):
            updateContact()
            break
        elif (choice == "d"):
            deleteContact()
            break
        elif (choice == "s"):
            print("Do you want to save the latest contact information? (y/n)")
            saveConfirmation = raw_input("-> ")
            if (saveConfirmation.lower() == "y"):
                print("")
                print("Saving Contacts to 'contacts.txt'...")
                saveContacts()
                print("Contacts saved successfully")
            break
        elif (choice == "e"):
            print("Are you sure you want to exit? (y/n)")
            closeConfirmation = raw_input("-> ")
            if (closeConfirmation.lower() == "y"):
                print("")
                print("Closing the Phonebook...")
                exit()
            break
        else:
            print("Not a valid choice")
            continue  
    loadMenu() 

def main():

    print("--------------------------------")
    print("|   Welcome to the Phonebook!  |")
    loadMenu()

with open('contacts.txt') as f:
    contacts = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

main()
