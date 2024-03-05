import os
x = os.getcwd()
path = "../"
list_dir = os.listdir(path)

print("All files and directories in {path} is: ")
list_dir.sort()
print(list_dir)