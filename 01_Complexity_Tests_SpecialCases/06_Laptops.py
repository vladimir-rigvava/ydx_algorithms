'''
В школе решили на один прямоугольный стол поставить два прямоугольных ноутбука. 
Ноутбуки нужно поставить так, чтобы их стороны были параллельны сторонам стола. 
Определите, какие размеры должен иметь стол, чтобы оба ноутбука на него поместились, и площадь стола была минимальна.

Формат ввода
Вводится четыре натуральных числа, первые два задают размеры одного ноутбука, а следующие два — размеры второго. Числа не превышают 1000.

Формат вывода
Выведите два числа — размеры стола. Если возможно несколько ответов, выведите любой из них (но только один).
'''
l1, l2, n1, n2 = list(map(int, input().split(' ')))

lmax = max(l1, l2)
lmin = min(l1, l2)
nmax = max(n1, n2)
nmin = min(n1, n2)

# вар1: два минимума * maximum всех
sqr1 = (max(lmax, nmax), (lmin + nmin))
minpr = sqr1[0]*sqr1[1]
toprint = (sqr1[0], sqr1[1])

# вар2: макс1+мин2 * макс одного из
if lmax > nmax:
    sqr2 = ((lmax + nmin), max(lmin, nmax))
else:
    sqr2 = ((nmax + lmin), max(nmin, lmax))

if sqr2[0]*sqr2[1] < minpr:
    toprint = (sqr2[0], sqr2[1])

print(toprint[0], toprint[1])