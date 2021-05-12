print('-----------Программа №27(25)-----------')

import random


def Coutline(a, max, remember):
    for remember in range(remember, max):
        print(a[remember], end=" ")
    print()


def BozoSort(a, max):
    sorted = False
    while sorted == False:
        x1 = random.randint(0, max-1)
        x2 = random.randint(0, max-1)

        swap = a[x1]
        a[x1] = a[x2]
        a[x2] = swap

        sorted = True
        for i in range (1, max):
            if (a[i-1] < a[i]):
                sorted = False
                break
    return a

n = int(input("Введите число: "))
a = list(map(int, input().split()))
line = []
temp = []
max = 0
remember = 0
t = 0
for i in range(n):
    line.append(a[t])
    t += 1
    max += 1
    if max <= 5:
        temp = BozoSort(line, max)
        Coutline(temp, max, remember)
    else:
        remember = max - 5
        temp = BozoSort(line, max)
        Coutline(temp, max, remember)