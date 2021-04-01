from math import sqrt
from math import fabs

print('-----------Программа №6(6)-----------')

a = int(input('Введите первое вещественное число: '))
b = int(input('Введите второе вещественное число: '))
c = int(input('Введите третье вещественное число: '))

D = ((b ** 2) - (4 * a * c))

if (D >= 0) & (((a != 0) & (b != 0)) | ((a != 0) & (c != 0)) | ((b != 0) & (c != 0))):
    if a != 0:
        x1 = (-b - (sqrt(D))) / (2 * a)
        x2 = (-b + (sqrt(D))) / (2 * a)
        if x1 == x2:
            print("x=", x1)
        else:
            print("x1 = ", x1)
            print("x2 = ", x2)
    else:
        x = (-c / b)
        print("x = ", x)
if (D < 0) | ((a == 0) & (b == 0) & (c != 0)):
    print("Нет решения")
if ((b == 0) & (c == 0) & (a != 0)) | ((a == 0) & (c == 0) & (b != 0)):
    if a != 0:
        print("x = ", 0 / a)
    if b != 0:
        print("x = ", 0 / b)
if (a == 0) & (b == 0) & (c == 0):
    print("Все корни верны")