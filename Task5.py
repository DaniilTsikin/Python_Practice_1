#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

import math

def FindDistance2D(X1, Y1, X2, Y2):
    result = math.sqrt(math.pow(X2 - X1, 2) + (math.pow(Y2 - Y1, 2)))
    return result

X1 = float(input("Введите координату X для первой точки: "))
Y1 = float(input("Введите координату Y для первой точки: "))
X2 = float(input("Введите координату X для второй точки: "))
Y2 = float(input("Введите координату Y для второй точки: "))

distance = (FindDistance2D(X1, Y1, X2, Y2))

print(f'Расстояние между точками: {distance}')


