#Реализуйте функцию join_numbers_from_range(), которая объединяет все числа из диапазона в строку и возвращает получившуюся строку:
#
#join_numbers_from_range(1, 1)  # 1
#join_numbers_from_range(2, 3)  # 23
#join_numbers_from_range(5, 10)  # 5678910

def join_numbers_from_range(onenumber,twonumber):
    i = onenumber
    sum = str()
    while i <= twonumber:
        sum += str(i)
        i = i + 1
    return sum
join_numbers_from_range(1,2)


