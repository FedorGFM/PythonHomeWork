# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

import random
input_n = int(input("n = "))
list_i = ([random.randint(1, 10) for _ in range(input_n)])
print(list_i)

max_sum = list_i[0] + list_i[-1] + list_i[-2]
sum = 0
for i in range(input_n - 1):
    sum = list_i[i - 1] + list_i[i] + list_i[i + 1]
    if sum > max_sum:
        max_sum = sum
print(f"сумма{max_sum}")



