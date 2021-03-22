import lin_algoritm as mod_la
import ramification as ram
import loop 
import lists_and_tuples as lp
import my_str as ms


def main():
    print('1 - lin_algoritm')
    print('2 - ramification')
    print('3 - loop')
    print('4 - lists_and_tuples')
    print('5 - my_str')
    print('0 - exit')
    try:
        while True:
            answer = int(input("> "))
            if answer == 1:
                mod_la.main_for_task()
            elif answer == 2:
                ram.main_for_task()
            elif answer == 3:
                loop.main_for_task()
            elif answer == 4:
                lp.main_for_task()
            elif answer == 5:
                ms.main_for_task()
            elif answer == 0:
                print('exit')
                break
    except Exception as exp:
        print(exp)


if __name__ == "__main__":
    main()
