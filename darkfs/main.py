import sys
from .cli import intro
from .core import main as cli_main

def main():
    if len(sys.argv) == 1:
        intro()
        cli_main()

    else:
        if sys.argv[1] in ["-h", "--help", "--version"]:
            cli_main()
        else:
            cli_main()
