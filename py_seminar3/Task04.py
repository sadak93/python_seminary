# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером)

from random import randint

print ( lst:= [randint (0, 10) for _ in range (0,10)] )

count = 0
for i in range (1,len(lst)):
    if lst[i] > lst[i-1]:
        count += 1
print(count)