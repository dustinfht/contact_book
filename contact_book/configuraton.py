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

        self.settings_input = self.__get("settings", "input")

    def __get(self, section, path):
        return utils.parse_string_color(self.__config_parser.get(section, path))
