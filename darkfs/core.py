import argparse
import hashlib
import os
import shutil
import sys

from colorama import init
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

    commands = [
        "cp",
        "mv",
        "cf",
        "rn",
        "swap",
        "duplicate"
    ]

    if (
        len(sys.argv) > 1
        and sys.argv[1] not in commands
        and not sys.argv[1].startswith("-")
    ):
        message(
            "error",
            f"dark-fs: '{sys.argv[1]}' is not a valid command. See 'dfs --help'."
        )
        return

    formatter = lambda prog: argparse.HelpFormatter(
        prog,
        indent_increment=4,
        max_help_position=25
    )

    parser = argparse.ArgumentParser(
        prog="dfs",
        description="A powerful CLI file system tool",
        formatter_class=formatter
    )

    parser.add_argument(
        "--version",
        action="version",
        version="dark-fs 0.2.0"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Copy

    cp = subparsers.add_parser(
        "cp",
        help="Copy a file",
        formatter_class=formatter
    )

    cp.add_argument("src")
    cp.add_argument("dest")

    # Move

    mv = subparsers.add_parser(
        "mv",
        help="Move a file",
        formatter_class=formatter
    )

    mv.add_argument("src")
    mv.add_argument("dest")

    # Create File

    cf = subparsers.add_parser(
        "cf",
        help="Create a file",
        formatter_class=formatter
    )

    cf.add_argument("filename")
    cf.add_argument("dest", nargs="?", default=".")

    # Rename

    rn = subparsers.add_parser(
        "rn",
        help="Rename a file",
        formatter_class=formatter
    )

    rn.add_argument("src")
    rn.add_argument("new_name")

    # Swap

    swap = subparsers.add_parser(
        "swap",
        help="Swap two files",
        formatter_class=formatter
    )

    swap.add_argument("file1")
    swap.add_argument("file2")

    # Duplicate

    duplicate = subparsers.add_parser(
        "duplicate",
        help="Find duplicate files",
        formatter_class=formatter
    )

    duplicate.add_argument(
        "folder",
        nargs="?",
        default="."
    )

    args = parser.parse_args()

    try:

        if args.command == "cp":

            shutil.copy(args.src, args.dest)

            message(
                "success",
                "File Copied Successfully"
            )

        elif args.command == "mv":

            shutil.move(args.src, args.dest)

            message(
                "success",
                "File Moved Successfully"
            )

        elif args.command == "cf":

            path = os.path.join(
                args.dest,
                args.filename
            )

            open(path, "w").close()

            message(
                "success",
                "File Created Successfully"
            )

        elif args.command == "rn":

            base = os.path.dirname(args.src)

            new_path = os.path.join(
                base,
                args.new_name
            )

            os.rename(
                args.src,
                new_path
            )

            message(
                "success",
                "File Renamed Successfully"
            )

        elif args.command == "swap":

            if not os.path.exists(args.file1):
                message(
                    "error",
                    f"'{args.file1}' does not exist"
                )
                return

            if not os.path.exists(args.file2):
                message(
                    "error",
                    f"'{args.file2}' does not exist"
                )
                return

            if os.path.isdir(args.file1):
                message(
                    "error",
                    f"'{args.file1}' is a folder, not a file"
                )
                return

            if os.path.isdir(args.file2):
                message(
                    "error",
                    f"'{args.file2}' is a folder, not a file"
                )
                return

            temp = args.file1 + ".dfs_tmp"

            os.rename(args.file1, temp)
            os.rename(args.file2, args.file1)
            os.rename(temp, args.file2)

            message(
                "success",
                "Files Swapped Successfully"
            )

        elif args.command == "duplicate":

            folder = args.folder

            if not os.path.exists(folder):

                message(
                    "error",
                    f"Folder '{folder}' does not exist"
                )

                return

            if os.path.isfile(folder):

                message(
                    "error",
                    f"'{folder}' is a file, not a folder"
                )

                return

            files = [
                f for f in os.listdir(folder)
                if os.path.isfile(
                    os.path.join(folder, f)
                )
            ]

            if not files:

                message(
                    "info",
                    "No files found in folder"
                )

                return

            hashes = {}
            found = False

            for file in files:

                path = os.path.join(
                    folder,
                    file
                )

                file_hash = get_file_hash(path)

                if file_hash in hashes:

                    if not found:
                        found = True

                    message(
                        "warning",
                        "Duplicate Found:"
                    )

                    print(
                        f"  {hashes[file_hash]}"
                    )

                    print(
                        f"  {file}\n"
                    )

                else:

                    hashes[file_hash] = file

            if not found:

                message(
                    "info",
                    "No duplicate files found"
                )

        else:

            help_text = parser.format_help()

            indented = "\n".join(
                "    " + line
                for line in help_text.splitlines()
            )

            print(indented)

    except Exception as e:

        message(
            "error",
            str(e)
        )
