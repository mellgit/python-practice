def main_for_task():

    value_7 = 54321
    t7 = task_7(value_7)
    print(f"task 7 - {t7}")

    value_8 = 1234
    print(f"task 8 - ")
    task_8(value_8)

    value_9 = 95432
    print(f"task 9 - ")
    task_9(value_9)

    value_10 = 5
    t10 = task_10(value_10)
    print(f"task 10 - {t10}")

    value_11 = 12
    t11l = task_11_loop(value_11)
    print(f"task 11l - {t11l}")

    # t11r = task_11_recursion(value_11)
    # print(f"task 11r - {t11r}")


def task_7(value_7):
    str_val_7 = str(value_7)
    revers_val_7 = int(str_val_7[::-1])
    return revers_val_7


def task_8(value_8):
    str_val_8 = str(value_8)

    list_8 = [int(str_val_8[i]) for i in range(len(str_val_8))]
    print(list_8)
    count_sum = 0
    for i in range(len(list_8)):
        count_sum += list_8[i]
    print(f"\tsum = {count_sum}")

    count_mux = 1
    for i in range(len(list_8)):
        count_mux *= list_8[i]
    print(f"\tmux = {count_mux}")


def task_9(value_9):
    str_val_9 = str(value_9)

    list_9 = [int(str_val_9[i]) for i in range(len(str_val_9))]
    print(list_9, end=' ')

    count_chet = 0
    count_ne_chet = 0
    for i in range(len(list_9)):
        if list_9[i] % 2 == 0:
            count_chet += list_9[i]
        else:
            count_ne_chet += list_9[i]

    print(f'\tchet - {count_chet}, ne_chet - {count_ne_chet}')


def task_10(value_10):

    if value_10 == 0:  # 0! = none
        return 0
    elif value_10 == 1:  # 1! = 1
        return 1

    fac_list = [1, ]  # когда факториал больше 1
    i = 1
    while i < value_10:
        fac = fac_list[-1] * (i+1)  # сумма последнего элемента и i+1
        fac_list.append(fac)  # добавление факториала в список
        i += 1
    return fac


def task_11_loop(value_11):

    f_list = [0, ]
    i = 1
    if value_11 == 0:  # позиции 0 нет
        return 'no position'

    elif value_11 == 1:  # если позиция 1
        return f_list

    else:  # если позиция больше 1
        f_list = [0, 1]
        while i < value_11-1:
            # сложение предыдущего и текущего элемента
            f_list.append(f_list[i-1] + f_list[i])
            i += 1
        return f_list


def task_11_recursion(value_11):  # не особо рабочий

    if value_11 <= 1:
        return 1

    return task_11_recursion(value_11 - 1) + task_11_recursion(value_11 - 2)


if __name__ == "__main__":
    main_for_task()
