"""
Учитывая целое число, определите, квадратное ли это число :
"""

def main():
    print(is_square(64))


def is_square(n):
    
    return True if pow(n,1/2)//2==1 or 0 else False
    # return pow(n, 1/2)%2

if __name__=="__main__":
    main()
