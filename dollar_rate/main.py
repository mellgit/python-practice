import requests
from bs4 import BeautifulSoup
import time
import msvcrt, sys

URL_DOLLAR = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&aqs=chrome..69i57j0l6j69i60.2040j0j4&sourceid=chrome&ie=UTF-8'
URL_EURO = 'https://www.google.com/search?ei=reH0X_zuKq2urgSylrDgCA&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80&gs_lcp=CgZwc3ktYWIQARgAMgoIABDJAxBGEIICMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgQIABBHOgUIABDJA1CEjJ8BWMKQnwFgvp6fAWgAcAJ4AIABQIgBuQGSAQEzmAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab'

# headers - чтобы браузер не подумал, что это бот
# загугли "my user agent" и вставь в значение ключа User-Agent
headers = {'User-Agent': ''}

# завершение программы клавишой "esc"
print("ending the program with the 'esc' key")

def dollar():
    full_page = requests.get(URL_DOLLAR, headers=headers) # содержиться вся html разметка

    # указываем через что будет парситься данная разметка bs4
    soup = BeautifulSoup(full_page.content, 'html.parser')

    # поиск по тегам
    convert = soup.findAll("span", {"class":"DFlfde SwHCTb", "data-precision":2})
    print(f"1$ = {convert[0].text}₽")


def euro():
    full_page = requests.get(URL_EURO, headers=headers) # содержиться вся html разметка

    # указываем через что будет парситься данная разметка bs4
    soup = BeautifulSoup(full_page.content, 'html.parser')

    # поиск по тегам
    convert = soup.findAll("span", {"class":"DFlfde SwHCTb", "data-precision":2})
    print(f"1€ = {convert[0].text}₽")


while True:
    dollar()
    euro()
    time.sleep(3)

    if msvcrt.kbhit(): # если нажата клавища
        k = ord(msvcrt.getch()) # считываем код клавиши
        if k == 27: # если клавиша Esc
            sys.exit() # завершаем программу



