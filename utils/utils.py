import os

def read_input(filename):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(project_root, "inputs", filename)
    with open(input_path, 'r') as f:
        return f.read().strip()

def read_input_lines(filename):
    return [line.strip() for line in read_input(filename).splitlines()]
