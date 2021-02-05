import random as rand


def main_for_task():
    list_14 = [23, 43, False, 'hi', 23]
    t14 = task_14(list_14)
    print(f"task 14 - {t14}")

    list_15 = [rand.randint(1, 100) for i in range(11)]
    t15 = task_15(list_15)
    print(f"task 15 - {t15}")

    list_16_1 = [rand.randint(1, 20) for i in range(11)]
    list_16_2 = [rand.randint(1, 20) for i in range(11)]
    t16 = task_16(list_16_1, list_16_2)
    print(f"task 16 - {t16} \n{list_16_1} \n{list_16_2}")


def task_14(list_14):
    list_14_1 = set(list_14)
    if len(list_14_1) == len(list_14):
        return True
    else:
        return False


def task_15(list_15):
    list_15_del = [list_15[i] for i in range(
        len(list_15)) if list_15[i] > 35 and list_15[i] < 65]
    return list_15_del


def task_16(list_16_1, list_16_2):
    list_16 = [list_16_1[i]
               for i in range(len(list_16_1)) if list_16_1[i] in list_16_2]
    if len(list_16) == 0:
        return 0
    return list_16


if __name__ == "__main__":
    main_for_task()
