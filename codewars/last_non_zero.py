"""
Ваша задача найти последнюю ненулевую цифру числа n! (факториал).

Пример:
если n = 12, ваша функция должна вернуть 6 поскольку 12! = 4 7 9 0 0 1 6 0 0

Вход
Неотрицательное целое число n
Диапазон: 0 - 2.5E6

Выход
Последняя ненулевая цифра n!

Примечание
Вычисление всего факториала приведет к тайм-ауту.
"""

import math

def main():
    print(last_digit(10000))

def last_digit(n):
    lb = str(math.factorial(n))[::-1]
    # for i in range(len(lb)):
    #     if lb[i] != '0':
    #         return int(lb[i])
    return [int(lb[i]) for i in range(len(lb)) if lb[i] != '0'][0]
    
        # if lb[i] != 0:
        #     return lb[i]

    

main()