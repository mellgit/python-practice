import math
import rsa

def main():
    
    n = 0
    d = 1
    # список для записи значения f, тк в дальнейшем его необходимо изменять
    euler_function = []

    russian_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                        'т',
                        'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', '0', '1', '2', '3', '4', '5',
                        '6', '7', '8', '9', ',', '.', '?', '!', ' ']  # русский алфавит
    list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                      101]  # список простых чисел
    list_of_e = []  # список для допустимых значение первого значения (е) открытого ключа
    list_of_e_and_n = []  # список из двух элементов е и n (открытый ключ)
    list_of_d_and_n = []  # список из двух элементов d и n (закрытый ключ)
    list_of_numbers_alphabet = []  # список индексов введеного сообщения
    list_of_encrypted_numbers = []  # зашифрованный список чисел
    list_of_decrypted_numbers = []  # расшифрованный список чисел
    decrypted_message_list = []  # список для перевода из чисел в буквы русского алфавита

    while True:
        try:
            choice = int(input("выбери один из двух способов шифрования(input 1(bit) or 2(private key)):>"))
            if choice == 1:
                bitwise_encryption()
            elif choice == 2:
                simple_key_generation(list_of_primes, list_of_e, n, list_of_e_and_n, euler_function)  # генерация открытого ключа
                private_key_generation(list_of_e_and_n, list_of_d_and_n, euler_function, d)  # генерация закрытого ключа
                encryption_function(russian_alphabet, list_of_e_and_n, list_of_numbers_alphabet,
                list_of_encrypted_numbers)  # шифрование сообщения
                decryption_function(russian_alphabet, list_of_encrypted_numbers, list_of_d_and_n, list_of_decrypted_numbers,
                decrypted_message_list)  # расшифрование сообщения
            else:
                continue
        except Exception as e3:
            print(f'неверный фромат числа - {e3}')
        break


def bitwise_encryption():
    
    (pubkey, privkey) = rsa.newkeys(512)

    message = input("enter message in english>").encode() # ввод только на английском

    # шифруем
    crypto = rsa.encrypt(bytes(message), pubkey)
    print(crypto)

    # расшифровываем
    message = rsa.decrypt(crypto, privkey)
    print(message)


def simple_key_generation(list_of_primes, list_of_e, n, list_of_e_and_n, euler_function):  # создание открытого ключа
    i = 1
    while True:
        try:
            print(*list_of_primes)  # список простых чисел
            print('выбери два простых числа')
            p = int(input('p = '))  # необходимые параметры p и q
            q = int(input('q = '))

            if p not in list_of_primes or q not in list_of_primes:
                i += 1
                raise Exception()
            else:
                n = p * q  # необходимый расчет значения n
                print(f"n = {n}")
                euler_function_var = (p - 1) * (q - 1)  # рассчет ф-ии Эйлера
                euler_function.append(euler_function_var)  # запись значения f
                print(f"f = {euler_function[0]}")
                print('неоходимо выбрать e, оно должно быть простым и < f')
                # цикл необходим для расчета диапозона допустимых значений e
                for i in range(len(list_of_primes)):
                    # обязательное усл-е, тк простое число не должно быть меньше f
                    if list_of_primes[i] < euler_function[0]:
                        e = euler_function[0] % list_of_primes[i]  # так же число должно быть взаимо простым с f
                        if e != 0:
                            list_of_e.append(list_of_primes[i])  # создание списка из допустимых значений простых чисел

                print(*list_of_e)  # здесь записаны допустимые значения e

                j = 1
                while True:
                    try:
                        var_for_enter_value_e = int(input())
                        if var_for_enter_value_e not in list_of_e:
                            j+=1
                            raise Exception()
                        else:
                            # запись допустимого значения e из списка list_of_e
                            list_of_e_and_n.append(var_for_enter_value_e)
                            list_of_e_and_n.append(n)  # запись значения n
                            print('{e,n} = ', *list_of_e_and_n)
                            break
                    except Exception as e2:
                        print(f'неверный фромат числа - {e2}')
                break
        except Exception as e:
            print(f'неверный фромат числа - {e}')


# создание закрытого ключа
def private_key_generation(list_of_e_and_n, list_of_d_and_n, euler_function, d):
    i = 1
    while True:
        # данный цикл методом подбора находит значение d
        formula_for_d = (d * list_of_e_and_n[0])
        # если деление по модулю равно 1 и d больше значения e
        if formula_for_d % euler_function[0] == 1 and d > list_of_e_and_n[0]:
            list_of_d_and_n.append(d)  # то добавляем его в наш список list_of_d_and_n и выходим
            break
        else:
            d += 1  # иначе цикл продолжает подбирать числа
            i += 1  # увеличивая число итераций и значение d
    list_of_d_and_n.append(list_of_e_and_n[1])  # после нахождения d, добавляем в этот список значения n
    print('{d,n} = ', *list_of_d_and_n)


def encryption_function(russian_alphabet, list_of_e_and_n, list_of_numbers_alphabet,
                        list_of_encrypted_numbers):  # ф-я шифрования
    print('введите сообщение: ', end='')
    input_str = input()  # сообщение для шифрования

    for i in range(len(input_str)):  # цикл для определения индекса буквы в алфавите
        for j in range(len(russian_alphabet)):
            if input_str[i] == russian_alphabet[j]:
                print((*russian_alphabet[j], j + 1))
                list_of_numbers_alphabet.append(j + 1)  # запись самих индексов в новый список
    print('list_of_numbers_alphabet\t', *list_of_numbers_alphabet)

    for i in range(len(list_of_numbers_alphabet)):  # алгоритм шифрования
        var_for_pow = pow(list_of_numbers_alphabet[i], list_of_e_and_n[0])
        var_for_model = var_for_pow % list_of_e_and_n[1]
        list_of_encrypted_numbers.append(var_for_model)
    print('list_of_encrypted_numbers\t', *list_of_encrypted_numbers)  # запись зашифрованных чисел в новый список


def decryption_function(russian_alphabet, list_of_encrypted_numbers, list_of_d_and_n, list_of_decrypted_numbers,
                        decrypted_message_list):  # ф-я расшифровки
    for i in range(len(list_of_encrypted_numbers)):  # цикл для расшифрования списка чисел
        var_for_pow = pow(list_of_encrypted_numbers[i], list_of_d_and_n[0])
        var_for_model = var_for_pow % list_of_d_and_n[1]
        list_of_decrypted_numbers.append(var_for_model)  # список содержащий индексы букв в алфавите
    print('list_of_decrypted_numbers\t', *list_of_decrypted_numbers)

    for i in range(len(list_of_decrypted_numbers)):  # преобразование из индексов в буквенные значения
        decrypted_message_list.append(russian_alphabet[list_of_decrypted_numbers[i] - 1])
    print('decrypted_message_list\t', *decrypted_message_list, sep='')


main()

