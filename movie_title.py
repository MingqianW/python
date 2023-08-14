import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36 Edg/115.0.1901.200"
           }
with open("./movie_titles.txt", "w", encoding="utf-8") as file:
    for start_num in range(0,250,25):
        response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers = headers)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        titles = soup.findAll("span", attrs={"class" : "title"})
        for title in titles:
                print(title.string)
                file.write(title.string.replace(u'\xa0','') + "\n")
