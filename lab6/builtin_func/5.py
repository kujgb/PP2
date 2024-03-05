def tuple_check(a):
    return all(x == True for x in a)

input_tuple = tuple(input()).split(',')

check = tuple_check(input_tuple)
print(check)