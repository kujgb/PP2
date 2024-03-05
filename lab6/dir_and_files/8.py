import os
if os.path.exists("a.txt"): 
  os.remove("a.txt")
else:
  print("Does not exist")