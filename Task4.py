#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

while (ValueError):
    try:
        quarterNumber = int(input('Введите номер четверти: ')) 
        while(quarterNumber < 1 or quarterNumber > 4): 
            print("Неправильный номер, введите число от 1 до 4")
            quarterNumber = int(input('Введите номер четверти: ')) 
            
    except  ValueError:
        print("Вы ввели что-то не то")
    else:
        break

if(quarterNumber == 1):
    print("Доступный диапазон координат X > 0 и Y > 0")
elif(quarterNumber == 2):
    print("Доступный диапазон координат X < 0 и Y > 0")
elif(quarterNumber == 3):
    print("Доступный диапазон координат X < 0 и Y < 0")
else:
    print("Доступный диапазон координат X > 0 и Y < 0")
