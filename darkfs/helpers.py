import time
from colorama import Fore, Style, init

init(autoreset=True)

def auto_print(color=Fore.WHITE, style=Style.NORMAL, text="", delay=0.05):
    for char in text:
        print(style + color + char, end="")
        time.sleep(delay)
    print()

def message(msg_type, text):
    colors = {
        "Success": Fore.GREEN,
        "Error": Fore.RED,
        "Warning": Fore.YELLOW,
        "Info": Fore.CYAN
    }

    color = colors.get(msg_type, Fore.WHITE)

    print(f"{Style.BRIGHT}{color}{text}")
