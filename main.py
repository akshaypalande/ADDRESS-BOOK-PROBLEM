"""
@Author: Akshay Palande
@Date: 2022-05-22 4:00:00
@Last Modified By: Akshay Palande
@Last Modified Date: 2022-05-22 4:00:00
@Title: Address Book Program

"""

from UC import AddressBookMain
from File import AddressBookFileService
from Console_System import AddressBookConsoleService

ADD_CONTACT = 1
DISPLAY_CONTACT = 2
EDIT_CONTACT = 3
DELETE_CONTACT = 4
SEARCH_BY_CITY_OR_STATE = 5
VIEW_BY_CITY_OR_STATE = 6
COUNT_BY_CITY_OR_STATE = 7
SORT_BY_PERSON_NAME = 8
SORT_BY_LOCATION = 9
WRITING_IN_JSON = 10
READ_FROM_JSON = 11
WRITING_IN_CSV = 12
READ_FROM_CSV = 13
EXIT = 0

if __name__ == "__main__":

    console_service = AddressBookConsoleService()
    file_service = AddressBookFileService()
    print("Welcome to Address Book Management System")

    while True:
        print("\n What you like to do ...?"
        "\n 1  Add Contact "
        "\n 2  Display Contact"
        "\n 3  Edit Contact"
        "\n 4  Delete Contact"
        "\n 5  Search by City or State"
        "\n 6  View Person by City or State"
        "\n 7  Count number of contacts having same city or state"
        "\n 8  Sort contact by name"
        "\n 9  Sort contact by location"
        "\n 10 Writing in json file"
        "\n 11 Read from json file"
        "\n 12 Writing in csv file"
        "\n 13 Read from csv file"
        "\n 0  Exit")
        user_choice = int(input())

        if user_choice == ADD_CONTACT:
            console_service.add_contact()

        elif user_choice == DISPLAY_CONTACT:
            console_service.display_contact()

        elif user_choice == EDIT_CONTACT:
            console_service.edit_contact()

        elif user_choice == DELETE_CONTACT:
            console_service.delete_contact()

        elif user_choice == SEARCH_BY_CITY_OR_STATE:
            console_service.search_person_by_location()

        elif user_choice == VIEW_BY_CITY_OR_STATE:
            console_service.view_person_by_location()
        
        elif user_choice == COUNT_BY_CITY_OR_STATE:
            console_service.count_number_of_contact_by_location()

        elif user_choice == SORT_BY_PERSON_NAME:
            console_service.sort_by_person_name()

        elif user_choice == SORT_BY_LOCATION:
            console_service.sort_by_location()

        elif user_choice == WRITING_IN_JSON:
            file_service.write_in_json()

        elif user_choice == READ_FROM_JSON:
            file_service.read_from_json()

        elif user_choice == WRITING_IN_CSV:
            file_service.write_in_csv()
        
        elif user_choice == READ_FROM_CSV:
            file_service.read_from_csv()

        elif user_choice == EXIT:
            print("Thanks for using us ")
            exit()

        else:
            print("Invalid choice")