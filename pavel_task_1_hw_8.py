'''Task1. 5 points

Написать функцию которая будет принимать 3 аргумента (int) и находить максимум из них '''

l_1 = input('введите переменные через пробел: ').split() # принимаем аргументы, преобразуем в список


def find_max(x):
    return max([int(a) for a in x]) # ищем максимальный аргумент в исходном списке


print(find_max(l_1))
