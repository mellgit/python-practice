"""
Завершите решение. Он должен попытаться получить 
значение массива по указанному индексу. 
Если индекс выходит за максимальные границы массива, 
вместо этого он должен возвращать значение по умолчанию.
"""

def main():
    data = ['a', 'b', 'c']
    print(solution(data, -3, 'd'))


def solution(items, index, default_value):
    return default_value if index > (len(items)-1) or index < -(len(items)) else items[index]
    
    # value = (len(items)-1)
    # return default_value if index > value or index < value else items[index]


    # if index > (len(items)-1) or index < -(len(items)-1):
    #     return default_value
    # else: 
    #     return items[index]
    

if __name__=="__main__":
    main()
