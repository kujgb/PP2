import re
def match_text(text):
        p = '^[a-z]+_[a-z]+$'
        if re.search(p,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(match_text("aab_cBbbc"))
print(match_text("aab_abbbc"))
print(match_text("Aaab_abbbc"))