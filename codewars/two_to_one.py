"""
Возьмите 2 строки s1и в s2том числе только буквы от aдо z. 
Вернуть новую отсортированную строку, как можно более длинную, 
содержащую отдельные буквы - каждая взятая только один раз - исходящая из s1 или s2.
ex:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

def main():
    print(longest("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"))

def longest(a1, a2):
    #v3
    # plus = a1+a2
    return ''.join(sorted(set(a1+a2)))

    # v1
    # return sorted(list(set([a1[i] for i in range(len(a1))])))

    #v2
    # ln = [a1[i] for i in range(len(a1))]
    # lb = []
    # for i in range(len(a1)):
    #     # ln = a1[i].split()
    #     lb.append(a1[i])
    # return sorted(list(set(lb)))

main()