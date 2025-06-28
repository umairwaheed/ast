# 🧪 Python AST Function Renamer

This project demonstrates how to use Python's built-in `ast` module to parse and modify Python code. Specifically, it detects all function definitions in a source file and renames them by prefixing with `renamed_`.

## 📦 Features

- Parses a Python file into an Abstract Syntax Tree (AST)
- Identifies all function definitions
- Renames each function to `renamed_<original_name>`
- Writes the modified code to a new file

## 🚀 Quick Start

### 1. Clone the repo or copy the files

```bash
git clone git@github.com:umairwaheed/ast-renamer.git
cd ast-function-renamer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create an input file

Create a file named `example.py`:

```python
def greet(name):
    print(f"Hello, {name}")

def add(x, y):
    return x + y
```

### 4. Run the AST transformer

```bash
python main.py
```

### 5. Output

A new file `example_modified.py` will be created with renamed functions:

```python
def renamed_greet(name):
    print(f"Hello, {name}")

def renamed_add(x, y):
    return x + y
```

## 🧠 How It Works

The script uses Python's `ast` module to parse and transform code. `astor` is used to convert the modified AST back into valid Python source code.

## 🧰 Tech Stack

- Python 3.x
- `ast` (standard library)
- `astor` (for AST to source code conversion)

## 📝 License

MIT License