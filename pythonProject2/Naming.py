#Вы столкнулись с таким кодом, который выводит на экран общее количество комнат во владении нынешнего короля:

#king = 'King Balon the 6th'
 #Функция str() превращает число в строку
 #О таких превращениях будет отдельный урок
#print(king + ' has ' + str(6 * 17) + ' rooms.')
#Как видите, это магические числа: непонятно, что такое 6 и что такое 17. Можно догадаться, если знать историю королевской семьи: каждый новый король получает в наследство все замки от предков и строит новый замок — точную копию родительского замка из 17 комнат.

#Эта странная династия просто плодит одинаковые замки…

#Избавьтесь от магических чисел, создав новые переменные, а затем выведите текст на экран:

#King Balon the 6th has 102 rooms.
#Названия переменных должны передавать смысл чисел, но должны при этом оставаться короткими и емкими.
#Помните: код будет работать с любыми названиями, а наша система всегда проверяет только результат на экране, поэтому выполнение этого задания — под вашу ответственность.


count_ancestors = 6
count_castle = 17
king = 'King Balon the 6th has'
count_rooms = count_castle * count_ancestors
print(king,count_rooms,'rooms')