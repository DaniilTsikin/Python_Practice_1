

N = int(input('Введите количество чисел фибоначчи: '))


fib_list = list(range(N))

for i in range(len(fib_list)):
    if(N == 2):
        fib_list[0] = 1
        fib_list[1] = 1
        break
    elif(N == 1):
        fib_list[0] = 1
        break
    fib_list[0] = 1
    fib_list[1] = 1
    fib_list[i] = fib_list[i-1] + fib_list[i-2]

print(fib_list)