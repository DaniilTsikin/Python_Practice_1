#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

dig_sum = map(int, str(float(input('Ввежите вещественное число: '))).replace('.', ''))
print(f'Сумма всех цифр {sum(dig_sum)}.')