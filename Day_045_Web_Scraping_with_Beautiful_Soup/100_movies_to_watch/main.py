import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

web_soup = BeautifulSoup(response.text, "html.parser")
titles_span = web_soup.find_all(name="h3", class_="title")
titles_list = [item.getText() for item in titles_span]
titles_list.reverse()
# for movie in titles_list:
    # print(movie)

with open("movies.txt", mode="w", encoding="utf8") as file:
    for movie in titles_list:
        file.write(f"{movie}\n")


