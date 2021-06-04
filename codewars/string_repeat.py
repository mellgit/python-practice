def main():
    print(count_bits(1234))

def count_bits(n):
    n = str(bin(n))
    s = n[2:]
    count = 0
    ln = [count + 1 for i in range(len(s)) if s[i] =='1']
    return len(ln)


main()
