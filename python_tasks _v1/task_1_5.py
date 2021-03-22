def main_for_task():
    list_a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89, 19, 99]
    list_b = [1, 2, 3, 4, 5, 6, 73, 82, 91, 10, 11, 12, 13]
    dict_a = {"bmw": 13, "audi": 6, "merin": 10}
    dict_b = {12: "tom", 1: "tom", 2: "tom"}
    my_dict_t5 = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5875, 'f': 20}

    print("task 1 - ", end=' ')
    task_1(list_a)

    value_tesk_2 = task_2(list_a, list_b)
    print(f"\ntask 2 - {value_tesk_2}")

    print("task 3 - ", end=' ')
    task_3(dict_a)

    print("task 4 - ", end=' ')
    task_4(dict_a, dict_b)

    print("task 5 - ", end=' ')
    task_5(my_dict_t5)


def task_1(list_a):
    list_a = [print(list_a[elem], end=' ')
              for elem in range(len(list_a)) if list_a[elem] < 5]


def task_2(list_a, list_b):
    like_list = [int(list_a[i]) for i in range(len(list_a)) if list_a[i] not in list_b]
    return like_list


def task_3(dict_a):
    key_dict_a = ["bmw", "audi", "merin"]
    for i in range(len(key_dict_a) - 1):
        for j in range(len(key_dict_a) - i - 1):
            if dict_a[key_dict_a[j]] > dict_a[key_dict_a[j + 1]]:  # разница в знаке тут
                dict_a[key_dict_a[j]], dict_a[key_dict_a[j + 1]
                                              ] = dict_a[key_dict_a[j + 1]], dict_a[key_dict_a[j]]
    print(dict_a, end=' ')

    for i in range(len(key_dict_a) - 1):
        for j in range(len(key_dict_a) - i - 1):
            if dict_a[key_dict_a[j]] < dict_a[key_dict_a[j + 1]]:
                dict_a[key_dict_a[j]], dict_a[key_dict_a[j + 1]
                                              ] = dict_a[key_dict_a[j + 1]], dict_a[key_dict_a[j]]
    print(dict_a)


def task_4(dict_a, dict_b):
    dict_a.update(dict_b)
    print(dict_a)


def task_5(my_dict_t5):
    key_my_dict = ['a', 'b', 'c', 'd', 'e', 'f']
    list_for_value = []
    for i in range(len(key_my_dict)):
        list_for_value.append(my_dict_t5[key_my_dict[i]])

    list_for_value.sort()
    print(list_for_value[-3:])
