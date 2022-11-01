#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число: '))
print(*[((1 + 1 / m) ** m) for m in range(1, n + 1)])
print(f'Сумма чисел последовательности: {(round(sum(list(map(lambda m: ((1 + 1 / m) ** m), range(1, n + 1)))), 3))}')

print(first_list)
print(second_list)
print(FindProduct(first_list, second_list))