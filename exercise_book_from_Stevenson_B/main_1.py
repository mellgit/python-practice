"""

"""
import math

def main():
    
    # ex_3()
    # ex_5()
    # ex_6()
    # ex_9()
    # ex_10()
    # ex_16()
    # ex_19()
    ex_33()

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
    # moscow 
    t1 = 55.7558
    g1 = 37.6173
    # podolsk
    t2 = 55.4247
    g2 = 37.5501
    distance = 6371.01 * math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
    print(f"{round(distance/100*1.61, 2)} km")
    

def ex_16():
    radius = int(input("> "))
    print(f"area = {math.pi*radius**2}")
    print(f"volume = {4/3*(math.pi*radius**3)}")

def ex_19():
    d = int(input('> '))
    v1 = 0
    a = 9.8
    print(f"v2 = {pow(v1**2+2*a*d, 1/2)}")

def ex_33():
    val = int(input('> '))
    ln = [int(i) for i in str(val)]
    print(sum(ln))



if __name__=='__main__':
    main()