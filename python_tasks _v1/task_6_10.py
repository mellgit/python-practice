import time


def main_for_task():
    value_6 = 3
    word_for_polindrom = ''
    value_for_task_10 = '1,2,3,4,5,6,7'
    value_7 = 6

    print("task 6 - ", end=' ')
    task_6(value_6)
    print("task 7 - ")
    task_7(value_7)

    print("task 8 - ", end=' ')
    task_8(word_for_polindrom)

    print("task 9 - ", end=' ')
    task_9()

    print("task 10 - ", end=' ')
    task_10(value_for_task_10)


def task_6(value):
    value_str = str(value)
    print(int(value_str, 16))


def task_7(value_7):
    row = [1]
    y = [0]
    for x in range(max(value_7, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]


def task_8(word_for_polindrom):
    word_for_polindrom = input('enter polindrom: ')
    word_reverse = word_for_polindrom[::-1] # реверс строки
    if word_for_polindrom == word_reverse:
        print('polindrom')
    else:
        print('no polindrom')


def task_9():
    print(time.ctime())


def task_10(value_for_tesk_10):
    value_list = value_for_tesk_10.split(',')
    value_tuple = tuple(value_list)
    print(value_list, value_tuple)
