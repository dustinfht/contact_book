from database_connector import DatabaseConnector
from colors import Color
import sys
import utils
from configuraton import Configuration

configuration = Configuration()


def main_loop():
    while True:
        print(configuration.message_select_context)
        user_selection = get_input().lower()
        if user_selection == "q" or user_selection == "quit":
            quitProgram()
        elif user_selection == "l" or user_selection == "list":
            show_list_entries_context()
        elif user_selection == "n" or user_selection == "new":
            show_add_entry_context()
        elif user_selection == "d" or user_selection == "delete":
            show_delete_entry_context()


def show_list_entries_context():
    print(f"{Color.INFORMATION}Showing all book-entries:{Color.RESET}")
    dbConnector = DatabaseConnector("sqlite.db")
    dbConnector.connect()
    dbConnector.print_entries()
    dbConnector.disconnect()


def show_add_entry_context():
    print(f"Please enter following information about your new friend:{Color.RESET}")
    print(configuration.message_enter_last_name)
    last_name = get_last_name()
    print(f"Please enter the {Color.MAGENTA}first name{Color.RESET}:")
    first_name = get_first_name()
    print(f"Please enter the {Color.MAGENTA}phone number{Color.RESET}:")
    number = get_phone_number()
    dbConnector = DatabaseConnector("sqlite.db")
    dbConnector.connect()
    dbConnector.insert_entry(last_name, first_name, number)
    dbConnector.disconnect()
    print(f"{Color.SUCCESS}Your friend {first_name} was successfully added to your contacts!{Color.RESET}")


def get_last_name():
    last_name = get_input().strip()
    if not last_name:
        print(f"Your friends name must not be empty. Please enter his last name:")
        return get_last_name()
    return last_name


def get_first_name():
    first_name = get_input().strip()
    if not first_name:
        print(f"Your friends name must not be empty. Please enter his first name:")
        return get_first_name()
    return first_name


def get_phone_number():
    phone_number = get_input().strip()
    if not phone_number:
        print(f"Your friends phone number must not be empty. Please enter his phone number")
        return get_phone_number()
    return phone_number


def show_delete_entry_context():
    print(f"{Color.INFORMATION}Please enter the id of the contact you want to delete:{Color.RESET}")
    contact_id = get_input()

    if not utils.is_int(contact_id):
        print("That is not an integer! Please only insert whole numbers.")
        show_delete_entry_context()

    contact_id = int(contact_id)
    if not contact_id > 0:
        print("That is not a valid id! Please only insert numbers greater than 0.")
        show_delete_entry_context()

    dbConnector = DatabaseConnector("sqlite.db")
    dbConnector.connect()
    contact = dbConnector.get_entry(contact_id)
    if contact is None:
        print(f"{Color.ERROR}There is no contact with the id {contact_id}.")
        dbConnector.disconnect()
        show_delete_entry_context()

    dbConnector.delete_entry(contact_id)
    dbConnector.disconnect()

    print(f"{Color.SUCCESS}Successfully deleted entry with id {contact_id}.{Color.RESET}")


def quitProgram():
    print(f"\n{Color.ERROR}Exiting by user request.{Color.RESET}")
    sys.exit(0)


def get_input():
    print(f"{configuration.settings_input}", end='')
    user_input = input()
    print(Color.RESET, end='')
    return user_input


if __name__ == '__main__':
    connector = DatabaseConnector("sqlite.db")
    connector.connect()
    connector.setup_tables()
    connector.disconnect()

    # print()
    # print("=======================================================================================================")
    # print("Hello my friend! Haven't seen you for a while. I've wondered if you are okay.\nBut beside that I still "
    #       "managed your contacts. Let them know you are still alive!")
    # print("=======================================================================================================")
    print(configuration.message_greetings)
    try:
        main_loop()
    except KeyboardInterrupt:
        quitProgram()
