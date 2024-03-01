#write a python program that mathes a string that has an 'a' followed by zero or more 'b's
import re
def match(text):
        p = "^a(b*)$"
        if re.search(p,  text):
            return 'Found a match!'
        else:
            return('Not matched!')
print(match("ac"))
print(match("abc"))
print(match("a"))
print(match("ab"))