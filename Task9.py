#Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

N = int(input('Введите число N: '))

list = list(range(1, N+1))
sum = 0
for i in range(len(list)):
    if(list[i] % 2 == 0):
        sum += list[i]

print(list)
print(sum)