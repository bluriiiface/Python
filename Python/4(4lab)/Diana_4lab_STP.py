print('-----------Программа №4(4)-----------')

number1 = input('Введите первое число: ')
number2 = input('Введите второе число: ')

number3 = number2
number2 = number1
number1 = number3

print('-----1 способ-----')
print('number1 =', number1)
print('number2 =', number2)

print('-----2 способ-----')
(number1, number2) = (number2, number1)
print('number1 =', number1)
print('number2 =', number2)


