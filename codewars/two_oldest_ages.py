"""Необходимо выполнить функцию / метод двух самых старых возрастов. 
Он должен принимать в качестве аргумента массив чисел и возвращать 
два самых высоких числа в массиве . Возвращаемое значение должно 
быть массивом в формате [второй самый старый возраст, самый старый возраст] .

Порядок переданных чисел может быть любым. В массиве всегда будет 
как минимум 2 элемента. Если есть два или более самых старых возраста, 
верните их оба в формате массива."""

def main():
    print(two_oldest_ages([1, 3, 10, 0]))

def two_oldest_ages(ages):
    temp_max = max(ages)
    ages.remove(max(ages))
    temp_min = max(ages)
    return [temp_min, temp_max]
    # return sorted(ages)[-2:]
    

if __name__=="__main__":
    main()