"""
Задача
Ваша задача - вернуть число из строки.

Подробности
Вам будет предоставлена ​​строка из смешанных цифр и букв, вы должны вернуть все числа в этой строке в том порядке, в котором они встречаются.
"""
import string
def main():
    my_string = "aa1bb2cc3dd"
    # my_string = "123"
    print(filter_string(my_string))

def filter_string(my_string):
    #your code here
    # ln = str(string.digits)
    
    # for i in my_string:
    #     if i in string.digits:
    #         print(i)
    return int(''.join([i for i in my_string if i in string.digits]))
    # return type(ln)
    # return string.digits

    # return type(my_string[0])



if __name__ == "__main__":
    main()