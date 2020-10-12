# Тестирование подсчета количества слова, абзацев, знаков, строк в txt документе

import csv


def main():
    filename = ["test1.txt", "test2.txt", "test3.txt", "test4.txt", "test5.txt"]
    filename_csv = ["necessary_result.csv", "program_result.csv"]
    list_for_csv = []  # список для записи в program_result.csv
    for i in range(len(filename)):
        try:
            print(f"{i + 1}-й файл")
            word = word_count(filename[i])
            number_p = number_of_paragraphs(filename[i])
            number_s = number_of_symbol(filename[i])
            number_l = number_of_lines(filename[i])
            list_for_csv.append([word, number_p, number_s, number_l])
            print(f" {word}\n {number_p}\n {number_s}\n {number_l}")
            record_of_results(filename_csv[1], list_for_csv)

        except Exception as ex:
            print('неверный формат')
            print(ex)
    comparison_of_results(filename_csv[0], filename_csv[1])


def word_count(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()  # чтение посимвольно
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    words = text.split()
    count = len(words)
    return f"количетсво слов - {count}"


def number_of_paragraphs(filename):
    count = 0
    with open(filename, "r", encoding='utf-8') as file:
        text = file.readlines()  # чтение построчно и записывает в список

    for line in text:
        # если слева от элемента есть абзац увеличивается счетчик
        if line != line.lstrip():
            count += 1
    return f"количетсво обрацев - {count}"


def number_of_symbol(filename):
    my_lst = ['.', ',', '!', '?', '(', ')', ';', ':', '...']
    count = 0
    with open(filename, "r", encoding='utf-8') as file:
        text = file.read()
    for j in text:  # вложенный цикл для поиска знака из списка
        for item in range(len(my_lst)):
            i = j.find(my_lst[item])  # если знак есть, то вывод будет индекс элемента
            # если нет знака то значение -1
            if i > -1:
                count += 1
    return f"количетсво символов - {count}"


def number_of_lines(filename):
    with open(filename, "r", encoding='utf-8') as file:
        number_row = len(file.readlines())  # построчный подсчет
        return f"количество строк - {number_row}"


def record_of_results(filename_csv, list_for_csv):  # запись результатов
    with open(filename_csv, "w", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(list_for_csv)


def comparison_of_results(filename_csv0, filename_csv1):  # сравнение результатов
    with open(filename_csv0, "r", newline="", encoding='utf-8') as file0:
        reader0 = csv.reader(file0)

        with open(filename_csv1, "r", newline="", encoding='utf-8') as file1:
            reader1 = csv.reader(file1)
            try:
                item = 1
                for row0, row1 in zip(reader0, reader1):
                    if len(row0) != 0 and len(row1) != 0:
                        if row0 == row1:
                            print(f"{item}-й файл: тест пройден")
                        else:
                            print(f"{item}-й файл: тест не пройден")
                        item += 1
            except Exception as exp:
                print("error")


if __name__ == '__main__':
    main()
