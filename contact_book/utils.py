from colors import Color


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def parse_string_color(string):
    if type(string) is not str:
        return string

    for key in Color.elements.keys():
        string = string.replace(f"<color:{key}>", Color.elements.get(key))

    return string



