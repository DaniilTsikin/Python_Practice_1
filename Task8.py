#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
#Пример списка ИНДЕКСОВ [2, 4, 3, 1, 8]
#Ввод: 10
#[-10, -9, ...-4, -3, -2, -1, 0, 1, 2, 3,4....10]

def FindProduct(list1, list2):
    product = 1
    for i in range(len(list2)):
        product *= list1[list2[i]]
    return product

N = int(input('Введите число N: '))
first_list = list(range(-N, N))
second_list = list(range(5))

for i in range(len(second_list)):
    second_list[i] = int(input('Введите номер индекса: '))

print(first_list)
print(second_list)
print(FindProduct(first_list, second_list))