# add_contact
# display_contact
# edit_contact
# delete_contact
# def search_by_first_name
# search_person_by_location
# view_person_by_location
# count_number_of_contact_by_location
# contact_founder
# sort_by_person_name
# sort_by
# sort_by_location


import unittest
from Console_System import AddressBookConsoleService

class TestAddressBook(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        self.book=AddressBookConsoleService()

    def test_add_contact(self, *args, **kwargs):
        self.book.display_contact("niki","Khapare","Chandur","Amravati","Maharashtra",444726,9075194857,"nikitakhapare53@gmail.com")
        self.book.display_contact("rk","Khapa","chandrapur","Chandrpur","mh",56566,1482415625,"nikikhapare@gmail.com")
        self.assertEqual(len(self.book.contact),1)


if __name__ == "__main__":
    unittest.main()
