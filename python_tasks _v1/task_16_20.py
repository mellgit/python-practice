import os


def main_for_task():
    value_17 = 23
    value_18 = 'hello my best friend'
    value_19_1 = 10
    value_19_2 = 5
    path = r''
    list_20 = [23, 25, 30, 44, 60, 75]

    print("task 16 - ", end=' ')
    task_16(path)
    print("task 17 - ", end=' ')
    task_17(value_17)
    print("task 18 - ", end=' ')
    task_18(value_18)
    print("task 19 - ", end=' ')
    task_19(value_19_1, value_19_2)
    print("task 20 - ", end=' ')
    task_20(list_20)


def task_16(path):
    path = input("enter path: ")
    for i in os.listdir(path):
        print(f"\t {i}")


def task_17(value_17):
    value_str = str(value_17)
    list_17 = [int(value_str[elem]) for elem in range(len(value_str))]
    print(sum(list_17))


def task_18(value_18):
    serch_value = 'e'
    count = 0
    for i in range(len(value_18)):
        if serch_value == value_18[i]:
            count += 1
    print(count)


def task_19(value_19_1, value_19_2):
    print(f'{value_19_1}-{value_19_2}', end=' ')
    midway = value_19_1
    value_19_1 = value_19_2
    value_19_2 = midway
    print(f'{value_19_1}-{value_19_2}')


def task_20(list_20):
    print((lambda i: [elem for elem in list_20 if elem % 15 == 0])(list_20))
