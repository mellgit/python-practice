from random import randint

def main():

    print(
        " 1 - palindrome\n",
        "2 - binary search\n",
        "0 - exit\n",
    )
    while True:
        try:
            answer = int(input(">"))
            if answer == 1:
                string = '1001'
                print(palindrome(string))
            elif answer == 2:
                random_set = set([randint(1, 100) for i in range(1,11)])
                sort_list = list(sorted(random_set))
                print(binary_search(sort_list))
            elif answer == 0:
                break
        except Exception as ex:
            print(ex)


def palindrome(string):
    print(f"{string} \n{string[::-1]}")
    return True if string[::-1] == string else False

def binary_search(sort_list):
    print(sort_list)
    serch_value = int(input('enter serch value: '))
    mid = len(sort_list) // 2 # находит середину значение середины списка
    low = 0 # начало списка
    high = len(sort_list) - 1 # конец списка

    """
    список будет делиться на половину и число, 
    которое оказалось посередине сравнивается с искомым, 
    если число больше, то переходим в правую часть списка,
    иначе в левую 
    и делаем тоже самое в середине половинного списка,
    и так пока не надем нужное нам число
    """

    while sort_list[mid] != serch_value and low <= high:
        if serch_value > sort_list[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    
    return f"No value" if low > high else f"ID = {mid}"



if __name__ == "__main__":
    main()