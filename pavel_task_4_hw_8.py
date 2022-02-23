'''Task 4. 10 points Lambda function. с помощью Анонимной функции остортировать список кортежей по цифре.

Пример(Example)

Input: [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]

Otput: [('cola', 1), ('milk', 2), ('bread', 5), ('eggs', 30)]'''


l_1 = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
l_1.sort(key= lambda x: x[1]) # сортировка элементов списка по ключу, заданному функцией
print(l_1)
