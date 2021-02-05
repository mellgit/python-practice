import math as m
import random


def main_for_task():

    try:
        equation = '+1*xx-70*x+600=0'  # == x^2-70x+600=0
        print(f"task 4 - ", end='')
        task_4(equation)

        print(f"task 5 - ")
        task_5()

        print(f"task 6 - ")
        x, y = [int(input(f"\tcoordinat{i+1} - ")) for i in range(2)]
        task_6(x, y)
    except Exception as exp:
        print(exp)

# Найти корни квадратного уравнения


def task_4(equation):
    list_4 = []
    list_4_symbol = []
    num_list = []
    num = ''

    for i in range(len(equation)):  # поиск знака перед числами
        if equation[i] == '-' or equation[i] == '+':
            list_4_symbol.append(equation[i])
    """
    Данный цикл не заносит последнее значение,
    тк поле последнего числа ничего нет и цикл завершается.
    Чтобы добавить последнее число в list_4,
    после цикла идет условие, чтобы добавить последнее число
    """
    for char in equation:  # поиск числа
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                list_4.append(int(num))
                num = ''
    if num != '':
        list_4.append(int(num))
        list_4.pop()

    for i in range(len(list_4_symbol)):  # запись коэффицентов со знаками
        if list_4_symbol[i] == '+':
            num_list.append(list_4[i])
        if list_4_symbol[i] == '-':
            num_list.append(-list_4[i])

    def task_4_discrim(num_list):  # поиск дискриминанта
        discrim = num_list[1]**2 - 4*num_list[0]*num_list[2]
        root_discrim = m.sqrt(discrim)
        return round(root_discrim)

    def task_4_root(num_list, root_discrim):  # поиск корней
        root_x1 = (-num_list[1] - root_discrim)/(2*num_list[0])
        root_x2 = (-num_list[1] + root_discrim)/(2*num_list[0])

        print("x1 = ", round(root_x1, 3), end='\t')
        print("x2 = ", round(root_x2, 3))

    root_discrim = task_4_discrim(num_list)
    task_4_root(num_list, root_discrim)

# Определить существование треугольника по трем сторонам


def task_5():
    # вводят значения сторон треугольника
    a, b, c = [int(input(f"\tsid{i+1} - ")) for i in range(3)]

    if a + b > c and a + c > b and b + c > a:
        print("triangle exists")
    else:
        print("triangle not exists")


# Принадлежит ли точка кругу


def task_6(x, y):
    radius = 5
    center_a, center_b = 0, 0
    value_circle = (x-center_a)**2+(y-center_b)**2
    # значение найденного радиуса
    value_circle = round(m.sqrt(value_circle), 2)

    if value_circle < radius:
        print('insid the circle')
    if value_circle == radius:
        print('on the circle')
    if value_circle > radius:
        print('outsid the circle')


if __name__ == "__main__":
    main_for_task()
