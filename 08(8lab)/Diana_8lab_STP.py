from math import sqrt

print('-----------Программа №8(8)-----------')

while 1:
    print('Введите 2 числа и знак через пробел')
    a, f, b = input().split(' ')
    a = int(a)
    b = int(b)
    if f == '/':
        a = a / b
        print('Ответ: ', a)
        break
    elif f == '*':
        a = a * b
        print('Ответ: ', a)
        break
    elif f == '+':
        a = a + b
        print('Ответ: ', a)
        break
    elif f == '-':
        a = a - b
        print('Ответ: ', a)
        break
    else:
        print('Некорректный ввод')