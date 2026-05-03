import argparse
import shutil
import os
import sys
from colorama import Fore, init, Style

init(autoreset=True)

def main():
    commands = ["cp", "mv", "cf", "rn"]

    if len(sys.argv) > 1 and sys.argv[1] not in commands and not sys.argv[1].startswith("-"):
        print(f"dark-fs: '{sys.argv[1]}' is not a tst command. See 'dfs --help'.")
        return

    formatter = lambda prog: argparse.HelpFormatter(
        prog,
        indent_increment=4,
        max_help_position=25
    )

    parser = argparse.ArgumentParser(
        prog="dsd",
        description="A powerful CLI file sytem tool",
        formatter_class=formatter
    )

    parser.add_argument("--version", action="version", version="dark-fs 0.1.0")

    subparsers = parser.add_subparsers(dest="command")

    cp = subparsers.add_parser("cp", help="Copy a file", formatter_class=formatter)
    cp.add_argument("src")
    cp.add_argument("dest")

    mv = subparsers.add_parser("mv", help="Move a file", formatter_class=formatter)
    mv.add_argument("src")
    mv.add_argument("dest")

    cf = subparsers.add_parser("cf", help="Create a file", formatter_class=formatter)
    cf.add_argument("filename")
    cf.add_argument("dest", nargs="?", default=".")

    rn = subparsers.add_parser("rn", help="Rename a file", formatter_class=formatter)
    rn.add_argument("src")
    rn.add_argument("new_name")

    args = parser.parse_args()

    try:
        if args.command == "cp":
            shutil.copy(args.src, args.dest)
            print(Fore.YELLOW + Style.BRIGHT +  " File Copied Successfully")

        elif args.command == "mv":
            if os.path.isdir(args.dest):
                shutil.move(args.src, args.dest)
                print(Fore.YELLOW + Style.BRIGHT +  " File Moved Successfully")
            else:
                print(Fore.RED + Style.BRIGHT + " Error: Destination must be a directory")

        elif args.command == "cf":
            path = os.path.join(args.dest, args.filename)
            open(path, "w").close()
            print(Fore.YELLOW + Style.BRIGHT + " File Created Successfully")

        elif args.command == "rn":
            base = os.path.dirname(args.src)
            new_path = os.path.join(base, args.new_name)
            os.rename(args.src, new_path)
            print(Fore.YELLOW + Style.BRIGHT  + " File Renamed Successfully")

        else:
            help_text = parser.format_help()
            indented = "\n".join("    " + line for line in help_text.splitlines())
            print(indented)

    except Exception as e:
        print(Fore.RED + " Error: " + str(e))
