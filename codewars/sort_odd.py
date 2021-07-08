"""
Задача
Вам будет предоставлен массив чисел. Вы должны 
отсортировать нечетные числа в порядке возрастания, 
оставив четные числа на своих исходных позициях.

Примеры
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""

def main():
    
    print(sort_array([3, 8, 6, 5, 4]))

def sort_array(source_array):
    # Return a sorted array.
    #v2
    # ln = [source_array.index(i) for i in source_array if source_array[i]%2!=0]
    # lm = [i for i in source_array if source_array[i]%2!=0]

    # source_array = [source_array.remove(i) for i in lm]
    # return source_array

    #v1
    # списки индексов и значений
    ln = [] # index
    lm = [] # value
    for i in range(len(source_array)):
        if source_array[i]%2!=0:
            ln.append(source_array.index(source_array[i]))
            lm.append(source_array[i])
    
    # удаление нечетных чисел из основного массива
    for i in range(len(lm)):
        source_array.remove(lm[i])

    # добовление элементов по индексу
    
    for i in range(len(sorted(lm))):
        source_array.insert(ln[i], sorted(lm)[i])
        
    return source_array
    # return sorted([i for i in source_array if i%2!=0])

main()