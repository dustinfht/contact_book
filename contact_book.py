from database_connector import DatabaseConnector
from colors import Color
import sys


def main_loop():
    while True:
        print("Please select one option: [q]uit, [s]how entries, [n]ew entry, [d]elete entry, [u]pdate entry")
        user_selection = input("> ").lower()
        if user_selection == "q":
            quitProgram()
        elif user_selection == "s":
            context_show_entries()
        elif user_selection == "n":
            context_add_entry()
        elif user_selection == "d":
            context_delete_entry()


def context_show_entries():
    print(f"{Color.INFORMATION}Showing all book-entries:{Color.RESET}")
    dbConnector = DatabaseConnector("sqlite.db")
    dbConnector.connect()
    dbConnector.print_entries()
    dbConnector.disconnect()


def context_add_entry():
    print(f"{Color.INFORMATION}Please enter following information about your new friend:{Color.RESET}")
    print(f"Please enter the {Color.MAGENTA}last name{Color.RESET}:")
    last_name = input("> ")
    print(f"Please enter the {Color.MAGENTA}first name{Color.RESET}:")
    first_name = input("> ")
    print(f"Please enter the {Color.MAGENTA}phone number{Color.RESET}:")
    number = input("> ")
    dbConnector = DatabaseConnector("sqlite.db")
    dbConnector.connect()
    dbConnector.insert_entry(last_name, first_name, number)
    dbConnector.disconnect()
    print(f"{Color.SUCCESS}Your friend {first_name} was successfully added to your contacts!{Color.RESET}")


def context_delete_entry():
    print(f"{Color.INFORMATION}Please enter the id of the contact you want to delete:{Color.RESET}")
    contact_id = input("> ")
    if not is_int(contact_id):
        print("That is not an integer! Please only insert whole numbers.")
        context_delete_entry()

    contact_id = int(contact_id)
    if not contact_id > 0:
        print("That is not a valid id! Please only insert numbers greater than 0.")
        context_delete_entry()

    dbConnector = DatabaseConnector("sqlite.db")
    dbConnector.connect()
    dbConnector.delete_entry(contact_id)
    dbConnector.disconnect()

    print(f"{Color.SUCCESS}Successfully deleted entry with id {contact_id}.{Color.RESET}")


def quitProgram():
    print(f"\n{Color.ERROR}Exiting by user request.{Color.RESET}")
    sys.exit(0)


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    connector = DatabaseConnector("sqlite.db")
    connector.connect()
    connector.setup_tables()
    connector.disconnect()

    print()
    print("=======================================================================================================")
    print("Hello my friend! Haven't seen you for a while. I've wondered if you are okay.\nBut beside that I still "
          "managed your contacts. Let them know you are still alive!")
    print("=======================================================================================================")
    try:
        main_loop()
    except KeyboardInterrupt:
        quitProgram()
