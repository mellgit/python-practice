import random
import sys


arg = sys.argv[1:] # первый эл-т списка sys.argv имя файла, необходимы последующие
open('pass_text.txt', 'w').close() # очистка файла

pas_list = [] # список для одного пароля
more_pas_list = [] # список для нескольких паролей

# набор необходимых символов 
sim_num_chr_str = "KP*Y@14I9qv$UEa3(AoNOFd0wMys#c@rV8m2ikxC6W5)p&BujGTQSX*Ln7l4_gDtfH1&$ZhbR_eJ"

# перемешка изначального набора 
sum_list = list(sim_num_chr_str) 
random.shuffle(sum_list) 
result_rand_str = ''.join(sum_list) 

def generator(value_end_arg):

    for j in range(value_end_arg): # геерация нескольких паролей
        for _ in range(34): # генерация одного пароля
            pas_list.append(random.choice(result_rand_str))

        more_pas_list.append(''.join(pas_list[-1:-35:-1])) # выбор последних 34 символов из строки
        print(f"{j+1} - " + ''.join(more_pas_list[j]))

        with open("pass_text.txt", "a") as hello_file: # запись в файл для удобства
            print(f"{j+1} - " + ''.join(more_pas_list[j]), file=hello_file)
    
# проверка, если user не установит значение паролей
if len(arg) < 1:
    generator(10)
else:
    value_end_arg = int(arg[0]) 
    generator(value_end_arg)



