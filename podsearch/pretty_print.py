"""
File         : pretty_print.py
Description  :

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 18-Nov-2020
"""

from enum import Enum


# ---------------------------------------------------------------------------------------------------------------------

class AnsiColor(Enum):
    BLACK = '\033[30m'
    RED = '\033[31m'
    BOLD_RED = '\033[1;31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    CYANBOLD = '\033[1;36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'


def pprint(text: str, color: AnsiColor):
    print(f'{color.value}{text}{AnsiColor.RESET.value}')


class ColorPrint():

    @staticmethod
    def red(text: str):
        pprint(text, AnsiColor.RED)

    @staticmethod
    def green(text: str):
        pprint(text, AnsiColor.GREEN)

    @staticmethod
    def blue(text: str):
        pprint(text, AnsiColor.BLUE)

    @staticmethod
    def magenta(text: str):
        pprint(text, AnsiColor.MAGENTA)

    @staticmethod
    def cyan(text: str):
        pprint(text, AnsiColor.CYANBOLD)
