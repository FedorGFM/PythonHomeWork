# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

n = int(input('Input n ')) # общее кол-во эл-в
x = int(input('Input a[0] ')) # первый элемент 
d = int(input('Input d ')) # шаг
print(*range(x, x + d * n, d))


# Эталонное решение

# a1 = int(input("Введите первый элемент a1: "))    # первый эл-т
# d = int(input("Введите шаг d: "))                 # шаг
# n = int(input("Введите общее кол-во эл-в n: "))   # общее кол-во эл-в
# for i in range(n):
#     print(a1 + i * d)




# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

arr = [randint(1, 10) for _ in range(20)]
print(arr)

min = int(input("min = "))
max = int(input("max = "))
index = []
for i in range(len(arr)):
	if min <= arr[i] <= max:
		index.append(i)
		
result = []
for i in index[::-1]:
	result.append(arr.pop(i))
	
print(f"Индексы -> {index}")
print(f"Числа входящие в отрезок от min до max -> {result}")   # Вывод начала с конца списка



# Эталонное решение

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# print(list_1)
# min_number = int(input("min = "))
# max_number = int(input("max = "))
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(f"Индекс: {i}")