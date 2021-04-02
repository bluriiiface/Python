from random import randint
print('-----------Программа №15(15)-----------')

random_number = randint(0, 100)

i = 1

for i in range(i, 5):
    n = (int(input('Введите число: ')))
    if n < random_number and i != 5:
        print('Загаданное число больше')
    elif n > random_number and i != 5:
        print('Загаданное число меньше')
    elif n == random_number:
        print('Поздравляю! Вы угадали число', random_number, '!')
        break

print('К сожалению, Вы проиграли. Было загадано число', random_number)
