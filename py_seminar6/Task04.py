# Два различных натуральных числа n и m называются дружественными, если сумма делителей
# числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k,
# не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых
# не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод:                  Вывод:
# 300                     220 284


# def sum_devs(num: int):
#     summ_ = 0
#     for i in range(1, num//2 + 1):
#         if num % i == 0:
#             summ_ += i
#         return summ_
# # print(sum_devs(220))
# # print(sum_devs(284))
#
# digit_dict = {i: sum_devs(i) for i in range(1,10000)}
#
# for digit, summ_ in digit_dict.items():
#     if digit == digit_dict.get(summ_) and digit < summ_:
#         print(digit, summ_)

nums = []

def findSum(num):
    sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum += i
    return(sum)

for i in range(1, 10000):
    sum1 = findSum(i)
    sum2 = findSum(sum1)
    if sum2 == i and sum1 != sum2 and sum1 not in nums:
        nums.append(i)
        nums.append(sum1)
        print(i, sum1)




# number = int(input('Number: '))
#
# count = 0
# for i in range(1, 300):
#     summ_1 = 0
#     for k in range(1, i//2 + 1):
#         if i % k == 0:
#             summ_1 += k
#     summ_2 = 0
#     for j in range(1, summ_1//2 + 1):
#         if summ_1 % j == 0:
#             summ_2 += j
#     if summ_2 == i and summ_1 != summ_2:
#         i = summ_1
#     print(f'{summ_1} {summ_2}')


