def main_for_task():
    my_list = ['qwe', 'asd', 'zxc', 'vbn', 'fgh', ]
    list_14 = [1, 23, 43, 44, 66, 943, 34, 55, 237, 21, 33, 22, 444]
    list_15_1 = [123, 'qwe', 33, 21, 'asd']
    list_15_2 = [321, 'qwe', 663, 201, 'asd']
    value13 = 18
    filename_12 = 'test.cvs'

    print("task 11 - ", end=' ')
    task_11(my_list)
    print("task 12 - ", end=' ')
    task_12(filename_12)
    print("task 13 - ", end=' ')
    task_13(value13)
    print("task 14 - ", end=' ')
    task_14(list_14)
    print("task 15 - ", end=' ')
    task_15(list_15_1, list_15_2)


def task_11(my_list):
    print(f'first - {my_list[0]} \t last - {my_list[-1]}')


def task_12(filename_12):
    list_expansion = ['txt', 'psd', 'cvs']  # список для проверки
    word_revers = filename_12[::-1]  # реверсивная строка
    list_12 = []
    for i in range(len(word_revers)):  # чтения реверсивной строки до точки
        if word_revers[i] == '.':
            break
        # занесение в список название расширения
        list_12.append(word_revers[i])
    value = ''.join(list_12)  # преобразование списка в строку
    # реверсирование, чтобы расширения не читались справа налево
    value_revers = value[::-1]
    if value_revers in list_expansion:  # проверка на существования расширения
        print('there is such an extension')
    else:
        print('no such expansion')


def task_13(value13):
    print(value13 + value13 ** 2 + value13 ** 3)


def task_14(list_14):
    for i in range(len(list_14)):
        if list_14[i] % 2 == 0:
            print(list_14[i], end=' ')
        elif list_14[i] == 237:
            print()
            break


def task_15(list_15_1, list_15_2):
    list_15_3 = [print(list_15_1[i], end=' ') for i in range(
        len(list_15_1)) if list_15_1[i] != list_15_2[i]]
    print()
