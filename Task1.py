#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

while (ValueError):
    try:
        day = int(input('Введите число обозначающее день недели: ')) 
        while(day <1 or day>7): 
            print("В неделе 7 дней")
            day = int(input('Введите число обозначающее день недели: '))       

    except  ValueError:
        print("Вы ввели что-то не то, в неделе 7 дней")
    else:
        break


if (day > 5): print("Это выходной день")

else: print("Это будний день")


