print('-----------Программа №13(13)-----------')

number = (int(input('Введите число: ')))

i = 1
n = 0
for i in range(i, number + 1):
    if number % i == 0:
        n += 1
if n > 2:
    print('Число', number, 'составное')
else:
    print('Число', number, 'простое')