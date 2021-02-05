import task_1_5 as t1_5
import task_6_10 as t6_10
import task_11_15 as t11_15
import task_16_20 as t16_20
import task_21_22 as t21_22


def main():
    print('1 - task 1-5')
    print('2 - task 6-10')
    print('3 - task 11-15')
    print('4 - task 16-20')
    print('5 - task 21-22')
    print('0 - exit')
    while True:
        try:
            answer = int(input('> '))
            if answer == 1:
                t1_5.main_for_task()
            if answer == 2:
                t6_10.main_for_task()
            if answer == 3:
                t11_15.main_for_task()
            if answer == 4:
                t16_20.main_for_task()
            if answer == 5:
                t21_22.main_for_task()
            if answer == 0:
                print('exit')
                break
        except Exception as exp:
            print(exp)


if __name__ == '__main__':
    main()
