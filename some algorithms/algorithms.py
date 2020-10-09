#!/usr/bin/env python3

def main():
    print(
        " 1 - bubble sort\n",
        "2 - factorial\n",
        "3 - fibonacci numbers\n",
        "4 - levenshtein distance\n",
        "5 - inverted list\n",
    )
    while True:
        try:
            answer = int(input(">"))
            if answer == 1:
                nums = [1, 4, 3, 7, 10, 2]
                val_bubble = bubble_sort(nums)
                print(f"bubble sort {val_bubble}")
            elif answer == 2:
                value = 5
                val_factorial = factorial(value)
                print(f"factorial {value} = {val_factorial}")
            elif answer == 3:
                value = 5
                print(f"\nspecific row - {fibonacci_numbers(value)}")
            elif answer == 4:
                dic_lev1 = "hello"
                dic_lev2 = "hello"
                print(f"number of fixes - {levenshtein_distance(dic_lev1, dic_lev2)}")
            elif answer == 5:
                inv_list = [1, 2, 3]
                inverted_list(inv_list)
            elif answer == 0:
                break
        except Exception as ex:
            print(ex)


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
    f1 = f2 = 1
    print(f"fibonacci numbers {value} = {f1} {f2}", end=' ')

    for i in range(2, value):
        f1, f2 = f2, f1+f2
        print(f2, end=' ')

    return f2

# расстояние левенштейна (редакционное расстояние) - отредактировать одну строку, чтобы она была похожа на другую


def levenshtein_distance(a, b):
    print(f"{a}\n{b}")
    def rec(i, j):
        if i == 0 or j == 0:
            # если строка пустая, то расстояние равняется ее длине
            return max(i, j)
        elif a[i-1] == b[j-1]:
            # если последние символы одинаковые, просто съедаем их
            return rec(i-1, j-1)
        else:
            # иначе считаем минимальный вариант
            return 1 + min(
                rec(i, j-1),  # удаление символа
                rec(i-1, j),  # вставка символа
                rec(i-1, j-1),  # замена символа
            )
    return rec(len(a), len(b))


def inverted_list(inv_list):
    print(inv_list)
    print(inv_list[::-1])


def linked_list():
    # linked_list()
    # чаще всего просят развернуть этот список
    pass


if __name__ == "__main__":
    main()
