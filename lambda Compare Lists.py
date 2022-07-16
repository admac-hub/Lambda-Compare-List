from textwrap import indent
print('*'*60)
print('\n')
l_func = lambda x, y: list((set(x)- set(y))) + list((set(y)- set(x))) 

list_a = [2, 4, 6, 8, 10, 12,'as']
list_b = [2, 4, 6, 8, 9, 13,'e4']

non_match = l_func(list_a, list_b)

print("Non-match elements: ", non_match)



print('\n')
print('*'*60)
print('\n')

# in whitch list does that value exist 
# index = 2
item = 12

if  item in list_a:
    print('item exist in list: A ''\n')
    print('Item is stored in this location:', list_a.index(item))
elif item in list_b:
    print('item exist in list: B''\n')
    print('Item as+ is stored in memory in this location:', list_a.index(item))
else:
    print('item does not exist ')

print('\n')


# print('\n')
# print('*'*60)
# print('\n')

# # where is stored in memory

# # index = list_a.index(y)
# # print('Item as+ is stored in memory in this location:', index)