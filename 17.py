print('введите номер задания')
k = int(input())
while k <= 5 and k > 0:
    if k == 1:
        print('Дан массив размера N и целые числа K и L (1 ≤ K ≤ L ≤ N). Найти \
среднее арифметическое элементов массива с номерами от K до L включительно.')
        n = int(input('N = '))
        a = []
        print('введите данные в массив')
        for i in range(0, n):
            print('a[', i + 1, '] = ', end='')
            c = int(input())
            a.append(c)
        k = int(input('K = '))
        l = int(input('L = '))
        s = 0
        for i in range(k - 1, l):
            s = s + a[i]
        d = s / (l - k + 1)
        print(d)
        print('введите номер задания')
        k = int(input())

    if k == 2:
        print('Дан целочисленный массив размера N,\
не содержащий одинаковых чисел. Проверить, образуют ли \
его элементы арифметическую прогрессию. \
Если образуют, то вывести разность прогрессии, если нет — вывести 0.')
        n = int(input('N = '))
        a = []
        print('введите данные в массив')
        for i in range(0, n):
            print('a[', i + 1, '] = ', end='')
            c = int(input())
            a.append(c)
        p = 1
        for i in range(1, n - 1):
            if a[i] - a[i - 1] != a[i + 1] - a[i]:
                print(0)
                p = 0
                break
        if p == 1: print(a[1] - a[0])
        print('введите номер задания')
        k = int(input())

    if k == 3:
        print('Дан массив A размера N. \
Найти минимальный элемент из его элементов с четными номерами: A2, A4, A6,')
        n = int(input('N = '))
        a = []
        print('введите данные в массив')
        for i in range(0, n):
            print('a[', i + 1, '] = ', end='')
            c = int(input())
            a.append(c)
        mn = a[1]
        for i in range(0, n):
            if (i + 1) % 2 == 0:
                if mn > a[i]:
                    mn = a[i]
        print(mn)
        print('введите номер задания')
        k = int(input())

    if k == 4:
        print('Дан массив размера N. Найти номер его последнего локального максимума')
        n = int(input('N = '))
        a = []
        print('введите данные в массив')
        for i in range(0, n):
            print('a[', i + 1, '] = ', end='')
            c = int(input())
            a.append(c)
        p = 0
        if a[0] > a[1]:
            p = 0
        for i in range(1, n - 1):
            if a[i] > a[i - 1] and a[i] > a[i + 1]:
                p = i
            if a[i] < a[i + 1] and i == n - 2: p = n - 1
        print('Локальный максимум: a[', p + 1, '] = ', a[p])
        print('введите номер задания')
        k = int(input())

    if k == 5:
        print('Дан целочисленный массив размера N, содержащий ровно два одинаковых элемента.\
Найти номера одинаковых элементов и вывести эти номера в порядке возрастания')
        n = int(input('N = '))
        a = []
        print('введите данные в массив')
        for i in range(0, n):
            print('a[', i + 1, '] = ', end='')
            c = int(input())
            a.append(c)
        p1 = 0
        p2 = 0
        t = 0
        for i in range(0, n):
            for c in range (i, n):
                if a[i] == a[c] and i != c:
                    t = 1
                    p1 = i + 1
                    p2 = c + 1
                    print('a[',p1,'] = a[', p2,'] = ', a[i])
                    break
                if t == 1:
                    break
        print('введите номер задания')
        k = int(input())

    
