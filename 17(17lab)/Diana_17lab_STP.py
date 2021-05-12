print('-----------Программа №17(17)-----------')

count = 37
mas = [0] * count
i = 0
t = 0
redNumb = 0
blackNumb = 0
p = 0
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
for i in range(37):
    mas[i] = 0
while True:
    u = 0
    use = 0
    notUse = 0
    numb = (int(input('Введите число: ')))
    if numb < 0:
        break
    else:
        mas[numb] += 1
        for t in range(18):
            if numb == red[t]:
                redNumb += 1
                break
            elif t == 17:
                blackNumb += 1
                break
    for u in range(37):
        if mas[u] > p:
            p = mas[u]
    for use in range(37):
        if mas[use] == p:
            print("Часто используемые номера: ", use)
    print("Не используемые номера: ")
    for notUse in range(37):
        if mas[notUse] == 0:
            print(notUse, end=" ")
    print("\n", "Красные: ", redNumb, " Черные: ", blackNumb)