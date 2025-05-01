#Палиндром — слово или текст, одинаково читающиеся в обоих направлениях. Примеры:
#
#"я",
#"радар",
#"асса",
#"ишак ищет у тещи каши"
#src/solution.py
#Реализуйте функцию is_palindrome(), которая принимает на вход слово, определяет, является ли оно палиндромом, а затем возвращает логическое значение.
#
#from solution import is_palindrome
#is_palindrome('')  # True пустая строка тоже считается палиндромом
#is_palindrome('radar') # True
#is_palindrome('a') # True
#is_palindrome('abs') # False
#is_palindrome('ишак ищет у тещи каши') # True


def is_palindrome(string):
    string_inverted = str(string[::-1])
    if string_inverted == string:
       return True
    else:
       return False
is_palindrome('')