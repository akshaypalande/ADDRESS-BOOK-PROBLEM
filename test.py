import unittest
import AddressBookMain

class TestAddressBook(unittest.TestCase):
    contact = {}
    contactLength = len(contact)
    contactInListLength = 0
    contactList = []

    def test_addContact(self):
       
        TestAddressBook.contact = AddressBookMain.AddressBook.addContact("Akshay","Palande","Virar","Mumbai","Maharashtra",405326,9876543210,"akshay@gmail")
        self.assertEqual(TestAddressBook.contact[0],["Akshay","Palande","Virar","Mumbai","Maharashtra",405326,9876543210,"akshay@gmail"])

    def test_multipleAddContact_length(self):
        
        TestAddressBook.contact=AddressBookMain.AddressBook.addContact("rahul","oberoi","Pundur","Patna","Maharashtra",456324,9876543210,"kasmir@gmail.com")
        contactLength = len(TestAddressBook.contact)
        self.assertEqual(contactLength, 2)

    def test_editContact(self):
        
        TestAddressBook.contact = AddressBookMain.AddressBook.editContact(0,"Akshay","Palande","Virar","Mumbai","Maharashtra",405326,9876543210,"akshay@gmail")
        self.assertEqual(TestAddressBook.contact[0],["Akshay","Palande","Virar","Mumbai","Maharashtra",405326,9876543210,"akshay@gmail"])


    def test_deleteContact(self):
        
        contactLengthCheck = len(TestAddressBook.contact)
        TestAddressBook.contact = AddressBookMain.AddressBook.deleteContact(0)
        self.assertEqual(len(TestAddressBook.contact),contactLengthCheck-1)
        
        
        
        
        
        
        
        


if __name__ == "__main__":
    unittest.main()