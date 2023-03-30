# Данастрока(возможно,пустая),состоящаяизбуквA-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
# BBBBBBBBBBBBBBBBBBBBBBBB
# НужнонаписатьфункциюRLE,котораянавыходедастстрокувида:
# A4B3C2XYZD4E3F3A6B28
# Исгенерируетошибку,еслинавходпришланевалиднаястрока.Пояснения:Есливстречается1,оностаетсябезизменений;
# Еслисимволповторяетсяболее1раза,кнемудобавляетсяколичествоповторений.

str_n = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"

input_str = [str_n[0]]
sum = 1
for i in range(1, len(str_n)):
    if str_n[i] == str_n[i - 1]:
        sum += 1
        if i == len(str_n) - 1:
            input_str.append(str(sum))
    else:
        if sum > 1:
            input_str.append(str(sum))
        input_str.append(str_n[i])
        sum = 1

result_str = "".join(input_str)
print(result_str)