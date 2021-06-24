"""
Если задано число n , вернуть 
количество положительных нечетных чисел меньше n
error:
ошибка во таймауту, не проходит проверку
"""

import time

def main():

    print(odd_count(15023))
    # odd_count(7)

def odd_count(n):
    
    # v1
    counter = 0
    for i in range(n):
        if i%2!=0:
            counter+=1
    return counter
    
    # v2
    # return len([i for i in range(n) if i % 2 != 0])

    #v3


if __name__=="__main__":
    start = time.time()
    main()
    print(f"{time.time()-start}")
