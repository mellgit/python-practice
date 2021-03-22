def main_for_task():
    str_21 = 'h e l l o f r i e n d'
    t21 = task_21(str_21)
    print(f"task 21 - {t21}")

    str_22 = 'hell31 77wo0rld'
    t22 = task_22(str_22)
    print(f"task 21 - {t22}")


def task_21(str_21):
    list_21 = str_21.split()
    my_str = "*".join(list_21)
    return my_str


def task_22(str_22):
    list_22 = []
    num = ''
    for char in str_22:  # поиск числа
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                list_22.append(int(num))
                num = ''
    if num != '':
        list_22.append(int(num))
        list_22.pop()
    return list_22


if __name__ == "__main__":
    main_for_task()
