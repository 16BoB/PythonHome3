# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.
def convert_sixteen(number):
    str_num = ''
    while number > 0:
        temp = number%16
        if temp == 10:
            temp = 'A'
            str_num = str_num + temp
        elif temp == 11:
            temp = 'B'
            str_num = str_num + temp
        elif temp == 12:
            temp = 'C'
            str_num = str_num + temp
        elif temp == 13:
            temp = 'D'
            str_num = str_num + temp
        elif temp == 14:
            temp = 'E'
            str_num = str_num + temp
        elif temp == 15:
            temp = 'F'
            str_num = str_num + temp
        else:
            str_num = str_num + str(temp)
        number //= 16

    str_num = str_num[::-1]

    return str_num


num = int(input('Введите число: '))

print(convert_sixteen(num))