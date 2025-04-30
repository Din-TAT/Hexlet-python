#Реализуйте функцию filter_string(). Она принимает на вход строку и символ и возвращает новую строку, в которой удален переданный символ во всех его позициях. Если строка не содержит указанный символ, то она возвращается без изменений.
#
#Итоговая строка также не должна содержать начальные и концевые пробелы:
#
#text = 'I look back if you are lost'
#filter_string(text, 'i')  # 'look back f you are lost'
#filter_string(text, 'O')  # 'I lk back if yu are lst'
#На этот раз реализуйте эту функцию с помощью цикла for. Дополнительное условие: регистр исключаемого символа не имеет значения.
#
#Подсказка
#Для удаления концевых пробелов можно использовать метод strip()

def filter_string(string,symbol):
    result = ''
    for char in string:
        if char != symbol.lower() and char != symbol.upper():
            result = result + char
    return print(result.strip())
filter_string('I look back if you are lost', 'I')

