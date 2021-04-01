from math import fabs
print('-----------Программа №9(9)-----------')
while 1:
    print('Введите промежуток времени - ЧЧ:ММ')
    h1, m1 = input().split(':')
    h2, m2 = input().split(':')

    h1 = int(h1)
    m1 = int(m1)
    h2 = int(h2)
    m2 = int(m2)

    if h1 <= 23 and h1 >= 0 and m1 <= 59 and m1 > 0 and h2 <= 23 and h2 >= 0 and m2 <= 59 and m2 > 0:
        H = fabs(h1 - h2)
        M = fabs(m1 - m2)

        if H == 0 and M <= 15 or H == 1 and M >= 45 or H == 23 and M >= 45:
            print("Встреча состоится!")
            break
        else:
            print("Встреча не состоится!")
            break
    else:
        print("Некорректный ввод, попробуйте еще раз!")