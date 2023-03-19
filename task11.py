# 11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое
# число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

input_number = int(input("Введите натуральное число: "))
first_fibonachi = 0
second_fibonachi = 1
tnp_fibonachi = first_fibonachi + second_fibonachi
index = 3
while tnp_fibonachi < input_number:
    first_fibonachi = second_fibonachi
    second_fibonachi = tnp_fibonachi
    tnp_fibonachi = first_fibonachi + second_fibonachi
    index += 1
if tnp_fibonachi == input_number:
    print(index + 1)
else:
    print(-1)
