# Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

while (ValueError):
    try:
        coordinateX = int(input('ВВведите координату Х: ')) 
        coordinateY = int(input('ВВведите координату Y: ')) 
        while((coordinateX == 0) and (coordinateY == 0)): 
            print("Вы в начале координат плоскости, попробуйте ввести другие числа")
            coordinateX = int(input('ВВведите координату Х: ')) 
            coordinateY = int(input('ВВведите координату Y: ')) 
            
    except  ValueError:
        print("Вы ввели что-то не то")
    else:
        break

if(coordinateX > 0 and coordinateY > 0):
    print("Вы в первой четверти")
elif(coordinateX < 0 and coordinateY > 0):
    print("Вы во второй четверти")
elif(coordinateX < 0 and coordinateY < 0):
    print("Вы в третьей четверти")
elif(coordinateX > 0 and coordinateY < 0):
    print("Вы в четвертой четверти")
elif(coordinateX == 0 and coordinateY > 0 or coordinateY < 0):
    print("Вы на оси Y")
else:
    print("Вы на оси X")