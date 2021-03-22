import math as m


def main_for_task():
    a_side = 3
    value_2 = 9
    value_3 = 555

    t1 = task_1(a_side)
    print(f"task 1 - {t1}")
    t2 = task_2(value_2)
    print(f"task 2 - {t2}")
    t3 = task_3(value_3)
    print(f"task 3 - {t3}")

# Найти площадь и периметр прямоугольного треугольника


def task_1(a_side):
    high = m.sqrt(a_side**2 - (a_side/2)**2)
    return f"peremetr = {a_side*3}; s = {round(a_side*high/2, 2)}"

# Побитовые операции. Двоичное представление числа


def task_2(value_2):
    only_value = bin(value_2)
    value_str = str(only_value)
    return value_str[2:]

# Сумма цифр трехзначного числа


def task_3(value_3):
    value_str = str(value_3)
    list_3 = [int(value_str[i]) for i in range((len(value_str)))]
    return sum(list_3)


if __name__ == "__main__":
    main_for_task()
