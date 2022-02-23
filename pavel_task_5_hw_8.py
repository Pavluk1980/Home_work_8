'''Task 5. 30 points
познакомиться с модулем datetime и написать программу с помощью
lambda для возвращение текущего года, месяца , дня
например результат должен быть таким
import datetime
now = datetime.datetime.now()
.....ваш код))
print(year(now))
print(month(now))
print(day(now))
скинуть мне ссылку на документациюю по datetime.'''

import datetime # импорт модуля

now = datetime.datetime.now() # присваиваем переменной значение объекта текущего времени
year = lambda x: x.year # задаем имя лямбда функции для определения текущего года
month = lambda x: x.month # задаем имя лямбда функции для определения текущего месяца
day = lambda x: x.day # задаем имя лямбда функции для определения текущего дня

print(year(now))

print(month(now))

print(day(now))

# Ссылка на документацию по datetime.datetime -
# https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime