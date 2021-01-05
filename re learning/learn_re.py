# https://tproger.ru/translations/regular-expression-python/


import re




def simple():

    # для определения есть ли в начале строки данная строка 'AV'
    # Мы используем «r» перед строкой шаблона, чтобы показать, что это «сырая» строка в Python
    res = re.match(r'AV', 'AV daniilhorn@gmail.com')
    print(res.group(0))

    print()
    #  методы start() и end() для того, чтобы узнать начальную и конечную позицию найденной строки
    res = re.match(r'AV', 'AV daniilhorn@gmail.com')
    print(res.start())
    print(res.end())

    print()
    # Метод search() ищет по всей строке, но возвращает только первое найденное совпадение
    res = re.search(r'@gmail', 'AV daniilhorn@gmail.com AV')
    print(res.group(0))

    print()
    # Этот метод возвращает список всех найденных совпадений.
    res = re.findall(r'AV', 'AV daniilhorn@gmail.com AV AV')
    print(res)

    print()
    # Этот метод разделяет строку по заданному шаблону
    res = re.split(r'a', 'AV daniilhorn@gmail.com AV AV')
    print(res)


    """
    Метод split() принимает также аргумент maxsplit со значением по умолчанию, 
    равным 0. В данном случае он разделит строку столько раз, сколько возможно, 
    но если указать этот аргумент, то разделение будет произведено не более 
    указанного количества раз
    """
    print()
    res = re.split(r'a', 'AV daniilhorn@gmail.com AV AV', maxsplit=1)
    print(res)

    print()
    # Этот метод ищет шаблон в строке и заменяет его на указанную подстроку. 
    # Если шаблон не найден, строка остается неизменной
    res = re.sub(r'a', '_', 'AV daniilhorn@gmail.com AV AV')
    print(res)


    """
    Мы можем собрать регулярное выражение в отдельный объект, 
    который может быть использован для поиска. Это также избавляет 
    от переписывания одного и того же выражения

    чтобы не писать лищний раз параметр
    """
    print()
    pattern = re.compile('AV')
    result = pattern.findall('AV Analytics Vidhya AV')
    print(result)
    result2 = pattern.findall('AV is largest analytics community of India')
    print(result2)


"""

Оператор	Описание
.	        Один любой символ, кроме новой строки \n.
?	        0 или 1 вхождение шаблона слева
+	        1 и более вхождений шаблона слева
*	        0 и более вхождений шаблона слева
\w	        Любая цифра или буква (\W — все, кроме буквы или цифры)
\d	        Любая цифра [0-9] (\D — все, кроме цифры)
\s	        Любой пробельный символ (\S — любой непробельный символ)
\b	        Граница слова
[..]	    Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
\	        Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
^ и $	    Начало и конец строки соответственно
{n,m}	    От n до m вхождений ({,m} — от 0 до m)
a|b	        Соответствует a или b
()	        Группирует выражение и возвращает найденный текст
\t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно
"""
def hard():
    my_str = "1. Hello world"

    # выводит список каждого символа, кроме новой строки
    res = re.findall(r'.', my_str)
    print(res)

    # выводит список каждого символа, только цифры и буквы
    res = re.findall(r'\w', my_str)
    print(res)


    # выводит список каждого символа, только цифры и слова и пробелы
    res = re.findall(r'\w*', my_str)
    print(res)


    # выводит список каждого символа, только цифры и слова, без пробелов и символов
    res = re.findall(r'\w+', my_str)
    print(res)


    # выводит первое слово
    res = re.findall(r'^\w+', my_str)
    print(res)


    # выводит последнее слово
    res = re.findall(r'\w+$', my_str)
    print(res)


def me():
    my_str = "1. Hello world\n2. Hello world\n"
    res = re.sub(r'^\d+', '', my_str)
    # res = re.findall(r'^\w+', my_str)
    print(res)



    """
    # Этот метод ищет шаблон в строке и заменяет его на указанную подстроку. 
    # Если шаблон не найден, строка остается неизменной
    res = re.sub(r'a', '_', 'AV daniilhorn@gmail.com AV AV')
    print(res)

    """
def main():
    # simple()
    # hard()
    me()

if __name__ == "__main__":
    main()