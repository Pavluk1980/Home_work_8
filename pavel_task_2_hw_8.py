'''Task2. 10 points

Написать функцию которая будет принимать 2 аргумента (int) и находить максимум из них.

Затем используя функцию1 (вызвать ее) написать функцию2 которая будет принимать 3 аргумента
и находить максимум с помощью функции1. в итоге будет .

псевдокод

функция_нахождения_макс_из_2х(арг1, арг2):

return максимальное значение из 2х аргументов

функция_нахождения_макс_из_3х(арг1, арг2, арг3):

использую тут функция_нахождения_макс_из_2х()

return максимальное значение из 3х аргументов.'''

# a, b, c = 1000, 220, 30
a, b, c = input('Введите 3 аргумента через пробел: ').split()
a, b, c = int(a), int(b), int(c)


def find_max_2arg(x, y):
    if x > y:
        return x
    else:
        return y


def find_max_3arg(x, y, z):
    middle = find_max_2arg(x, y)
    if z > middle:
        return z
    else:
        return middle


print(find_max_3arg(a, b, c))