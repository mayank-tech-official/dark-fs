import argparse
import hashlib
import os
import shutil
import sys

from colorama import init, Fore
from .helpers import message

init(autoreset=True)


def get_file_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            sha256.update(chunk)

    return sha256.hexdigest()


def main():

    commands = ["cp", "mv", "cf", "rn", "swap", "dup"]

    if (
        len(sys.argv) > 1
        and sys.argv[1] not in commands
        and not sys.argv[1].startswith("-")
    ):
        message("error", f"'{sys.argv[1]}' is not a valid command. Use dfs --help")
        return

    formatter = lambda prog: argparse.HelpFormatter(
        prog,
        indent_increment=4,
        max_help_position=25
    )

    parser = argparse.ArgumentParser(
        prog="dfs",
        description="Dark-FS - Fast CLI File Manager",
        formatter_class=formatter
    )

    parser.add_argument("--version", action="version", version="dark-fs 0.2.0")

    subparsers = parser.add_subparsers(dest="command")

    # CP
    cp = subparsers.add_parser("cp", help="Copy file", formatter_class=formatter)
    cp.add_argument("src")
    cp.add_argument("dest")

    # MV
    mv = subparsers.add_parser("mv", help="Move file", formatter_class=formatter)
    mv.add_argument("src")
    mv.add_argument("dest")

    # CF
    cf = subparsers.add_parser("cf", help="Create file", formatter_class=formatter)
    cf.add_argument("filename")
    cf.add_argument("dest", nargs="?", default=".")

    # RN
    rn = subparsers.add_parser("rn", help="Rename file", formatter_class=formatter)
    rn.add_argument("src")
    rn.add_argument("new_name")

    # SWAP
    swap = subparsers.add_parser("swap", help="Swap files", formatter_class=formatter)
    swap.add_argument("file1")
    swap.add_argument("file2")

    # DUP
    dup = subparsers.add_parser("dup", help="Find duplicates", formatter_class=formatter)
    dup.add_argument("folder", nargs="?", default=".")

    args = parser.parse_args()

    try:

        if args.command == "cp":
            shutil.copy(args.src, args.dest)
            message("success", "File copied successfully")

        elif args.command == "mv":
            shutil.move(args.src, args.dest)
            message("success", "File moved successfully")

        elif args.command == "cf":
            path = os.path.join(args.dest, args.filename)
            open(path, "w").close()
            message("success", "File created successfully")

        elif args.command == "rn":
            base = os.path.dirname(args.src)
            new_path = os.path.join(base, args.new_name)
            os.rename(args.src, new_path)
            message("success", "File renamed successfully")

        elif args.command == "swap":

            if not os.path.exists(args.file1):
                message("error", f"'{args.file1}' not found")
                return

            if not os.path.exists(args.file2):
                message("error", f"'{args.file2}' not found")
                return

            if os.path.isdir(args.file1) or os.path.isdir(args.file2):
                message("error", "Folders cannot be swapped")
                return

            temp = args.file1 + ".tmp"

            os.rename(args.file1, temp)
            os.rename(args.file2, args.file1)
            os.rename(temp, args.file2)

            message("success", "Files swapped successfully")

        elif args.command == "dup":

            folder = args.folder

            if not os.path.exists(folder):
                message("error", "Folder does not exist")
                return

            if os.path.isfile(folder):
                message("error", "Path is a file, not folder")
                return

            files = [
                f for f in os.listdir(folder)
                if os.path.isfile(os.path.join(folder, f))
            ]

            if not files:
                message("info", "No files found")
                return

            hashes = {}
            found = False

            for file in files:
                path = os.path.join(folder, file)
                file_hash = get_file_hash(path)

                if file_hash in hashes:
                    found = True
                    message("warning", "Duplicate files found")

                    print(Fore.YELLOW + f"    ├─ {hashes[file_hash]}")
                    print(Fore.YELLOW + f"    └─ {file}\n")

                else:
                    hashes[file_hash] = file

            if not found:
                message("info", "No duplicates found")

        else:
            print(parser.format_help())

    except Exception as e:
        message("error", str(e))
