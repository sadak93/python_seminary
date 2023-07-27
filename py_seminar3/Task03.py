# Напишите программу для печати всех уникальных значений в словаре.
# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
#           {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
list_2 = []

for i in list_1:
    for key, value in i.items():
        list_2.append(value)

print (list_2)
print (set(list_2))

