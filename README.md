# 🌑 Dark FS

Dark FS is a lightweight and fast command-line file manager built with Python.

It provides useful file-system operations such as copying, moving, renaming, swapping files, finding duplicates, displaying directory trees, and viewing detailed information about files and folders.

Designed to be simple, powerful, and beginner-friendly while remaining useful for everyday terminal work.

---

## ✨ Features

### File Operations

- Copy files
- Move files
- Create files
- Rename files
- Swap files

### Analysis Tools

- Find duplicate files using SHA-256 hashing
- Display directory structure in tree format
- Show detailed file information
- Show detailed folder information
- Detect empty files
- Find the largest file in a folder
- Calculate total folder size

### Additional Features

- Save information output to a text file
- Command suggestions for mistyped commands
- Colored terminal output
- Fast and lightweight

---

## 🚀 Installation

Install from PyPI:

```bash
pip install dark-fs
```

Upgrade to the latest version:

```bash
pip install --upgrade dark-fs
```

Verify installation:

```bash
dfs --version
```

---

## 📦 Current Version

```text
0.3.0
```

---

## 🛠 Commands

### Copy File

```bash
dfs cp source.txt destination.txt
```

Copies a file to another location.

---

### Move File

```bash
dfs mv source.txt destination.txt
```

Moves a file to another location.

---

### Create File

```bash
dfs cf myfile.txt
```

Creates a new file in the current directory.

Create inside another directory:

```bash
dfs cf myfile.txt folder
```

---

### Rename File

```bash
dfs rn old.txt new.txt
```

Renames a file.

---

### Swap Files

```bash
dfs swap file1.txt file2.txt
```

Swaps two files.

---

### Find Duplicate Files

Search current folder:

```bash
dfs fd
```

Search a specific folder:

```bash
dfs fd myfolder
```

Duplicate files are detected using SHA-256 hashes.

---

### Show Directory Structure

```bash
dfs ds folder
```

Example:

```text
Project
├── main.py
├── README.md
└── src
    └── helpers.py
```

---

### Show File Information

```bash
dfs inf example.txt
```

---

### Show Folder Information

```bash
dfs inf project
```

---

### Save Information to a File

```bash
dfs inf project -s report.txt
```

---

## 📁 Folder Information

The `inf` command displays the following information for folders:

- Folder Name
- Folder Path
- Total Files
- Total Folders
- Created Time
- Last Modified File
- Modified Time
- Folder Size
- Largest File
- Empty Files

Example:

```text
Folder Information
------------------------------
Folder Name        : Project
Folder Path        : /storage/emulated/0/Project
Files Inside       : 18
Folders Inside     : 4
Created Time       : 2026-06-15 12:30:20
Last Modified File : main.py
Modified Time      : 2026-06-15 14:10:55
Folder Size        : 12.8 MB
Largest File       : archive.zip (8.2 MB)
Empty Files        : notes.txt
------------------------------
```

---

## 📄 File Information

The `inf` command displays the following information for files:

- File Name
- File Type
- File Size
- Created Time
- Modified Time

Example:

```text
File Information
------------------------------
File Name      : main.py
File Type      : Python Source File
File Size      : 8.4 KB
Created Time   : 2026-06-15 10:20:11
Modified Time  : 2026-06-15 14:15:45
------------------------------
```

---

## 🔍 Duplicate Detection

Dark FS uses SHA-256 hashing to detect duplicate files.

Process:

```text
File → SHA-256 Hash
File → SHA-256 Hash

Same Hash = Duplicate File
```

This approach is much more reliable than comparing only file names or file sizes.

---

## 🧰 Technologies Used

### Language

```text
Python 3
```

### Standard Library Modules

```text
argparse
difflib
hashlib
os
pathlib
shutil
sys
```

### External Libraries

```text
colorama and pyfiglet
```

---

## 📂 Project Structure

```text
dark-fs/
│
├── LICENSE
├── README.md
├── pyproject.toml
│
├── darkfs/
│   ├── __init__.py
│   ├── core.py
│   ├── main.py
│   ├── cli.py
│   └── helpers.py
│
└── .github/
    └── workflows/
        └── publish.yml
```

---

## 🎯 Roadmap

### Planned Features

- Delete file command
- Delete folder command
- Folder copy support
- Folder move support
- File search command
- Export to JSON
- Export to CSV
- Progress bars
- Better reporting
- Interactive mode

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to open an issue or submit a pull request if you find a bug or want to improve the project.

---

## 👨‍💻 Author

```text
Mayank Sinha
```

Creator of Dark FS.

---

## 📜 License

```text
MIT License
```

---

## ⭐ Why Dark FS?

- Lightweight
- Fast
- Easy to use
- Beginner-friendly
- Useful daily file-management commands
- Clean terminal output
- Open Source

---

## 💡 Example Workflow

```bash
# Create a file
dfs cf notes.txt

# Rename it
dfs rn notes.txt ideas.txt

# View information
dfs inf ideas.txt

# Find duplicates
dfs fd .

# Show project tree
dfs ds .

# Save folder report
dfs inf . -s report.txt
```

---

```text
Dark FS
Fast • Simple • Lightweight
```
