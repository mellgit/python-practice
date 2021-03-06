"""
Напишите функцию, persistence, которая принимает положительный параметр 
num и возвращает его мультипликативную постоянство, то есть количество раз, 
которое вы должны умножить цифры, numпока не дойдете до единственной цифры.
ex:
 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit
                  
 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number
"""

# import numpy as np
# l = [1,2,3,4,5]
# print(np.prod(l))

import numpy as np
def main():
    print(persistence(999))



def persistence(n):
    #v7
    snum = str(n)
    if len(snum) == 1:
        return 0
    list_num = [int(elem) for elem in snum]
    ln = np.prod(list_num)
    counter = 1
    while ln >= 10:
        list_num = [int(elem) for elem in list(str(ln))]
        ln = int(np.prod(list_num))
        counter+=1
    return counter
    
    
    #v6
    # num = str(n)
    
    # if len(num)==1:
    #     return 0

    # else:
    #     global counter
    #     counter+=1
    #     ln = []
    #     for i in range(len(num)):
    #         ln.append(int(num[i]))
        
    #     return persistence(int(np.prod(ln))) if int(np.prod(ln)) >= 10 else counter
        
    

# def test(test_n):
#     num = str(test_n)
#     ln = []
#     for i in range(len(num)):
#         ln.append(int(num[i]))
#     # lb = int(np.prod(ln))
#     return test(int(np.prod(ln)))
    
    # if len(num) == 1:
    #     # if int(num) == n:
    #     #     return 0
    #     # else:
    #     #   return int(num)  
    #     # if len(num) == 1 and num.isdigit() and num > '0':
    #     #     return 0
    #     # else:
    #     #     return int(num)
    #     return int(num)
    # else:
    #     ln = []
    #     for i in range(len(num)):
    #         ln.append(int(num[i]))
    #     return persistence(int(np.prod(ln)))

    #v5
    # num = str(n)
    
    # if len(num) == 1:
    #     # if int(num) == n:
    #     #     return 0
    #     # else:
    #     #   return int(num)  
    #     # if len(num) == 1 and num.isdigit() and num > '0':
    #     #     return 0
    #     # else:
    #     #     return int(num)
    #     return int(num)
    # else:
    #     ln = []
    #     for i in range(len(num)):
    #         ln.append(int(num[i]))
    #     return persistence(int(np.prod(ln)))
    
    #v4
    # num = str(n)
    # ln = []
    # for i in range(len(num)):
    #     ln.append(int(num[i]))
    # return persistence(int(np.prod(ln))

    #v3
    # num = str(n)
    # ln = []
    # j = 1
    # while j >= len(num):
    #     for i in range(len(num)):
    #         ln.append(int(num[i]))
    #     num = np.prod(ln)
    #     j+=1
    # return  num


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