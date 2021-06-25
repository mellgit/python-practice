"""
Напишите функцию, persistenceкоторая принимает положительный параметр 
numи возвращает его мультипликативную постоянство, то есть количество раз, 
которое вы должны умножить цифры, numпока не дойдете до единственной цифры.
ex:
 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit
                  
 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number
"""


def main():
    print(persistence(999))

def persistence(n):
    #v3
    pass


    #v2
    # x = str(n)
    # if len(x) == 1 and x.isdigit() and x > '0':
    #     return n
    # else:
    #     # m = str(n)
    #     # sum = int(str(n)[0])*int(str(n)[1])
    #     return persistence(int(str(n)[0])*int(str(n)[1]))

    #v1
    # if 1<=n<=9:
    #     return n
    # else:
    #     # m = str(n)
    #     # sum = int(str(n)[0])*int(str(n)[1])
    #     return persistence(int(str(n)[0])*int(str(n)[1]))

main()