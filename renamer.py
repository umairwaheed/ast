import ast
import astor  # Install with: pip install astor


class FunctionRenamer(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        print(f"Found function: {node.name}")
        node.name = f"renamed_{node.name}"
        return node


# Load source code
with open("example.py", "r") as f:
    source = f.read()

# Parse to AST
tree = ast.parse(source)

# Transform AST
renamer = FunctionRenamer()
modified_tree = renamer.visit(tree)
ast.fix_missing_locations(modified_tree)

# Convert AST back to source code
new_source = astor.to_source(modified_tree)

# Save modified code
with open("example_modified.py", "w") as f:
    f.write(new_source)

print("\nModified code written to example_modified.py")
