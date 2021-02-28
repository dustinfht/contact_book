from database_connector import DatabaseConnector


def main():
    print("Starting contact_book...")
    connector = DatabaseConnector("sqlite.db")
    connector.connect()
    print("Connected to database.")
    connector.setup_tables()
    print("Printing entries....")
    print("=======================")
    connector.print_entries()
    print("=======================")
    print("Entries printed.")
    print("Filling database with content...")
    connector.insert_entry("Müller", "Max", "0123456789")
    print("Filled database with content.")
    print("Printing entries....")
    print("=======================")
    connector.print_entries()
    print("=======================")
    print("Entries printed.")
    connector.disconnect()


if __name__ == '__main__':
    try:
        main()
    finally:
        print("Program exit..")
