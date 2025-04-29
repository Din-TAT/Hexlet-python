#Напишите функцию print_numbers(). Функция должна принимать число и выводить числа в обратном порядке от этого числа до нуля (нуль не выводится).
#
#По окончании работы функция должна вывести на экран строку finished!.
#
#print_numbers(4)
# => 4
# => 3
# => 2
# => 1
# => finished!


def print_numbers(number):
    while number != 0:
        print(number)
        number = number - 1
    print('finished!')
print_numbers(4)
