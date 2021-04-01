print('-----------Программа №10(10)-----------')
print("Введите число и диапазоны через пробел")
S, L1, R1, L2, R2 = input().split(' ')
z = 0
S = int(S)
L1 = int(L1)
R1 = int(R1)
R2 = int(R2)
L2 = int(L2)
if S > (R1 + R2) or S < (L1 + L2):
    print('Таких чисел не существует\n', -1)
else:
    if (S - L1) >= L2:
        if S <= (L1 + R2):
            print('Такие числа существуют\n', L1, S - L1)
        else:
            z = abs (S - (L1 + R2))
            if (L1 + z) < R1 and (R2 - z) > L2:
                print('Такие числа существуют\n', L1 + z, S - (L1 + z))
            else:
                print('Таких чисел не существует\n', -1)
    else:
        print('Таких чисел не существует\n', -1)