# remove exclamation marks

def main():
    remove_exclamation_marks('')

def remove_exclamation_marks(s):
    ln = [s[i] for i in range(len(s)) if s[i] != '!']
    ln1 = ''.join(ln)
    return ln1
    
main() 