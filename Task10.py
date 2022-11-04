#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def FindPairProduct(list):

    product_list = []
    for i in range(len(list)):
        product_list.append(list[i] * list[(i + 1) * -1])
        if(len(list)%2 == 0):
            if(i+1 == len(list)//2):
                break
        if(len(list)%2 != 0):
            if(i == len(list)//2):
                break
    return product_list


N = int(input('Задайте количество элементов списка: '))

list = list(range(N))

for i in range(len(list)):
    list[i] = int(input("Введите значение элемента списка: "))

print(list)

print(FindPairProduct(list))