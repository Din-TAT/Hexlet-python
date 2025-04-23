#Реализуйте функцию letter_multiply(). Она должна принимать три параметра:
#
#Слово, тип данных строка
#Букву, тоже строка, но состоящая из одного символа
#Число, которое обозначает, сколько раз нужно повторить букву в слове
#text = 'python'
#print(letter_multiply(text, 'p', 2)) # => ppython
#print(letter_multiply(text, 'y', 3)) # => pyyython
#print(letter_multiply(text, 'n', 4)) # => pythonnnn
#Функция должна возвращать строку — слово с повторенными символами
#
#Укажите аннотации типов при объявлении функции.
#
#Подсказка
#Для замены символов в строке воспользуйтесь методом replace()
#Не забудьте, что аннотацию типов также нужно указать и у возвращаемого значения
from idlelib.replace import replace


def letter_multiply(text: str,word : str,count : int):
    text = str(text)
    word = str(word[0:])
    count = word * count
    return print(text.replace(word,count)) #-> str
letter_multiply('qwertys','q',2)





