def a(list1,list2):
    for x in list1:
        if x in list1 and x not in list2:
            list2.append(x)
    return list2
list1 = list(input().split())
list2 = list([])
print(a(list1,list2))