#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def FindProduct(list1, list2):
    product = 1
    for i in range(len(list2)):
        product *= list1[list2[i]]
    return product

N = int(input('Введите число N: '))

first_list = list(range(-N, N+1))
second_list = list(range(5))

for i in range(len(second_list)):
    second_list[i] = int(input("Введите номер индекса: "))

print(first_list)
print(second_list)
print(FindProduct(first_list, second_list))