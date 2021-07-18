from GoogleNews import GoogleNews


google_news = GoogleNews(period='5d', lang='ru')
google_news.search('russia')
result = google_news.result()

for i in result:
    print(f"Title:        {i['title']}")
    print(f"Date/Time:    {i['date']}")
    print(f"Description:  {i['desc']}")
    print(f"Link:         {i['link']}")
    print('#'*20)
