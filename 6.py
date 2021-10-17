print('введите номер задания')
k = int(input())
while k <= 7 and k > 0:
    if k == 1:
        print('Поменять местами содержимое переменных A и B. Вывести новые значения A и B.')
        a = int(input())
        b = int(input())
        t = a
        a = b
        b = t
        print(a, b)
        print('введите номер задания')
        k = int(input())
        
    if k == 2:
        print('Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A, и вывести новые значения переменных A, B, C.')
        a = int(input())
        b = int(input())
        c = int(input())
        t = a
        a = c
        c = b
        b = t
        print(a, b, c)
        print('введите номер задания')
        k = int(input())
        
    if k == 3:
        print('Даны переменные A, B, C. Изменить их значения, переместив содержимое A в C, C — в B, B — в A, и вывести новые значения переменных A, B, C.')
        a = int(input())
        b = int(input())
        c = int(input())
        t = c
        c = a
        a = b
        b = t
        print(a, b, c)
        print('введите номер задания')
        k = int(input())
        
    if k == 4:
        print('Найти значение функции y при данном значении x')
        x = int(input())
        y = 3 * x ** 2 - 6 * x ** 2 - 7
        print(y)
        print('введите номер задания')
        k = int(input())

    if k == 5:
        print('Найти значение функции y при данном значении x')
        x = int(input())
        y = 4 * (x - 3) ** 6 - 7 * (x - 3) ** 3 + 2
        print(y)
        print('введите номер задания')
        k = int(input())

    if k == 6:
        print('Дано число A. Вычислить A8.')
        a = int(input())
        b = a ** 3
        c = b * b * a * a
        print(c)
        print('введите номер задания')
        k = int(input())

    if k == 7:
        print('Дано число A. Вычислить A15')
        a = int(input())
        b = a ** 4
        d = a ** 3
        c = b * d * d * d * a * a
        print(c)
        print('введите номер задания')
        k = int(input())
        
    
