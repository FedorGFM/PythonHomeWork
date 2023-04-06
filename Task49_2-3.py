input_str_list = {}
input_len_str_list = int(input("Введите количество пар строк: "))
for i in range(input_len_str_list):
    input_str_list[i] = []
    input_str_list[i].append(list(map(lambda x: int(x), input("Введите числа разделённые пробелами: ").split())))
    input_str_list[i].append(list(map(lambda x: int(x), input("Введите числа разделённые пробелами: ").split())))

result = []
for couple in input_str_list:
    for i in range(2):
        result.append(list(set(list(filter(lambda x: x % 10 == 1 or x % 10 == 3, input_str_list[couple][i])))))

print(result)




n = int(input())
some_list = [[i for i in input().split() if i[-1] in ('1', '3')] for i in range(2 * n)]
print(some_list)
for ind in range(0, len(some_list) - 1, 2):
    res = list(set(some_list[ind]).intersection(set(some_list[ind + 1])))
    res = list(map(int, res))
    print(*sorted(res, reverse=True), sep=' & ') 


n = int(input())
# some_list = [[i for i in input().split() if i[-1] in ('1', '3')] for _ in range(2 * n)]

some_list = []
for _ in range(2 * n):
    temp_list = []
    for i in input().split():
        if i[-1] in ('1', '3'):
            temp_list.append(i)
    some_list.append(temp_list)

print(some_list)
for ind in range(0, len(some_list) - 1, 2):
    res = list(set(some_list[ind]).intersection(set(some_list[ind + 1])))
    res = list(map(int, res))
    print(*sorted(res, reverse=True), sep=' & ')