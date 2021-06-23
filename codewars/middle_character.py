"""
Вам дадут слово. Ваша задача - вернуть средний символ слова. 
Если длина слова нечетная, вернуть средний символ. 
Если длина слова четная, вернуть 2 средних символа.
"""
from typing import SupportsAbs


def main():
    print(get_middle("testing"))
    print(get_middle("test"))


def get_middle(s):
    if len(s) % 2 == 1:
        return f"{s[int(((len(s)+1)/2)-1)]}"
    else:
        return f"{s[int((len(s)/2)-1)]}{s[int((len(s)/2)-1)+1]}"


if __name__ == "__main__":
    main()
