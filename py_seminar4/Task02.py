# Пользователь вводит текст(строка). Словом считается последовательность 
# непробельных символов идущих подряд, слова разделены одним или большим 
# числом пробелов или символами конца строки.Определите, сколько различных 
# слов содержится в этом тексте.

# str = input('Введите текст: ')
str = """She sells sea shells on the sea shore The shells that she sells 
are sea shells I'm sure. So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells"""
str = str.lower()
str = str.replace('.', ' ')

words = set(str.split())
print(words)

print('Кол-во уникальных слов: ', len(words))