#Реализуйте функцию normalize_url(), которая выполняет так называемую нормализацию данных. Она принимает адрес сайта и возвращает его с https:// в начале.
#
#Функция принимает адреса в виде:
#
#АДРЕС
#http://АДРЕС
#https://АДРЕС (нормализованный)
#Функция всегда возвращает адрес в виде https://АДРЕС.
#
#normalize_url('https://ya.ru')  # https://ya.ru
#normalize_url('google.com')  # https://google.com
#normalize_url('http://ai.fi')  # https://ai.fi
#Подсказка
#Можно сравнить первые семь символов адреса со строкой http://. Для этого вам нужно получить кусок строки или отбросить ненужный. Мы рассматривали способ получения части строки ее начала:
#
## Берем два символа от начала
#print('Python'[:2])  # => Py
#
## Отбрасываем первые два символа
#print('Python'[2:])  # => thon

def normalize_url(address):
    address2 = address[:7]
    if address2 == "https:/":
        print(address2 + address[7:])
    elif address2 == 'http://':
        print('https:/' + address[6:])
    else:
        print('https://' + address)
normalize_url(address='ya.ru')

