import time
import re
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

def get_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
def calc_size(size):
    KB, MB, GB = 1024, 1024**2, 1024**3
    if size < KB:
        return f"{size} Bytes"
    elif size < MB:
        return f"{round(size / KB, 2)} KB"
    elif size < GB:
        return f"{round(size / MB, 2)} MB"
    return f"{round(size / GB, 2)} GB"

def save_file(data, file_name):
    file_path = f"{file_name}.txt"
    clean_data = re.sub(r'\x1b\[[0-9;]*m', '', data)
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(clean_data)
    print(f"Saved at {file_path}")

def get_file_type(ext):
    types = {
        ".py": "Python",
        ".html": "HTML",
        ".css": "CSS",
        ".js": "JavaScript",
        ".json": "JSON",
        ".java": "Java",
        ".c": "C",
        ".cpp": "C++",
        ".yml": "YAML",
        ".yaml": "YAML",
        ".ts": "TypeScript",
        ".cs": "C#",
        ".php": "PHP",
        ".rb": "Ruby",
        ".go": "Go",
        ".rs": "Rust",
        ".swift": "Swift",
        ".kt": "Kotlin",
        ".dart": "Dart",
        ".sh": "Shell",
        ".xml": "XML",
        ".txt": "Text",
        ".md": "Markdown",
        ".png": "Image",
        ".jpg": "Image",
        ".jpeg": "Image",
        ".webp": "Image",
        ".mkv": "Video",
        ".mp4": "Video",
        ".mp3": "Audio",
        ".m4a": "Audio",
        ".zip": "Zip",
        ".toml": "TOML"
    }
    return types.get(ext.lower(), "Unknown")
def line(name, value):
    return (
        f"{Fore.GREEN + Style.BRIGHT + name:<28}"
        f"{Fore.WHITE}: "
        f"{Fore.CYAN + Style.BRIGHT + str(value)}"
    )
def auto_print(text="", color=Fore.WHITE, style=Style.NORMAL, delay=0.03):
    for char in str(text):
        print(style + color + char, end="",flush=True)
        time.sleep(delay)
    print()

def message(msg_type, text):
    styles = {
        "success": ( Fore.GREEN, Style.BRIGHT, "[SUCCESS]"),
        "error": (Fore.RED, Style.BRIGHT, "[ERROR]"),
        "warning": (Fore.YELLOW, Style.BRIGHT, "[WARNING]"),
        "info": (Fore.CYAN, Style.BRIGHT, "[INFO]")
    }
    color, style, prefix = styles.get(
        msg_type.lower(),
        (
            Fore.WHITE,
            Style.BRIGHT,
            "[INFO]"
        )
    )
    print()
    print(style + color + prefix + " " + str(text))
    print()

def divider(char="─", length=50, color=Fore.CYAN):
    print( color + (char * length))

def title(text):
    divider()
    print(Style.BRIGHT + Fore.CYAN + str(text))
    divider()
