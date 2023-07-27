# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

from random import randint

numbers = int(input('Введите кол-во чисел: '))

print ( lst:= [randint (0, 10) for _ in range (numbers)] )
k = int (input('Введите сдвиг: '))
# print(lst[-k:]+lst[:-k])

# for i in range(k):
#     lst.insert(0, lst.pop())
# print(lst)

new_list = []
for i in range(len(lst)):
    new_list.append(lst[(i-k) % len(lst)])
print(new_list)

# new_list = []
# for i in range(100):
#     print(lst[i%len(lst)])