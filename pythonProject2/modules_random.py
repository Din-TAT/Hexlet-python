#Реализуйте функцию choice_from_range(), которая принимает строку-набор и возвращает случайный символ по индексу из ограниченного диапазона.
#
#Аргументы функции:
#
#строка-набор
#начальный индекс диапазона
#конечный индекс диапазона
#text = "abcdef"
#choice_from_range(text, 3, 5)  # d
#choice_from_range(text, 3, 5)  # f
#choice_from_range(text, 3, 5)  # e
#
## диапазон включает начальный и конечный индексы
#choice_from_range(text, 2, 2)  # c

from random import choice

def choice_from_range(string,start_index,finish_index):
    if start_index != finish_index:
        index_string = choice(string[start_index:finish_index])
        print(index_string)
    else:
        finish_index += 1
        index_string2 = choice(string[start_index:finish_index])
        print(index_string2)
choice_from_range('qwerty',2,3)
