"""

Написать функцию, которая получает список байтовых строк(32-битные) и 
интерпретирует их как целые числа, возвращая их как итерацию по 
содержащимся целым числам.

ex:
input:  ["\0\0\0\0\0\0\0\1\0\0\0\2", "\0\0\1\1"]
output: [        0,      1,      2,        257 ]
Примечание. Входящую итеративную последовательность 
следует рассматривать как непрерывный поток данных, 
и ее соответствие не гарантируется до 32 бит для каждого пакета.
"""


def main():
    stream = ["\0\0\0\0\0\0\0\1\0\0\0\2", "\0\0\1\1"]
    
    print(convert(256))
    x = str(convert(256))
    print(int(x, base=2))

def interpret_as_int32(stream):
    pass

def convert(i):
    return int(bin(i+2**32)[-32:])


if __name__ == "__main__":
    main()
