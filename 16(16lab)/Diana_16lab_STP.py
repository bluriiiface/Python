print('-----------Программа №16(16)-----------')

k = 0
n = int(input('Введите количество банкнот: '))
print('Введите банкноты через enter: ')
i = 0
result = 'Номера билетов Сигизмунда:'
while i < n:
    ticket = str(input())
    if ticket[0] == 'a' and ticket[4] == '5' and ticket[5] == '5' and ticket[6] == '6' and ticket[7] == '6' and ticket[8] == '1':
        result = result + ' ' + ticket
    else:
        k = k + 1
    i = i + 1
if k == n:
    print("-1")
else:
    print(result)

