import random as rd

def main_for_task():
    list_24 = [rd.randint(1, 5) for i in range(11)]
    print(task_24(list_24))

def task_24(list_24):
    value = 1 # искомое
    count = 0
    for i in range(len(list_24)):
        if list_24[i] == value:
            count+=1
    return f"task 24 - {list_24} count = {count}"

if __name__ == "__main__":
    main_for_task()