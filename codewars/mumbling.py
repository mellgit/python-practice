"""
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""

def main():
    print(accum("RqaEzty"))


def accum(s):
    # ln = [str(s[i]*(i+1)).title() for i in range(len(list(s.lower())))]
    return '-'.join([str(s[i]*(i+1)).title() for i in range(len(list(s.lower())))])

if __name__=="__main__":
    main()
