# Задача №15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

quantity = int(input("Количество арбузов: "))
max_weight = 0
min_weight = 0
for i in range(quantity):
    current_waight = int(input("Вес арбуза: "))
    while current_waight <= 0 or current_waight > 30000:
        print("Такой арбуз не унести.")
        current_waight = int(input("Вес арбуза: "))
    if i == 0:
        min_weight = current_waight
        max_weight = current_waight
    if i != 0:
        if current_waight > max_weight and current_waight < 30000:
            max_weight = current_waight
        if current_waight < min_weight and current_waight > 0:
            min_weight = current_waight
print(f"Арбуз для себя {max_weight}")
print(f"Арбуз для тещи {min_weight}")


arbusi = int(input("Количество "))
max = 0
min = 0

for i in range(arbusi):
    massa_arbus = int(input("Масса "))
    while 0 <= massa_arbus > 30000:
        print("выбери другой")
        massa_arbus = int(input("Масса "))
    if i == 0:
        min = massa_arbus
    if massa_arbus > max:
        max = massa_arbus
    if massa_arbus < min:
        min = massa_arbus
print(f"max = {max}")
print(f"min = {min}")
