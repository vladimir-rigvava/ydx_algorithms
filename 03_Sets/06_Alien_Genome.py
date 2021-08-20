"""
Геном жителей системы Тау Кита содержит 26 видов оснований, для обозначения которых будем использовать буквы латинского
алфавита от A до Z, а сам геном записывается строкой из латинских букв. Важную роль в геноме играют пары соседних
оснований, например, в геноме «ABBACAB» можно выделить следующие пары оснований: AB, BB, BA, AC, CA, AB.

Степенью близости одного генома другому геному называется количество пар соседних оснований первого генома,
которые встречаются во втором геноме.

Вам даны два генома, определите степень близости первого генома второму геному. Программа получает на вход две строки,
состоящие из заглавных латинских букв. Каждая строка непустая, и её длина не превосходит 10^5.

Программа должна вывести одно целое число – степень близости генома,
записанного в первой строке, геному, записанному во второй строке.
"""
g1 = {}
g2 = {}
tmp = list(input())
for i in range(1, len(tmp)):
    g1[tmp[i-1]+tmp[i]] = g1.get(tmp[i-1]+tmp[i], 0) + 1
tmp = list(input())
for i in range(1, len(tmp)):
    g2[tmp[i-1]+tmp[i]] = g2.get(tmp[i-1]+tmp[i], 0) + 1

diff = set(g1).intersection(set(g2))
closeness = 0
for gene in diff:
    closeness += g1[gene]

print(closeness)