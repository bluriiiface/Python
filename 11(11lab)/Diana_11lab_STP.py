print('-----------Программа №11(11)-----------')
a = (int(input('Введите возводимое число: ')))
res = a
n = (int(input('Введите степень числа: ')))
i = 1
if n == 0:
    res = 1
    print(a, '^', n, '=', res)
elif n > 0:
    for i in range(i, n):
        res = res * a
    print(a, '^', n, '=', res)
else:
    n = abs(n)
    for i in range(i, n):
        res = res * a
    print(a, '^', n, '=', 1 / res)