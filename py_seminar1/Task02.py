# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты 
# для них новыми партами. За каждой партой может сидеть два учащихся. Известно количество 
# учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
# **Input:**
# 20
# 21
# 22
# **Output:**
# 32

import math

# class1 = math.ceil(20/2)
# class2 = math.ceil(20/2)
# class3 = math.ceil(21/2)

# tables = (class1+class2+class3)
# print(tables)

class1 = 20
class2 = 20
class3 = 22

tables = (class1+1)//2+(class2+1)//2+(class3+1)//2
print(tables)