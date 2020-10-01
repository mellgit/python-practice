#!/usr/bin/env python3

def main():
    # bubble
    nums = [1, 4, 3, 7, 10, 2]
    # val_bubble = bubble_sort(nums)
    # print(f"bubble sort {val_bubble}")

    # factorial
    value = 5
    val_factorial = factorial(value)
    # print(f"factorial {value} = {val_factorial}")

    # fibonacci numbers
    # fibonacci_numbers(value)

    # Levenshtein distance 
    # расстояние левенштейна - как неточное сравнение или
    # насколько строка призко схожа с другой (редакционное расстояние)
    # сколько действий необходимо совершить
    # редакционное расстояние - отредактировать одну строку, чтобы она была похожа на другую


    # singly linked list односвязный список
    # чаще всего просят развернуть этот список

    # inverted list
    inv_list = [1,2,3]
    inverted_list(inv_list)

def bubble_sort(nums):

    print(nums)
    for i in range(len(nums)):
        for j in range(len(nums) - i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums


def factorial(value):
    if value == 0:
        return 1
    fac = 1
    i = 1
    while i < value:
        i += 1
        fac *= i
    return fac

def fibonacci_numbers(value):
    f1=f2=1

    print(f1, end=' ')
    print(f2, end=' ')
    

    for i in range(2,value):
        f1,f2 =f2,f1+f2
        print(f2, end=' ')
    print()
    print(f2) # конкретный ряд

def levenshtein_distance():
    pass

def singly_linked_list():
    pass

def inverted_list(inv_list):
    print(inv_list)
    print(inv_list[::-1])
    
if __name__ == "__main__":
    main()
