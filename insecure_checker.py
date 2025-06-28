import ast


class InsecureCodeChecker(ast.NodeVisitor):
    INSECURE_FUNCTIONS = {"eval", "exec", "compile", "input", "open"}
    INSECURE_MODULES = {
        ("os", "system"),
        ("os", "popen"),
        ("subprocess", "call"),
        ("subprocess", "run"),
        ("subprocess", "Popen"),
        ("pickle", None),
    }

    def __init__(self):
        self.issues = []

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in self.INSECURE_FUNCTIONS:
            self.issues.append(
                f"Insecure function '{node.func.id}' used at line {node.lineno}"
            )
        if isinstance(node.func, ast.Attribute) and isinstance(
            node.func.value, ast.Name
        ):
            mod_func = (node.func.value.id, node.func.attr)
            if mod_func in self.INSECURE_MODULES:
                self.issues.append(
                    f"Insecure call '{mod_func[0]}.{mod_func[1]}' used at line {node.lineno}"
                )
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            if (alias.name, None) in self.INSECURE_MODULES:
                self.issues.append(
                    f"Insecure module '{alias.name}' imported at line {node.lineno}"
                )
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if (node.module, None) in self.INSECURE_MODULES:
            self.issues.append(
                f"Insecure module '{node.module}' imported at line {node.lineno}"
            )
        self.generic_visit(node)


def check_code_for_insecurity(source_code: str):
    tree = ast.parse(source_code)
    checker = InsecureCodeChecker()
    checker.visit(tree)
    return checker.issues


def test_insecure_code(code):
    issues = check_code_for_insecurity(code)
    for issue in issues:
        print("⚠️", issue)
    if not issues:
        print("✅ No insecure code detected.")


test_insecure_code(
    """
eval("2 + 2")
exec("print('hello')")
compile("x = 1", "<string>", "exec")
input("Enter your name: ")
open("file.txt", "r")
"""
)
