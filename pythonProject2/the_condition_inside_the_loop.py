#Реализуйте функцию has_char(). Она должна проверять, содержит ли строка указанную букву (вне зависимости от регистра). Функция принимает два параметра:
#
#Строка
#Буква для поиска
#И возвращает результат проверки – булево значение.
#
#print(has_char('Hexlet', 'H'))  # => True
#print(has_char('Hexlet', 'h'))  # => True
#print(has_char('Awesomeness', 'd'))  # => False



def has_char(string,letter_to_search):
    i = 0
    char = letter_to_search.upper()
    while i <= len(string) - 1:
        if char == string[i].upper():
            return print(True)
        i += 1
    return print(False)
has_char('qwerty','Q')

