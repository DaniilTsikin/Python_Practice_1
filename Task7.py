#Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
#Пример:
#- Для n = 15:  Ответ: 3
#- Для n = 35:  Ответ: 5

N = int(input('Введите число N: '))
def smallest_divisor(N):
    number = 2
    while(N%number != 0):
        number += 1
    return number

print(smallest_divisor(N))