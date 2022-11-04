#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


list = [1.15, 4.1, 14.43, 15.6]

def FindTheDifference(list):
    max = list[0] % 1
    min = list[0] % 1

    for i in range(len(list)):
        
        if(list[i] % 1 > max):
            max = list[i] % 1
        if(list[i] % 1 < min):
            min = list[i] % 1
    print(max)
    print(min)
    result = max - min
    return result

print(FindTheDifference(list))
        
