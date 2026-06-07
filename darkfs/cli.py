from pyfiglet import Figlet
from colorama import init, Fore, Style
from .helpers import auto_print

def intro():
    init(autoreset=True)

    f = Figlet()

    dark_text = f.renderText("    Dark")
    fs_text = f.renderText(" FS")

    dark_lines = dark_text.splitlines()
    fs_lines = fs_text.splitlines()

    for d, f_line in zip(dark_lines, fs_lines):
        print(Style.BRIGHT + Fore.RED + d + Style.BRIGHT + Fore.YELLOW + f_line)

    print(Style.BRIGHT + "\t\t[+]" + Fore.YELLOW + " Author" + Style.RESET_ALL + " : " + Style.BRIGHT + "Mayank Sinha")
    print(Style.BRIGHT + "\t\t[+]" + Fore.YELLOW + " Version" + Style.RESET_ALL + " : " + Style.BRIGHT + "v0.2.1")
    print(Style.BRIGHT + "\t\t[+]" + Fore.YELLOW + " Github" + Style.RESET_ALL + " : " + Style.BRIGHT + "mayank-tech-official\n")

    auto_print(Fore.CYAN, Style.BRIGHT, "    Support Us To Add More Features.\n")

    print("    Dark-FS - Powerfull File System CLI Tool\n")
