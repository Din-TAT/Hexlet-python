#Реализуйте функцию sort_pair, которая принимает пару (кортеж из двух значений) и возвращает пару, значения которой расположены строго в порядке возрастания.
#
#Пример:
#
## обратите внимание на скобки у аргумента функции
#sort_pair((5, 1)) # (1, 5)
#sort_pair((2, 2)) # (2, 2)
#sort_pair((7, 8)) # (7, 8)



def soft_pair(tuple):
    number_one, number_two = tuple
    if number_one > number_two:
        return number_two,number_one
    else:
        return number_one,number_two
soft_pair(())