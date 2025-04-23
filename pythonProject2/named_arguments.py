#Реализуйте функцию trim_and_repeat(), которая принимает три параметра:
#
#Строку
#offset — число символов, на которое нужно обрезать строку слева
#repetitions — сколько раз нужно повторить строку перед возвратом получившейся строки
#Число символов для среза по умолчанию равно 0, а количество повторений по умолчанию равно 1.
#
#Функция должна возвращать полученную строку.
#
#text = 'python'
#
#trim_and_repeat(text, offset=3, repetitions=2)  # honhon
#trim_and_repeat(text, repetitions=3)  # pythonpythonpython
#trim_and_repeat(text)  # python
#Подсказки
#Реализовать эту функцию можно различными способами
#С точки зрения проверочной системы не имеет значения, каким из способов будет реализована функция trim_and_repeat() внутри. Главное – чтобы она выполняла поставленную задачу

def trim_and_repeat(text, offset, repetitions):
    text = text
    offset = text[offset:] * repetitions
    repetitions = text * repetitions
    print(text,'\n',offset,'\n', repetitions,sep='')
    return text
trim_and_repeat('python',2,4)