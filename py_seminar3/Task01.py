# Дан список чисел. Определите, сколько в нем встречается различных чисел.

from random import randint

# list_numbers = []

# list_1 = [randint(-5,5) for i in range (1,10)]
# print(list_1)

# list_2 = []
# count = 0
# for item in list_1: 
#     if item not in list_2: 
#         list_2.append(item)
#         count += 1
# print(count)

print(lst := [randint(-3,3) for _ in range (1,10)])

# lst_2 = []

# for i in lst:
#     if i not in lst_2:
#         lst_2.append(i)

# print (len(lst_2))
print(set(lst))
print(len(set(lst)))