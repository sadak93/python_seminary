# 9. По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

# n = int (input('n= '))
# i = 1
# f = 1
# while i<=n:
#     f = f * i
#     i += 1
# print (f)

number = int (input('Введите число: '))

fact = 1

while number > 1:
    fact *= number
    number -= 1

print(fact)