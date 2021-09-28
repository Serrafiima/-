print('введите номер задания')
x = int(input())
while x <= 5 and x > 0:
    if x == 1:
        print ('найти площадь и периметр прямоугольника по заданным сторонам')
        a = int(input())
        b = int(input())
        S = a * b
        P = 2 * (a + b)
        print(S)
        print(P)
        print('введите номер задания')
        x = int(input())

    if x == 2:
        print('найти длину окружности по заданному диаметру')
        import math
        d = int(input())
        L = math.pi * d
        print(L)
        print('введите номер задания')
        x = int(input())

    if x == 3:
        print('Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2')
        a = int(input())
        b = int(input())
        Q = (a + b) / 2
        print(Q)
        print('введите номер задания')
        x = int(input())

    if x == 4:
        print('Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов')
        a = int(input())
        b = int(input())
        C1 = a ** 2 + b ** 2
        C2 = a ** 2 - b ** 2
        C3 = a ** 2 * b ** 2
        C4 = a ** 2 / b ** 2
        print(C1, C2, C3, C4)
        print('введите номер задания')
        x = int(input())

    if  x == 5:
        print('Даны два ненулевых числа. Найти сумму, разность, произведение и частное их модулей')
        a = int(input())
        b = int(input())
        a = abs(a)
        b = abs(b)
        C1 = a + b
        C2 = a - b
        C3 = a * b
        C4 = a / b
        print(C1, C2, C3, C4)
        print('введите номер задания')
        x = int(input())






