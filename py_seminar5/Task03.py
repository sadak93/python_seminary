# 1. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)*

# number = int(input('Введите число: '))

# count = 0
# for i in range(1, number+1):
#     if number % i == 0:
#         count += 1
# if count > 2:
#     print('Число НЕ является простым')
# else:
#     print('Число является простым')

# def simple_number(number):
#     count = 0
#     for i in range(1, number + 1):
#         if number % i == 0:
#             count += 1
#     if count > 2:
#         print('Число НЕ является простым')
#     else:
#         print('Число является простым')
# simple_number(number)

def simple_number(number: int) -> bool:
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for dev in range(3, number//2 + 1, 2):
        if number % dev == 0:
            return False
    return True

print(simple_number(1250078961232654654321233221))
print(simple_number(25))
print(simple_number(31))
print(simple_number(7))
print(simple_number(99))
# number = int(input("Введите число: "))
#
# def isPrime(number):
#     for num in range(2, number // 2 + 1):
#         if number % num == 0:
#             return "Число сложное!"
#     return "Число простое!"
#
# print(isPrime(number))