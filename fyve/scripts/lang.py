import re

def parse(f):
    parts = re.search(r"five\.([^\s]{0,}) = function\(\) { (return '.{0,}')", f)
    return parts.group(1), parts.group(2)

def generate_py_func(parts):
    return "def {0}(self):\n    {1}".format(parts[0], parts[1])

if __name__ == '__main__':
    with open('langs') as f:
        for line in f:
            print(generate_py_func(parse(line)), "\n")
