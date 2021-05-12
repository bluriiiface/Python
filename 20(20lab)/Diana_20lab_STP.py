print('-----------Программа №20(20)-----------')

b = 0

cash, n = int(input("Введите число: ")), int(input())

drinks = [0] * n
price = [0] * n
V = [0] * n
rez = [0] * n
liter = [0] * n

for i in range(n):
    drinks[i], price[i], V[i] = map(str, input().split(' '))
    price[i] = int(price[i])
    V[i] = int(V[i])
    rez[i] = int(cash / price[i])
    liter[i] = rez[i] * V[i]
    if liter[i] == 0:
        b = b + 1

if b == n :
    print(-1)
    exit(0)

for i in range(n):
    for j in range(n):
        if liter[i] > liter[j]: k = i

print(drinks[k], rez[k])
print("Всего литров:", liter[k])
print("Оставшиеся деньги: ", cash - (price[k] * rez[k]))