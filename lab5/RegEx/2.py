import re
def match_text(text):
        p = 'ab{2,3}'
        if re.search(p,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(match_text("ab"))
print(match_text("abb"))
print(match_text("aabbbbbc"))