def a(list):
    contains = True
    a = 0
    b = 0
    c = 7
    if '0' in list:
        a = int(list.index('0'))
        list.pop(a)
    if '0' in list:
        b = int(list.index('0'))
        list.pop(b)
    if '7' in list:
        c = int(list.index('7'))
        list.pop(c)
    if a<b<c or b<a<c:
        return True
    return False
list = list(input().split())
print(a(list))