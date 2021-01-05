import requests
from bs4 import BeautifulSoup
import time
import msvcrt, sys

URL = 'https://www.google.com/search?ei=3-v0X9qlHI71qwHf35G4Dw&q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&oq=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+&gs_lcp=CgZwc3ktYWIQAxgAMgUIABDJAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoECAAQRzoICC4QxwEQowI6AgguOg4ILhDHARCjAhDJAxCTAjoFCAAQkgM6CggAEMkDEEYQgAJQgMxTWJnjU2DV9FNoAHACeACAAXKIAYoEkgEDNi4xmAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab'


# headers - чтобы браузер не подумал, что это бот
# загугли "my user agent" и вставь в значение ключа User-Agent
headers = {'User-Agent': ''}

# завершение программы клавишой "esc"
print("ending the program with the 'esc' key")

def weather_forecast():
    full_page = requests.get(URL, headers=headers) # содержиться вся html разметка

    # указываем через что будет парситься данная разметка bs4
    soup = BeautifulSoup(full_page.content, 'html.parser')

    # поиск по тегам
    convert = soup.findAll("span", {"class":"wob_t TVtOme", "id":"wob_tm"})
    print(f"{convert[0].text}")


while True:
    weather_forecast()
    
    time.sleep(3)

    if msvcrt.kbhit(): # если нажата клавища
        k = ord(msvcrt.getch()) # считываем код клавиши
        if k == 27: # если клавиша Esc
            sys.exit() # завершаем программу



