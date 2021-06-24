"""
Завершите функцию, чтобы она принимала 
массив ключей и значение по умолчанию и 
возвращала словарь (Python) со всеми ключами, 
установленными в значение по умолчанию.
ex:
["draft", "completed"], 0   # should return {"draft": 0, "completed: 0}
"""

def main():
    print(populate_dict(["draft", "completed", "complet"], 4))


def populate_dict(keys, default):
    ln = dict.fromkeys(keys)
    for i in range(len(ln)):
        ln[keys[i]] = default
    return ln
    # return {k: default for k in keys}

if __name__=="__main__":
    main()
