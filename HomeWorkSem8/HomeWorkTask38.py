# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

import functions

while True:
    print('Опции: \n1. Вывод \n2. Добавление \n3. Поиск \n4. Изменить. \n5 Удалить')
    mode = input("Введите опцию: ")
    if mode == "1":
        functions.show_data()
    elif mode == "2":
        functions.add_data()
    elif mode == "3":
        functions.find_data()
    elif mode == "4":
        functions.change_data()
    elif mode == "5":
        functions.delete_data()
    else:
        break
