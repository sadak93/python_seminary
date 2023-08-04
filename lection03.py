# 1
# def sum_numbers(n, y = 'hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
#
# a = sum_numbers(5, 'qwerty')
# print(a)

# 2
# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(sum_str('q','e','l'))
# print(sum_str('q','e','l','r','f'))
# print(sum_str(1,8,9))

# 3 Импорт модуля
# import modul1
#
# print(modul1.max1(5,9))

#4 другой способ импортирования модуля
# from modul1 import *  #импорт всех функций
# print(max1(10,9))

#5 другой способ импортирования модуля
# import modul1 as m1
# print(m1.max1(10,9))

# 6 Рекурсия
# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# list_1 = []
# for i in range (1,10):
#     list_1.append(fib(i))
# print(list_1)

# 7 Быстрая сортировка - Разделяй и властвуй
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i >= pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
#
# print(quick_sort([10,5,2]))

# 8 Сортировка слиянием
def merge_sort(nums):
    if len (nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left [i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1,5,6,36,8,5,19,12,8,4,66,4]
merge_sort(list1)
print(list1)