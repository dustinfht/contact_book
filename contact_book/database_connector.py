import sqlite3
from prettytable import PrettyTable
import os
import contact


class DatabaseConnector:
    table_name = "contacts"

    def __init__(self, database_name):
        self.database_name = os.path.join(os.path.dirname(os.path.dirname(__file__)), database_name)
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def setup_tables(self):
        sql = f"CREATE TABLE IF NOT EXISTS {self.table_name}(" \
              "id INTEGER PRIMARY KEY, " \
              "last_name TEXT, " \
              "first_name TEXT, " \
              "phone_number TEXT, " \
              "last_updated TEXT);"
        self.cursor.execute(sql)

    def insert_entry(self, last_name, first_name, phone_number):
        sql = f"INSERT INTO {self.table_name} (last_name, first_name, phone_number, last_updated)" \
              f" VALUES ('{last_name}', '{first_name}', '{phone_number}', datetime('now'));"
        self.cursor.execute(sql)
        self.connection.commit()

    def print_entries(self):
        sql = f"SELECT * FROM {self.table_name};"
        self.cursor.execute(sql)

        table = PrettyTable()
        table.field_names = ["ID", "Last Name", "First Name", "Number", "Updated on"]

        for entry in self.cursor:
            contact1 = contact.create(entry)
            table.add_row([contact1.contact_id, contact1.last_name, contact1.first_name, contact1.phone_number,
                           contact1.last_updated])

        print(table)

    def delete_entry(self, contact_id):
        sql = f"DELETE FROM {self.table_name} WHERE id = {contact_id};"
        self.cursor.execute(sql)
        self.connection.commit()

    def get_entry(self, contact_id):
        sql = f"SELECT * FROM {self.table_name} WHERE id = {contact_id} LIMIT 1;"
        self.cursor.execute(sql)

        for entry in self.cursor:
            return contact.create(entry)

    def disconnect(self):
        self.connection.close()
