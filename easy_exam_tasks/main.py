import csv
import collections as c
import re

def main():
    
    # izi_task_1_10()
    # task_11()
    # task_12() # ready

    # red = [4, 5, 5, 4, 5, 5, 4]
    # red = [4, 5, 5, 4, 5, 5, 4, 4]
    red = [4, 5, 5, 4, 5, 5, 4, 4, 3]
    t13 = task_13(red) # ready
    print(t13)


# work with csv file
def task_11():

    # with open("ice_cream.csv", newline='', encoding='utf-8') as csv_file:
    #     reader = csv.DictReader(csv_file, delimiter=';')
        

    with open("ice_cream.csv", encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')

        counter = c.Counter()
        for row in csvreader:
            if row[2]:  # skip empty
                counter[row[2]] += 1
                

    print(counter.most_common(1))
    


    # strawberry_count = 0
    # mango_count = 0
    # apple_count = 0



    # with open("ice_cream.csv", newline='', encoding='utf-8') as csv_file:
    #     reader = csv.DictReader(csv_file, delimiter=';')
        
    #     for row in reader:
    #         print(row['ice_1'], row['ice_2'], row['ice_3'])


        #     if "клубника" in row['ice_1'] or row['ice_2'] or row['ice_3']:
        #         strawberry_count += 1
        # print(strawberry_count)

    # read file
    # with open("ice_cream.csv", newline='', encoding='utf-8') as csv_file:
    #     reader = csv.DictReader(csv_file, delimiter=';')
    #     for row in reader:
    #         print(row['ice_1'], row['ice_2'], row['ice_3'])
    # write file
    # with open("new_file.csv", 'w', newline='', encoding='utf-8') as csv_file:
    #     writer = csv.writer(csv_file, delimiter=';')
    #     writer.writerow(['row 1', 'row 2', 'row 3'])


def task_12():
    s = "Pearl Jam - Garden; Fools Garden - Lemon tree;".lower().split(";")
    word = "garden"
    count = 0
    print(s)
    print(word)
    for i in range(len(s)):
        if word in s[i]:
            count+=1
    print(count)

    # print(s.count(word))
    # подсчет колличества слов в строке
    # count = 0
    # flag = 0
    # count_word = 0
    # for i in range(len(s)):
    #     if s[i] != ' ' and flag == 0:


    #         count += 1
    #         flag = 1
            
    #     else:
    #         if s[i] == ' ':
    #             flag = 0
    # print(count_word)
    # подсчет каждого символа
    # results = c.Counter(trek)
    # print(results)
    # counter = 0
    # word = "garder"
    # if word in trek:
    #     print(1)
    # else:
    #     print(0)
    

def task_13(red):
    
    if 3 in red:
        return False
    elif red.count(4) > 3:
        return False
    else:
        return True
    

def izi_task_1_10():
    ##### 1
    # s1 = "4.0" # done
    # s2 = "-1" # done
    # s3 = "ABCD"
    # s4 = "12 000"
    # s5 = "12,4"

    # print(float(s5))

    ##### 2
    # number = input()
    # new_number = number * int(number) # int
    # print(type(new_number))

    ##### 3
    # while True:
    #     mark = int(input())
    #     if mark > 7:
    #         print("great")
    #     elif mark > 5:
    #         print("good")
    #     elif mark > 3:
    #         print("удов")
    #     else:
    #         print("неудов")

    ##### 4 --> 2,3
    # e = 2
    # if e >1:
    #     print("гот яиш")
    # print("кофе")

    ##### 5
    # n1 = int(input())
    # n2 = int(input())
    # while n1<=n2:
    #     if n1%2==0:
    #         print(n1**2)
    #     n1 += 1

    ##### 6
    # shop = ('milk', 'bread', 'choco')
    # shop_list = list(shop)
    # shop_list[1] = 'salat'
    # shop = tuple(shop_list)
    # print(shop[1])

    ##### 7
    # p = 'cat dog'.split()
    # p.append('parrot')
    # print(p)

    ##### 8 --> 1, 3, 4
    # w = "account"
    # print(w.rfind("ac"))
    # print(w.find("ac"))

    ##### 9 --> 0 ноль не отрицательное число
    # s = "а роза упала на лапу азора"
    # print(s[0:])

    ##### 10
    st = ['mark', 'alica', 'evgen']
    for i in range(len(st)):
        print(st[i])


if __name__ == "__main__":
    main()
