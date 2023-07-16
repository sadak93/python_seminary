# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать 
# маршрут длиной m километров? При решении этой задачи нельзя пользоваться 
# условной инструкцией if и циклами.

# **Input:**

# n = 700

# m = 750

# **Output:**

# 2

# n = int(input("n = "))
# m = int(input("m = "))

# print((m + n - 1) // n)

import math
# print('Ввдеите сколько проезжает машина в день')
# n = int(input())
# print('Введите сколько нужно проехать')
# m = int(input())
# print(math.ceil (m/n))

per_day = 700
total = 750

# days = (per_day + total - 1)//per_day
# print (days)

# number = 1.7

# print(round(number))
# print(math.floor(number))
# print(math.ceil(number))

days = total//per_day + (total%per_day != 0)
print(days)
