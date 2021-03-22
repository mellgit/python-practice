def main_for_task():
    list_21 = [12, 'qwe', 432, False]
    str_22 = """    hi my best friend!
    how you feel my friend?
    I will miss you my brooooooo
    """

    print("task 21 - ", end=' ')
    task_21(list_21)
    print("task 22 - ", end=' ')
    task_22_1(str_22)
    task_22_2(str_22)


def task_21(list_21):
    set_20 = set(list_21)
    if len(set_20) == len(list_21):
        print('unique')
    else:
        print('no unique')
    print(list_21)
    print(set_20)


def task_22_1(str_22):
    # заполнение словами список, без знаков
    list_22 = str_22.replace('?', '').replace('!', '').replace('\n', '').split()

    # запонение списка числами, которые равны длиннам каждого элемента
    list_22_v1 = [len(elem) for elem in list_22]

    index_value = max(list_22_v1)  # нахождение max значения в списке
    self_index = list_22_v1.index(index_value)  # нахождение индекса max значения
    print(f"long:{list_22[self_index]};", end=' ')

    # ['hi', 'my', ...] - сопоставляем индексы первого и второго списка и находим слово
    # [0, 1, ...]


def task_22_2(str_22):
    list_22 = str_22.replace('?', '').replace('!', '').replace('\n', '').split()
    # заполнение списка значениями
    list_22_v2 = [list_22.count(elem) for elem in list_22]

    index_value = max(list_22_v2)
    self_index = list_22_v2.index(index_value)
    print(f"frequent:{list_22[self_index]}")
