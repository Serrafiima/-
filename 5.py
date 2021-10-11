print("введите номер задания")
k = int(input())
import math
while k >= 1 and k < 6:
    if k == 1:
        print('Найти расстояние между двумя точками с заданными координатами (x1, y1) и (x2, y2)')
        x1 = int(input())
        y1 = int(input())
        x2 = int(input())
        y2 = int(input())
        d = math.sqrt((x1 + x2) ** 2 + (y1 + y2) ** 2)
        print(d)
        print("введите номер задания")
        k = int(input())
        
    if k == 2:
        print('Даны три точки A, B, C на числовой оси. Найти длины отрезков AC и BC и их сумму.')
        a = int(input())
        b = int(input())
        c = int(input())
        dAC = abs(a - c)
        dBC = abs(b - c)
        S = dAB + dBC
        print(dAC, dBC, S)
        print("введите номер задания")
        k = int(input())
        
    if k == 3:
        print('Даны три точки A, B, C на числовой оси.Точка C расположена между точками A и B. Найти произведение длин отрезков AC и BC')
        a = int(input())
        b = int(input())
        c = int(input())
        dAC = abs(a - c)
        dBC = abs(b - c)
        C = dAC * dBC
        print(C)
        print("введите номер задания")
        k = int(input()) 
        
    if k == 4:
        print('Найти периметр и площадь прямоугольника по заданным вершинам')
        x1 = int(input())
        y1 = int(input())
        x2 = int(input())
        y2 = int(input())
        AB = abs(x1 - x2)
        BC = abs(y1 - y2)
        P = 2 * (AB + BC)
        S = AB * BC
        print(P, S)
        print("введите номер задания")
        k = int(input())
        
    if k == 5:
        print('Даны координаты трех вершин треугольника: (x1, y1), (x2, y2), (x3, y3). Найти его периметр и площадь')
        x1 = int(input())
        y1 = int(input())
        x2 = int(input())
        y2 = int(input())
        x3 = int(input())
        y3 = int(input())
        d1 = math.sqrt((x1 + x2) ** 2 + (y1 + y2) ** 2)
        d2 = math.sqrt((x2 + x3) ** 2 + (y2 + y3) ** 2)
        d3 = math.sqrt((x1 + x3) ** 2 + (y1 + y3) ** 2)
        P = d1 + d2 + d3
        p = P / 2
        S = math.sqrt(p * (p - d1) * (p - d2) * (p - d3))
        print(P, S)
        print("введите номер задания")
        k = int(input())
        
    
        
