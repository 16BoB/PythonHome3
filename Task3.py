# 3.12 Вводим с клаиватуры строку. Необходимо вывести строку, где развернём подстроку между первой и последней буквой "о" из исходной строки. Если она только одна или её нет - то сообщить, что буква "о" - одна или не встречается.

def reverb(txt):
    txt = txt.lower()
    first_index = txt.find('о')
    second_index = txt.rfind('о')

    if first_index == -1:
        print('Буквы "о" нет в строке')
        return exit
    elif first_index == second_index:
        print('буква "о" одна в строке')
        return exit

    temp_str = txt[first_index + 1:second_index]
    txt = txt.replace(temp_str,temp_str[::-1])

    return txt

input_str = input('Введите строку: ')

print(reverb(input_str))