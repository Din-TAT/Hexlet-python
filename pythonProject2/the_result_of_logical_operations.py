#Реализуйте функцию string_or_not(), которая проверяет является ли переданный параметр строкой. Если да, то возвращается строка yes, иначе no.
#
#string_or_not('Hexlet') # yes
#string_or_not(10)       # no
#string_or_not('')       # yes
#string_or_not(False)    # no
#Подсказки
#Проверить, что значение является строкой, можно с помощью функции isinstance():
#
#isinstance(3, str) # False
#isinstance('Hexlet', str) # True

def string_or_not(class1):
    type1 =  isinstance(class1,str)
    return (print(type1 == True and 'yes' or 'no'))
string_or_not('21')



