def main():
    str_in = ''  # строка на ввод

    str_out = []  # строка на вывод

    prom_out = []

    russian_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                        'т',
                        'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', '0', '1', '2', '3', '4', '5',
                        '6', '7', '8', '9', ',', '.', '?', '!', ' ']  # русский алфавит
    english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', '$$q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z', '/', '0', '3', '|', '*', ' ', '#',
                        '}', '3', '+', '=', '<', '`', '>', '-', '_', '&', '$', '@', ')', '0', '%',
                        '!']  # английский алфавит

    encryption_fun(str_out, russian_alphabet, english_alphabet)
    decrypted_fun(str_out, prom_out, russian_alphabet, english_alphabet)


def encryption_fun(str_out, russian_alphabet, english_alphabet):
    print('создайте письмо: ', end='')
    str_in = input()
    print('длина письма ', len(str_in))

    for i in range(len(str_in)):
        for j in range(len(russian_alphabet)):

            if russian_alphabet[j] == str_in[i]:
                str_out.append(english_alphabet[j])
    print(*str_out, sep='')


def decrypted_fun(str_out, prom_out, russian_alphabet, english_alphabet):
    for i in range(len(str_out)):
        for j in range(len(english_alphabet)):
            if english_alphabet[j] == str_out[i]:
                prom_out.append(russian_alphabet[j])
    print('длина письма ', len(prom_out))
    print(*prom_out, sep='')


main()

# prom_out = []
#
# russian_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
#                     'т',
#                     'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', '0', '1', '2', '3', '4', '5',
#                     '6', '7', '8', '9', ',', '.', '?', '!', ' ']  # русский алфавит
# english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', '$$q', 'r', 's',
#                     't', 'u', 'v', 'w', 'x', 'y', 'z', '/', '0', '3', '|', '*', ' ', '#',
#                     '}', '3', '+', '=', '<', '`', '>', '-', '_', '&', '$', '@', ')', '0', '%',
#                     '!']  # английский алфавит
# str_out = '$$qrjcft$%ytp%opcpdp%sfdpeo#%rasslahfz|)'


def decrypted_fun1(str_out, prom_out, russian_alphabet, english_alphabet):
    for i in range(len(str_out)):
        for j in range(len(english_alphabet)):

            if english_alphabet[j] == str_out[i]:
                prom_out.append(russian_alphabet[j])

    print('длина письма ', len(prom_out))
    print(*prom_out, sep='')


# decrypted_fun1(str_out, prom_out, russian_alphabet, english_alphabet)
