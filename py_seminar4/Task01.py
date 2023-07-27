# Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. Количество повторов добавляется 
# к символам с помощью постфикса формата _n.

str = 'a a a b c a a d c d d'
str = str.split()
print(str)

dict = {}

for i in str:
    if i not in dict:
        print(i, end=' ')
    else:
        print(f'{i}_{dict[i]}',end=' ')
    dict[i]=dict.get(i,0)+1
    
# number = input('Введите строку: ')

# count_dict = {}

# for i in number:
#     count_dict[i] = count_dict.get(i,0)+1
#     print(f'{i}'+(f'_{count_dict[i]-1}' if count_dict[i] > 1 else ''), end=' ')
   