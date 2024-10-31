myContacts = dict()

def addToPhoneNumber(contacts):
    print("***WELCOME TO THE NUMBER ADDITION SCREEN***")
    get_name = input("Name: ")
    get_number = input("Phone number: ")
    
    contacts = myContacts.setdefault(get_name, get_number)
    print(f"{get_name} has been added to the contacts...")
    input("Continue?")


def showContacts(contacts):
    numberOfPerson = len(contacts)
    print(f"Number of person: {numberOfPerson}")
    
    for i,j in contacts.items():
        print(i,":",j)
    input("Continue?")


def removeNumber(contacts):
    print("WELCOME TO THE DELETE CONTACT SCREEN")
    deletePerson = input("Name: ")
    contacts = myContacts.pop(deletePerson)
    print(f"{deletePerson} has been successfully deleted.")
    input("Continue?")


while True:
    print("***WELCOME***")
    print("***Make a choice***")
    selection = int(input("1-Add\n2-Delete\n3-See the contact\n4-Exit\n"))

    if selection == 1:
        addToPhoneNumber(myContacts)
    elif selection == 2:
        removeNumber(myContacts)        
    elif selection == 3:
        showContacts(myContacts)
    elif selection == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid selection")