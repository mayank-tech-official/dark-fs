# Dark FS

Dark FS is a cross-platform command-line file management tool built with Python. It provides a simple and colorful interface for performing common file operations directly from the terminal.

## Features

- Copy files
- Move files
- Create files
- Rename files
- Swap two files
- Find duplicate files
- Colored terminal output
- Cross-platform support
- Simple command structure

## Installation

```bash
pip install dark-fs
```

## Usage

### Show Help

```bash
dfs --help
```

### Show Version

```bash
dfs --version
```

## Commands

### Copy File

```bash
dfs cp source.txt destination.txt
```

### Move File

```bash
dfs mv source.txt destination_folder
```

### Create File

```bash
dfs cf hello.txt
```

Create file in a specific folder:

```bash
dfs cf hello.txt Documents
```

### Rename File

```bash
dfs rn old.txt new.txt
```

### Swap Two Files

```bash
dfs swap file1.txt file2.txt
```

Swaps the names of two files safely.

### Find Duplicate Files

Current directory:

```bash
dfs duplicate .
```

Specific folder:

```bash
dfs duplicate Downloads
```

Dark FS compares file contents using SHA-256 hashes and reports duplicate files.

## Examples

```bash
dfs cp notes.txt backup.txt

dfs mv image.png Images

dfs cf index.html

dfs rn draft.txt final.txt

dfs swap photo.jpg image.jpg

dfs duplicate Downloads
```

## Project Structure

```
dark-fs/
├── LICENSE
├── README.md
├── pyproject.toml
├── .github/
│   └── workflows/
│       └── publish.yml
└── darkfs/
    ├── __init__.py
    ├── main.py
    ├── core.py
    ├── cli.py
    └── helpers.py
```

## Requirements

- Python 3.8+
- colorama
- pyfiglet

## Installation From Source

```bash
git clone https://github.com/mayank-tech-official/dark-fs.git

cd dark-fs

pip install .
```

## Release Notes

### v0.2.0

Added:
- swap command
- duplicate command
- improved terminal message system

### v0.1.0

Initial release:
- cp command
- mv command
- cf command
- rn command

## Author

Mayank Sinha

GitHub:
https://github.com/mayank-tech-official

## License

MIT License
