import re
def match_text(text):
        p = '[A-Z]+[a-z]+$'
        if re.search(p, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(match_text("AaBbGg"))
print(match_text("Apple"))
print(match_text("aD"))