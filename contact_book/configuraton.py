from configparser import ConfigParser
import utils
import os


class Configuration:
    message_enter_last_name = None

    def load(self):
        config_parser = ConfigParser()
        config_parser.read(os.path.join(os.path.dirname(__file__), '../config.cfg'))
        self.message_enter_last_name = utils.parse_string(config_parser.get("messages", "enter_last_name"))
