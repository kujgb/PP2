import os
x = os.getcwd()
path = "../"
list_dir = os.listdir(path)

print("All files and directories in {path} is: ")

if list_dir:
    print(list_dir)
else:
    print("Not exist such kind of path")