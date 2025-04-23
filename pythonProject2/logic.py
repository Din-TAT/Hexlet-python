#Реализуйте функцию has_upper_case(), которая определяет, содержит ли строка заглавные буквы. Функция должна вернуть булево значение:
#
#has_upper_case('')  # False
#has_upper_case('python')  # False
#has_upper_case('pyThon')  # True
#Подсказка
#Воспользуйтесь методом из стандартной библиотеки, который приводит строку к нижнему регистру. Обратите внимание, чем отличается такая строка от исходной.

def has_upper_case(argument):
    argument_two = argument
    argument = str.lower(argument)
    return print(bool(argument_two != argument))
has_upper_case("asD")
