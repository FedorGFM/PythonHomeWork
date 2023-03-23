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


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.

input_list = []
list_len = int(input("Колличество элементов в массиве: "))
for i in range(list_len):
    input_list.append(int(input(f"Введите {i + 1} элемент: ")))
print(input_list)

input_len_x = int(input("Введите число Х: "))

desired_num = input_len_x
for i in range(len(input_list)):
    if input_list[i] < input_len_x:
        desired_num = -desired_num
    else:
        desired_num = desired_num
    if input_list[i] >= input_len_x and input_list[i] - input_len_x <= desired_num - input_len_x:
        desired_num = input_list[i]
    elif input_list[i] <= input_len_x and desired_num - input_len_x <= input_list[i] - input_len_x:
        desired_num = input_list[i]
print(f"Ближайшее число к заданному: {desired_num}")



# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.

# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.


input_list = (str(input("Введите слово на английском: "))).upper()
print(list(input_list))

scrabble_dict = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,  
                 'D': 2, 'G': 2, 
                 'B': 3, 'C': 3, 'M': 3, 'P': 3,
                 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 
                 'K': 5, 
                 'J': 8, 'X': 8, 
                 'Q': 10, 'Z': 10}
sum = 0
print(input_list)
for i in range(len(input_list)):
    sum = sum + scrabble_dict[input_list[i]]
print(sum)