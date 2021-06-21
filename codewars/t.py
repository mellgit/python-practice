def solution(value):
    # value_str = str(value)
    # val_str = len(value_str)
    # ln = 5 - val_str
    # out_str = ''
    # for i in range(ln):
    #     out_str+="0"
    # return out_str+value_str

    
    out_str = ''
    for i in range(5 - len(str(value))):
        out_str+="0"
    return f"Value is {out_str+str(value)}"

print(solution(000))