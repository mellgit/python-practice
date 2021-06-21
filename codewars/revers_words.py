# Завершите решение, чтобы оно перевернуло все слова в переданной строке.


def main():
    print(reverse_words('so good'))

def reverse_words(s):
    ln = s.split()
    return ' '.join(ln[::-1])

if __name__=='__main__':
    main()