import re
def match_text(text):
        p = 'a.*?b$'
        if re.search(p,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(match_text("aacccbb"))
print(match_text("aabAbbbc"))