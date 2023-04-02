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