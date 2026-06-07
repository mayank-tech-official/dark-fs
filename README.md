# 🚀 Dark FS

Dark FS is a fast, lightweight and cross-platform command-line file manager built with Python.  
It helps you perform daily file operations quickly using simple commands.

---

## ✨ Features

- 📁 Copy files  
- 📦 Move files  
- 🆕 Create files  
- ✏️ Rename files  
- 🔄 Swap two files  
- 🔍 Detect duplicate files (via SHA256)  
- 🎨 Colored terminal output  
- ⚡ Fast CLI performance  

---

## 📦 Installation

```bash
pip install dark-fs
```

---

## ⚙️ Usage

### Show help
```bash
dfs --help
```

### Show version
```bash
dfs --version
```

---

## 📂 Commands

### 📄 Copy file
```bash
dfs cp file1.txt file2.txt
```

---

### 📦 Move file
```bash
dfs mv file.txt folder/
```

---

### 🆕 Create file
```bash
dfs cf file.txt
```

Create in folder:
```bash
dfs cf file.txt Documents
```

---

### ✏️ Rename file
```bash
dfs rn old.txt new.txt
```

---

### 🔄 Swap files
```bash
dfs swap file1.txt file2.txt
```

---

### 🔍 Find duplicates
Current folder:
```bash
dfs dup .
```

Specific folder:
```bash
dfs dup Downloads
```

---

## 🧠 How duplicate detection works

Dark FS uses **SHA256 hashing** to compare file contents.  
Even if filenames are different, identical content will be detected.

---

## 📁 Example

```bash
dfs cp a.txt b.txt
dfs mv a.txt Docs/
dfs cf new.txt
dfs rn old.txt new.txt
dfs swap a.txt b.txt
dfs dup .
```

---

## 🏗 Project Structure

```
darkfs/
├── main.py
├── core.py
├── cli.py
├── helpers.py
└── __init__.py
```

---

## 📌 Requirements

- Python 3.8+
- colorama

---

## 🚀 Version

```
v0.2.0
```

---

## 👨‍💻 Author

Mayank Sinha  
GitHub: https://github.com/mayank-tech-official

---

## 📜 License

MIT License
