"""
Вам предоставляется массив (который будет иметь длину не менее 3, но может быть очень большим), 
содержащий целые числа. Массив либо полностью состоит из нечетных целых чисел, 
либо полностью состоит из четных целых чисел, за исключением одного целого числа N. 
Напишите метод, который принимает массив в качестве аргумента и возвращает этот «выброс» N.


"""


def main():
    print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

def find_outlier(integers):
    #v3
    count1 = 0
    count2 = 0
    for i in range(len(integers)):
        #odd
        if integers[i]%2 != 0:
            count1+=1
        #even
        else:
            count2+=1

    if count1 < count2:
        return [integers[i] for i in range(len(integers)) if integers[i]%2 != 0][0]
    else:
        return [integers[i] for i in range(len(integers)) if integers[i]%2 == 0][0]
        
        
    # return count1, count2


    #v2
    # ln = [integers[i] for i in range(len(integers)) if integers[i]%2 != 0]
    
    #v1
    # return [integers[i] for i in range(len(integers)) if integers[i]%2 != 0]

main()