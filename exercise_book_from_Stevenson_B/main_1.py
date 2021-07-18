"""

"""

def main():
    
    # ex_3()
    # ex_5()
    # ex_6()
    ex_9()

def ex_3():
    w = float(input('w(m) = '))
    h = float(input('h(m) = '))
    print(f"s = {w*h}")

def ex_5():
    b_litre = float(input('> litre = '))
    m_litre = float(input('<= litre = '))
    print(f"${b_litre*0.25+m_litre*0.1}")
    
def ex_6():
    s = float(input('sum($) = '))
    print(f'percent = {s*18/100} \ntax = {s*20/100} \nsum = {s+s*18/100+s*20/100}')
    
def ex_9():
    first_installment = float(input('first installment = '))
    for i in range(3):
        first_installment+=first_installment*4/100
        print(round(first_installment, 2))

if __name__=='__main__':
    main()