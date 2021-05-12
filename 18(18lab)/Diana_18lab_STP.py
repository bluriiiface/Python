print('-----------Программа №18(18)-----------')

import collections
words = dict(collections.Counter('halloklempnerdasistfantastischfluggegecheimen'))

stopWord = str(input("Введите стоп слово: "))
f = [0] * len(stopWord)
b = str('halloklempnerdasistfantastischfluggegecheimen')
t = float(1)
q = 0

for i in range(len(stopWord)):
    for j in range(len(b)):
        if stopWord[i] == b[j]:
            f[i] = f[i] + 1
for i in range(len(stopWord)):
    if f[i] == 0:
        q = 1
if q == 1:
    print('Сигизмунд не знает букву')
else:
    for i in range(len(stopWord)):
        t = t * (words[stopWord[i]]/len(b))
    print("Вероятность равна: ", t)