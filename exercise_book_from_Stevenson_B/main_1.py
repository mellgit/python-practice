"""

"""
import math

def main():
    
    # ex_3()
    # ex_5()
    # ex_6()
    # ex_9()
    ex_10()

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


# moscow 55.7558° N, 37.6173° E
# podolsk 55.42474549506035, 37.550110684896815
def ex_10():

    t1 = 55.7558
    g1 = 37.6173

    t2 = 55.4247
    g2 = 37.5501
    distance = 6371.01 * math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
    print(f"{round(distance/100*1.61, 2)} km")
    



if __name__=='__main__':
    main()