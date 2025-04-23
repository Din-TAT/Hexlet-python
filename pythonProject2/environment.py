#Это задание не связано напрямую с уроком, это просто еще одно полезное упражнение по работе с функциями.
#
#Напишите функцию get_age_difference(), которая принимает два года рождения и возвращает строку с разницей в возрасте в виде The age difference is 11.
#
#Пример работы функции:
#
#actual = get_age_difference(2001, 2018)
#print(actual)  # => The age difference is 17
#Подсказки
#Вам пригодится функция abs()

def get_age_difference(one_date,two_date):
    difference = one_date - two_date
    return print('The age difference is', abs(difference))
get_age_difference(2001,2001,)