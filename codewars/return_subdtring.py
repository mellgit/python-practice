"""
Завершите решение, чтобы оно возвращало, 
сколько раз search_text был найден в full_text.
ex:
solution('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up twice
"""
def main():
    print(solution('aa_bb_cc_dd_bb_e', 'bb'))

def solution(full_text, search_text):
    ln = full_text.replace(search_text, '*')
    return len([i for i in range(len(ln)) if ln[i] == '*'])
    # return full_text.count(search_text)

if __name__== "__main__":
    main()
