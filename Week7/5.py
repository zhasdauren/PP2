# Delete ONLY Python files from the given Directory
import os   # Operating System

os.chdir('tmp')
files = os.listdir()

for file in files:
    print(file)
    print(type(file))
    if file.endswith('.py'):
        os.remove(file)