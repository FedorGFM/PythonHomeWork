# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# list_1 = []
# list_len = int(input('Количество элементов: '))
# for i in range(list_len):
#     list_1.append(int(input(f'Введите {i + 1} число: ')))
# print(list_1)

# set_1 = set(list_1)
# print(f"Разных чисел: {len(set_1)}")


input_list = []
list_len = int(input("Введите количество элементов в списке: "))
for _ in range(list_len):
    input_list.append(int(input(f"Введите число: ")))
print(input_list)

input_set = set(input_list)
print(f"Различных чисел {len(input_set)}")

