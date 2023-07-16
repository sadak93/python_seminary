# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: 
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? 
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, 
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза. 
# Все числа натуральные и не превышают 30000.

from random import randint

num_watermelon = int (input())
weight = 0
min_weight = 30001
max_weight = 1000
i=1
while i <= num_watermelon: 
    weight = randint(1000,30000)
    print(weight, end= ', ')
    if weight < min_weight:
        min_weight = weight
    if weight > max_weight:
        max_weight = weight
    i += 1
    
print()
print(min_weight)
print(max_weight)