print("Welcome to Address Book")


class AddressBook:
    contact = {}
    contactLength = len(contact)
    contactInListLength = 0
    keysList = list(contact)

    def __init__(self):
        
        pass

    def addContact(first_name, last_name, address, city, state, zip, number, email):
        """
            Description:
                adding contact using add contacts functions
            Parameter:
                self is as parameter
            Return:
                Returning contact dictionary
        """

        contactInList = []

        contactInList.append(first_name)
        contactInList.append(last_name)
        contactInList.append(address)
        contactInList.append(city)
        contactInList.append(state)
        contactInList.append(zip)
        contactInList.append(number)
        contactInList.append(email)

        AddressBook.contactInListLength = len(contactInList)
        AddressBook.contact[AddressBook.contactLength] = contactInList
        AddressBook.keysList = list(AddressBook.contact)
        AddressBook.contactLength += 1
        return AddressBook.contact

    def editContact(contactNumber, first_name, last_name, address, city, state, zip, number, email):

        contactInList = []

        contactInList.append(first_name)
        contactInList.append(last_name)
        contactInList.append(address)
        contactInList.append(city)
        contactInList.append(state)
        contactInList.append(zip)
        contactInList.append(number)
        contactInList.append(email)

        AddressBook.contact[contactNumber] = contactInList
        return AddressBook.contact

    def deleteContact(contactNumber):
       
        del AddressBook.contact[contactNumber]
        return AddressBook.contact

if __name__ == '__main__':
    contact1 = AddressBook()

    while True:
        check = int(input("""
                    1. Press 1 to Add Contact
                    2. Press 2 to Show Contact
                    3. Press 3 to edit Contact
                    4. Press 4 To Delete Contact
                    5. Press 5 To Exit
            """))

        if check == 1:
            fName = input("Enter First Name: ")
            lName = input("Enter Last Name: ")
            address = input("Enter Address: ")
            city = input("Enter City: ")
            state = input("Enter State: ")
            zip = int(input("Enter Zip Code: "))
            mobileNumber = int(input("Enter Mobile Number: "))
            eMail = input("Enter E mail: ")

            AddressBook.addContact(first_name, last_name, address,
                                   city, state, zip, number, email)

        elif check == 2:
            print(AddressBook.contact)

        elif check == 3:
            checkFlag = False
            while True:
                checkName = input("Enter First Name To Check Contact!")
                for i in range(AddressBook.contactLength):

                    if checkName == AddressBook.contact[i][0]:
                        print("Now You Can Edit!")
                        first_name = input("Enter First Name: ")
                        last_name = input("Enter Last Name: ")
                        address = input("Enter Address: ")
                        city = input("Enter City: ")
                        state = input("Enter State: ")
                        zip = int(input("Enter Zip Code: "))
                        number = int(input("Enter Mobile Number: "))
                        email = input("Enter E mail: ")

                        AddressBook.editContact(i, first_name, last_name, address, city, state, zip, number, email)
                        checkFlag = True

                if checkFlag == False:
                    print("Enter Valid Name!")

                elif checkFlag == True:
                    break

        elif check == 4:
            checkFlag = False
            while True:
                checkName = input("Enter First Name To Check Contact!")
                for i in range(AddressBook.contactLength):

                    if checkName == AddressBook.contact[i][0]:
                        AddressBook.deleteContact(i)
                        checkFlag = True

                if checkFlag == False:
                    print("Enter Valid Name!")

                elif checkFlag == True:
                    break

        elif check == 4:
            print("Thakyou!")
            break

        else:
            print("Enter Valid Input")