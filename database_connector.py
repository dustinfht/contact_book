import sqlite3


class DatabaseConnector:
    table_name = "contacts"

    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def setup_tables(self):
        sql = f"CREATE TABLE IF NOT EXISTS {self.table_name}(" \
              "last_name TEXT, " \
              "first_name TEXT, " \
              "phone_number TEXT, " \
              "last_updated TEXT);"
        self.cursor.execute(sql)

    def insert_entry(self, last_name, first_name, phone_number):
        sql = f"INSERT INTO {self.table_name} (last_name, first_name, phone_number, last_updated) VALUES ('{last_name}', '{first_name}', '{phone_number}', datetime('now'));"
        self.cursor.execute(sql)
        self.connection.commit()

    def print_entries(self):
        sql = f"SELECT * FROM {self.table_name};"
        self.cursor.execute(sql)

        for entry in self.cursor:
            print(entry[0], entry[1], entry[2], entry[3])

    def disconnect(self):
        print("Disconnect from database" + ("" if self.connection is not None else " which is null") + ".")
        self.connection.close()
