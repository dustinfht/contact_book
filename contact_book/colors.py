class Color:
    RESET = "\u001b[0m"
    BLACK = "\u001b[30m"
    BRIGHT_BLACK = "\u001b[30;1m"
    RED = "\u001b[31m"
    BRIGHT_RED = "\u001b[31;1m"
    GREEN = "\u001b[32m"
    BRIGHT_GREEN = "\u001b[32;1m"
    YELLOW = "\u001b[33m"
    BRIGHT_YELLOW = "\u001b[33;1m"
    BLUE = "\u001b[34m"
    BRIGHT_BLUE = "\u001b[34;1m"
    MAGENTA = "\u001b[35m"
    BRIGHT_MAGENTA = "\u001b[35;1m"
    CYAN = "\u001b[36m"
    BRIGHT_CYAN = "\u001b[36;1m"
    WHITE = "\u001b[37m"
    BRIGHT_WHITE = "\u001b[37;1m"

    BOLD = "\u001b[1m"
    UNDERLINE = "\u001b[4m"
    REVERSED = "\u001b[7m"

    INFORMATION = CYAN
    SUCCESS = GREEN
    ERROR = RED

    elements = {"reset": RESET, "black": BLACK, "bright_black": BRIGHT_BLACK, "red": RED, "bright_red": BRIGHT_RED,
                "green": GREEN, "bright_green": BRIGHT_GREEN, "yellow": YELLOW, "bright_yellow": BRIGHT_YELLOW,
                "blue": BLUE, "bright_blue": BRIGHT_BLUE, "magenta": MAGENTA, "bright_magenta": BRIGHT_MAGENTA,
                "cyan": CYAN, "bright_cyan": BRIGHT_CYAN, "white": WHITE, "bright_white": BRIGHT_WHITE, "bold": BOLD,
                "underline": UNDERLINE, "reversed": REVERSED, "information": INFORMATION, "success": SUCCESS,
                "error": ERROR}
