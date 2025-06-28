# 🧪 Python AST Function Renamer & Insecure Code Checker

This project demonstrates how to use Python's built-in `ast` module to parse and modify Python code. It contains two tools:

1. **Function Renamer** — detects all function definitions and renames them by prefixing with `renamed_`.
2. **Insecure Code Checker** — identifies unsafe Python functions and modules like `eval`, `exec`, `os.system`, etc.

## 📦 Features

- Parses Python files into Abstract Syntax Trees (AST)
- Identifies and renames all function definitions
- Detects insecure statements in code:
  - Dangerous functions (`eval`, `exec`, etc.)
  - Insecure imports (`pickle`, `os.system`, etc.)
- Includes demo test cases (without `unittest`)

## 🚀 Quick Start

### 1. Clone the repo or copy the files

```bash
git clone git@github.com:umairwaheed/ast.git
cd ast
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

### 4. Run the function renamer

```bash
python renamer.py
```

This will create `example_modified.py` with all function names prefixed by `renamed_`.

### 5. Run the insecure code checker demo

Run the script below (or `test_insecure_checker.py` if using a separate test file):

```bash
python insecure_checker.py
```

This will print out which lines in the test code contain insecure patterns.

## 🧠 How It Works

- **AST Parsing**: Code is parsed using Python's `ast` module.
- **Transformation**: `ast.NodeTransformer` is used to modify functions.
- **Security Check**: `ast.NodeVisitor` traverses the tree and flags insecure patterns.
- **Pretty Printing**: `astor` is used to convert AST back into valid Python code.

## 📁 Files

- `renamer.py`: Renames functions in Python source
- `insecure_checker.py`: Detects insecure functions and modules
- `test_insecure_checker.py`: Test script to run and print results
- `requirements.txt`: Lists required Python packages
- `.gitignore`: Common ignore patterns
- `pyproject.toml`: Config for code formatting (Black)

## 🧰 Tech Stack

- Python 3.x
- `ast` (standard library)
- `astor` (for AST to source code conversion)
- `black` (optional code formatter)

## 📝 License

MIT License