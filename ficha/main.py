"""
here are some python language features
"""
import pretty_errors # для красивый ошибок
import string

def main():
    sort_array()
    const_string()

def sort_array():
    arr = [4,2,0,1,5,3,6]

    print('\n***sort_array***'.upper())
    print(f"sorted(arr) =   {sorted(arr)}")
    print(f"arr =           {arr}")

    print(f"arr.sort() =    {arr.sort()}")
    print(f"arr =           {arr}")
    

def const_string():
    print('\n***const_string***'.upper())
    print(string.ascii_letters)
    print(string.punctuation)
    print(string.digits)
    print(string.whitespace)


if __name__ == "__main__":
    main()
