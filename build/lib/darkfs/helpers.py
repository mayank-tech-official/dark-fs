import time
from colorama import Fore, Style, init

init(autoreset=True)


def auto_print(color=Fore.WHITE, style=Style.NORMAL, text="", delay=0.03):
    for char in text:
        print(style + color + char, end="")
        time.sleep(delay)
    print()


def message(msg_type, text):

    styles = {
        "success": (Fore.GREEN, "[SUCCESS]"),
        "error": (Fore.RED, "[ERROR]"),
        "warning": (Fore.YELLOW, "[WARNING]"),
        "info": (Fore.CYAN, "[INFO]")
    }

    color, prefix = styles.get(msg_type, (Fore.WHITE, "[INFO]"))

    print()
    print(color + prefix + " " + text)
    print()
