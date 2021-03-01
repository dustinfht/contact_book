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
    print(configuration.message_create_contact)
    last_name = None
    first_name = None
    number = None
    while True:
        if last_name is None:
            print(configuration.message_enter_last_name)
            last_name = get_last_name()
        elif first_name is None:
            print(configuration.message_enter_first_name)
            first_name = get_first_name()
        elif number is None:
            print(configuration.message_enter_phone_number)
            number = get_phone_number()
        else:
            break

        if last_name == "cancel" or first_name == "cancel" or number == "cancel":
            print(configuration.message_cancelled_create_contact)
            return

    dbConnector = DatabaseConnector("sqlite.db")
    dbConnector.connect()
    dbConnector.insert_entry(last_name, first_name, number)
    dbConnector.disconnect()
    print(configuration.message_created_contact)


def get_last_name():
    last_name = get_input().strip()
    if not last_name:
        print(configuration.message_last_name_must_not_be_empty)
        return get_last_name()
    return last_name


def get_first_name():
    first_name = get_input().strip()
    if not first_name:
        print(configuration.message_first_name_must_not_be_empty)
        return get_first_name()
    return first_name


def get_phone_number():
    phone_number = get_input().strip()
    if not phone_number:
        print(configuration.message_phone_number_must_not_be_empty)
        return get_phone_number()
    return phone_number


def show_delete_entry_context():
    print(configuration.message_enter_delete_contact_id)
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
