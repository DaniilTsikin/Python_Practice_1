# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле Task9.txt в одной строке одно число.

from functools import reduce
import random


n = random.randint(5, 10)

list = [i for i in range(-n, n+1)]

print('Задан список: ', list, '\n')

with open('Task9.txt', 'w') as data: 
    for i in range(int(n/2)):
        data.write(f'{random.randint(0, n*2)}\n')


def read2list(file):    
    with open(file, 'r') as file:
        position_index = [int(line.strip()) for line in file.readlines()]
        position_index.sort()
        print('Выбраны позиции с индексами: \t', *position_index)
        return position_index


position_index = read2list('Task9.txt')
position_element = [list[i] for i in position_index]
mult = reduce((lambda x, y: x*y), position_element)

print('Элементы на указанных позициях:\t', *position_element,
      '\nИх произведение равно : \t', mult, '\n')