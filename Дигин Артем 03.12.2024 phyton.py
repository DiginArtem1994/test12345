memory = float(input('Введите размер файла'))
speed = int(input('Введиет скорость загрузки(бит/сек)'))

memorytwo = memory * 1024 * 1024 * 1024 * 8
downloawd_time = memorytwo/speed

choise = input('выберите единицу измерения [с/м/ч]')

if choise == 'c':
    print(f'время скачинивая файл',(downloawd_time),'c')
elif choise=='м':
    print(f'время скачинивая файл', (downloawd_time)//60,'м')
if choise == 'c':
    print(f'время скачинивая файл', (downloawd_time)//3600,'ч')
else:
    print('некоректный ввод')


# тест
points = 0
name = input('Введите имя')
print('Привет',name)
print('Какую функцию выполняет команда input? варианты ответа:(1.запрос на ввод информации/2.вывод информации на экран?/3.создание переменной)')
otvet = int(input('Введите вариант ответа'))
if otvet == 1:
    print('Ответ правильный!вы заработали 10 баллов')
    points += 10
else:
    print('Ответ неправильный!вы заработали 5 баллов')
    points -= 5
print('Какую функцию выполняет команда print? варианты ответа:(1.запрос на ввод информации/2.вывод информации на экран?/3.создание переменной)')
otvet_2 = int(input('Введите вариант ответа'))
if otvet_2 == 2:
    print('Ответ правильный!вы заработали 10 баллов')
    points += 10
else:
    print('Ответ неправильный!вы заработали 5 баллов')
    points -= 5


print('name = 5 это?|1.уравнение /2.задаем переменную/ 3.будет ошибка')
otvet_3 = int(input('Введите вариант ответа'))
if otvet_3 == 2:
    print('Ответ правильный!вы заработали 10 баллов')
    points += 10
else:
    print('Ответ неправильный!вы заработали 5 баллов')
    points -= 5
if points>19:
    print('Отлично,тест пройдет',points,'баллов')
else:
    print('тест пройдет', points, 'баллов')


# перевод времени

hour = int(input('Введите часы:'))
minute = int(input('Введите минуты:'))
difference = int(input('Введите разницу:'))
new_hour = hour + difference
if new_hour>24:
    new_hour-= 24
elif new_hour<0:
    new_hour+= 24
print(f'{new_hour}:{minute}')






