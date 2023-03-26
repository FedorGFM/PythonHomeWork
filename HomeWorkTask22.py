# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random
# input_list_n = sorted(set([random.randint(1, 10) for _ in range(int(input()))]))
# input_list_m = sorted(set([random.randint(1, 10) for _ in range(int(input()))]))
input_list_n = (set([random.randint(1, 10) for _ in range(int(input()))]))
input_list_m = (set([random.randint(1, 10) for _ in range(int(input()))]))
# input_n = int(input("Колличество элементов в первом множестве: "))
# input_m = int(input("Колличество элементов во втором множестве: "))
# for i in range(input_n):
#     input_list_n.append(int(input(f"Введите {i + 1} элемент в первом множестве: ")))
# for i in range(input_m):
#     input_list_m.append(int(input(f"Введите {i + 1} элемент во втором множестве: ")))
print(f"Первое множество -> {input_list_n}")
print(f"Второе множество -> {input_list_m}")

# input_list_x = []
# for i in range(len(input_list_n)):
#     for j in range(len(input_list_m)):
#         if input_list_n[i] == input_list_m[j]:
#             input_list_x.append(input_list_n[i])
#             break
# print(input_list_x)

input_list_l = sorted(input_list_n.intersection(input_list_m))  # Способ интерсепшен(сравнивает множества лист н и лист м, 
print(input_list_l)                                             #если совпадает вычитает их остальные не трогает)

    

