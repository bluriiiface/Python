from math import fabs
print('-----------Программа №5(5)-----------')

print('Введите через пробел параметры x0, v0 и t:')
x0, v0, t = input().split()
x0 = int(x0)
v0 = int(v0)
t = int(t)
g = 9.8
xt = fabs((x0 + v0 * t - (g * t * t) / 2) - x0)

print('Положение после вычислений x(t)=', xt)

