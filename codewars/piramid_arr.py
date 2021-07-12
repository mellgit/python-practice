"""
Напишите функцию, которая при заданном числе> = 0 возвращает массив подмассивов возрастающей длины.

pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
Примечание: подмассивы должны быть заполнены 1s
"""

def main():
    
    print(pyramid(3))

def pyramid(n):
    a = []
    for i in range(n):
        a.append([int(1) for j in range(n)])
        n-=1
    return list(reversed(a))


if __name__== "__main__":
    main()