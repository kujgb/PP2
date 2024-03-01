import re
def insert_spaces(str1):
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', str1)
    return result
str1 = input(str())
modified_string = insert_spaces(str1)
print(f"Modified string: {modified_string}")