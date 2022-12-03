# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

def is_float_number(txt):
    if ',' in txt:
        txt = txt.replace(',', '.')
    try:
        float(txt)
        return True
    except ValueError:
        return False

input_num = input('Введите дробное число: ')

print(is_float_number(input_num))