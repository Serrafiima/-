print('введите номер задания')
import math
k = int(input())
while k <= 6 and k > 0:
    if k == 1:
        print('Дано значение угла α в градусах (0 < α < 360). Определить значение этого же угла в радианах.')
        a = int(input())
        a = a * math.pi / 180
        print(a)
        print('введите номер задания')
        k = int(input())

    if k == 2:
        print('Дано значение угла α в радианах (0 < α < 2·π). Определить значение этого же угла в градусах')
        a = float(input())
        a = a * 180 / math.pi
        print(a)
        print('введите номер задания')
        k = int(input())

    if k == 3:
        print('Известно, что X кг конфет стоит A рублей. Определить, сколько стоит 1 кг и Y кг этих же конфет.')
        a = int(input())
        x = int(input())
        kg = a / x
        print('один кг конфет стоит', kg)
        y = int(input())
        y = y * kg
        print(y)
        print('введите номер задания')
        k = int(input())
        
    if k == 4:
        print('Скорость первого автомобиля V1 км/ч, второго — V2 км/ч, расстояние между ними S км. \
Определить расстояние между ними через T часов, если автомобили удаляются друг от друга. ')
        v1 = int(input())
        v2 = int(input())
        S = int(input())
        t = int(input())
        S = S + t * v1 + t * v2
        print(S)
        print('введите номер задания')
        k = int(input())
        
    if k == 5:
        print('Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).')
        A = int(input())
        B = int(input())
        x = (-B) / A
        print(x)
        print('введите номер задания')
        k = int(input())
        
    if k == 6:
        print('Найти решение системы линейных уравнений вида A1·x + B1·y = C1, A2·x + B2·y = C2')
        a1 = int(input("А1 = "))
        b1 = int(input("В1 = "))
        c1 = int(input("С1 = "))
        a2 = int(input("А2 = "))
        b2 = int(input("В2 = "))
        c2 = int(input("С2 = "))
        x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
        y = (c1 * a2 - c2 * a1) / (b2 * a1 - a2 * b1)
        if x == -0 or y == -0:
            x = abs(x)
            y = abs(y)
        print("х = ", x, "у = ", y)
        print('введите номер задания')
        k = int(input())
        
        
            
        
        
        
        
