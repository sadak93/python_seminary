# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается,
# что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод:              Вывод:
# 1 2 3 2 3          2

from random import randint

n_of_list_1 = int(input('Введите кол-во чисел в списке: '))
list_1 = [randint(0,5) for _ in range(n_of_list_1)]
print(f'Набор чисел: {list_1}')

# dic = {}
# count = 0
# for i in list_1:
#     value = dic.get(i,0) + 1
#     dic[i] = value
# print(dic)
# count = 0
# for value in dic.values():
#     count += value // 2
# print(count)

print(sum([list_1.count(i)//2 for i in set(list_1)]))

count = 0
for item in set(list_1):
    count += list_1.count(item)//2
print(count)