from configparser import ConfigParser
import utils
import os


class Configuration:

    def __init__(self):
        self.__config_parser = ConfigParser()
        self.__config_parser.read(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.cfg'))
        self.message_enter_last_name = self.__get("messages", "enter_last_name")
        self.message_enter_first_name = self.__get("messages", "enter_first_name")
        self.message_enter_phone_number = self.__get("messages", "enter_phone_number")
        self.message_enter_id = self.__get("messages", "enter_id")
        self.message_select_context = self.__get("messages", "select_context")
        self.message_greetings = self.__get("messages", "greetings")
        self.message_create_contact = self.__get("messages", "create_contact")
        self.message_cancelled_create_contact = self.__get("messages", "cancelled_create_contact")
        self.message_created_contact = self.__get("messages", "created_contact")
        self.message_last_name_must_not_be_empty = self.__get("messages", "last_name_must_not_be_empty")
        self.message_first_name_must_not_be_empty = self.__get("messages", "first_name_must_not_be_empty")
        self.message_phone_number_must_not_be_empty = self.__get("messages", "phone_number_must_not_be_empty")
        self.message_enter_delete_contact_id = self.__get("messages", "enter_delete_contact_id")

        self.settings_input = self.__get("settings", "input")

    def __get(self, section, path):
        return utils.parse_string_color(self.__config_parser.get(section, path))
