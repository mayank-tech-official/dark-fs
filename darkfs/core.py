import argparse
import difflib
import hashlib
import os
import shutil
import sys
from pathlib import Path
from colorama import init, Fore, Style

from .helpers import (
    get_time,
    calc_size,
    save_file,
    get_file_type,
    line,
    message
)

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
    commands = ["cp", "mv", "cf", "rn", "swap", "fd", "ds", "inf"]
    if (len(sys.argv) > 1 and sys.argv[1] not in commands and not sys.argv[1].startswith("-")):
        suggestion = difflib.get_close_matches(sys.argv[1], commands, n=1)
        if suggestion:
            message("error", f"Unknown command '{sys.argv[1]}'. Did you mean '{suggestion[0]}'?")
        else:
            message("error", f"Unknown command '{sys.argv[1]}'. Use 'dfs --help'")
        return
    formatter = lambda prog: argparse.HelpFormatter(prog, indent_increment=4, max_help_position=25)
    parser = argparse.ArgumentParser(prog="dfs", description="Dark-FS - Fast CLI File Manager", formatter_class=formatter)
    parser.add_argument("--version", action="version", version="dark-fs 0.3.0")
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
    # FD
    fd = subparsers.add_parser("fd", help="Find duplicates", formatter_class=formatter)
    fd.add_argument("folder", nargs="?", default=".")
    # DS
    ds = subparsers.add_parser("ds", help="Show the directory structure", formatter_class=formatter)
    ds.add_argument("dir")
    # INF
    inf = subparsers.add_parser("inf", help="Show the information of file or folder", formatter_class=formatter)
    inf.add_argument("dof")
    inf.add_argument("-s", "--save", help="Save the information in given file")
    
    # Executions Logic
    args = parser.parse_args()
    if args.command is None:
        help_text = parser.format_help()
        print("    " + help_text.replace("\n", "\n    "))
        return
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
        elif args.command == "fd":
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
        elif args.command == "ds":
            if not os.path.exists(args.dir):
                print(Fore.RED + Style.BRIGHT + "Directory not found!")
                return
            if not os.path.isdir(args.dir):
                print(Fore.RED + Style.BRIGHT + "Path is not a directory!")
                return
            print("\n" + Fore.YELLOW + Style.BRIGHT + os.path.basename(os.path.abspath(args.dir)))
            def show_tree(directory, prefix=""):
                try:
                    items = sorted(os.listdir(directory))
                except PermissionError:
                    print(prefix + Fore.RED + Style.BRIGHT + "└── Permission Denied")           
                    return
                for index, item in enumerate(items):
                    path = os.path.join(directory, item)
                    is_last = index == len(items) - 1
                    connector = ("└── " if is_last else "├── ")
                    if os.path.isdir(path):
                        print(prefix + Fore.CYAN + Style.BRIGHT + connector + Fore.YELLOW + Style.BRIGHT + item)
                        new_prefix = prefix + ( "    " if is_last else Fore.CYAN + Style.BRIGHT + "│   ")
                        show_tree(path, new_prefix)
                    else:
                        print(prefix + Fore.CYAN + Style.BRIGHT + connector + Fore.WHITE + Style.BRIGHT + item)
            show_tree(args.dir)
        elif args.command == "inf":
            def info(dof):
                data = ""
                path = Path(dof)
                if not path.exists():
                    return f"{Fore.RED}Path does not exist."
                created_time = get_time(path.stat().st_ctime)
                if path.is_dir():
                    folder_name = path.resolve().name
                    total_files = sum(1 for item in path.rglob("*") if item.is_file())
                    total_folders = sum(1 for item in path.rglob("*") if item.is_dir())
                    total_size = sum(file.stat().st_size for file in path.rglob("*") if file.is_file())
                    files = [file for file in path.rglob("*") if file.is_file()]
                    empty_files = [file.name for file in path.rglob("*") if file.is_file() and file.stat().st_size == 0]
                    if files:
                        largest_file = max(files, key=lambda x: x.stat().st_size)
                        largest_text = (f"{largest_file.name} "f"({calc_size(largest_file.stat().st_size)})")
                        last_file = max(files, key=lambda x: x.stat().st_mtime)
                        last_modified = last_file.name
                        modified = get_time(last_file.stat().st_mtime)
                    else:
                        largest_text = "None"
                        last_modified = "None"
                        modified = "None"
                    if not empty_files:
                        empty_files_text = "No Empty Files"
                    else:
                        empty_files_text = ", ".join(empty_files)
                    data = f"""
    {Fore.WHITE + Style.BRIGHT + "Folder Information"}
{Fore.WHITE + "------------------------------"}
 {line("Folder Name", folder_name)}
 {line("Folder Path", path.resolve())}
 {line("Files Inside", total_files)}
 {line("Folders Inside", total_folders)}
 {line("Created Time", created_time)}
 {line("Last Modified File", last_modified)}
 {line("Modified Time", modified)}
 {line("Folder Size", calc_size(total_size))}
 {line("Largest File", largest_text)}
 {line("Empty Files", empty_files_text)}
{Fore.WHITE + "------------------------------\n"}
"""
                    return data
                elif path.is_file():
                    ext = path.suffix
                    file_type = get_file_type(ext)
                    file_size = calc_size(path.stat().st_size)
                    modified = get_time(path.stat().st_mtime)
                    data = f"""
{Fore.WHITE + Style.BRIGHT + "File Information"}
{Fore.WHITE + "------------------------------"}
 {line("File Name", path.name)}
 {line("File Type", file_type)}
 {line("File Size", file_size)}
 {line("Created Time", created_time)}
 {line("Modified Time", modified)}
{Fore.WHITE + "------------------------------"}
"""
                return data
            data = info(args.dof)
            print(data)
            if args.save:
                save_file(data, args.save)
                message("success", f"Saved to '{args.save}'")           
    except Exception as e:
        message("error", str(e))
