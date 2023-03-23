# Задача 16: Требуется вычислить, сколько раз встречается некотороечисло X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X. Попробуйте использовать метод count(),
# а также решите задачу с помощью своего алгоритма (без count).
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.

input_list = []
list_len = int(input("Колличество чисел: "))
for i in range(list_len):
    input_list.append(int(input(f"Введите {i + 1} элемент: ")))
print(input_list)

input_len_x = int(input("Введите число Х: "))

# start = time.perf_counter()
count = 0

for i in range(list_len):
    if input_list[i] == input_len_x:
        count += 1
print(f"Число X \"{input_len_x}\" встречается {count} раза.")
# end = time.perf_counter()
# print(end - start)

# start = time.perf_counter()
# print(input_list.count(input_len_x))                   Функция time не работает выдает ошибку
# end = time.perf_counter()
# print(end - start)      