import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


def movies_to_watch():
    response = requests.get(URL)
    web_page = response.text
    soup = BeautifulSoup(web_page, "html.parser")
    movies = soup.find_all('div', class_="article-title-description__text")
    result = [f'{movie.find("h3", class_="title").getText()}\n' for movie in movies]
    result.reverse()
    return "".join(result)
