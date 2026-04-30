def main():
    from pyfiglet import Figlet
    from colorama import init, Fore, Style

    init(autoreset=True)

    f = Figlet(font="slant")

    dark_text = f.renderText("Dark")
    fs_text = f.renderText("FS")

    dark_lines = dark_text.splitlines()
    fs_lines = fs_text.splitlines()

    for d, f_line in zip(dark_lines, fs_lines):
        print(Style.BRIGHT + Fore.BLUE + d + Style.NORMAL + Fore.YELLOW + f_line)
