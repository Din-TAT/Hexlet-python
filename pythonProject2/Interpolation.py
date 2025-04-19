#Выведите на экран две строки: Do you want to eat, <name>? и Yes, I'm hungry, mom.
#
#Вместо <name> должна использоваться переменная stark. При формировании итоговой строки используйте интерполяцию. Вывод должен получиться таким:

#Do you want to eat, Arya?
#Yes, I'm hungry, mom.

stark = 'Arya'
print('Do you want to eat, 'f'{stark}?\n',"Yes, I'm hungry, mom.")

