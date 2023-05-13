from movies_to_watch import movies_to_watch
from scrapping import buzzoid_scrap
from bs4 import BeautifulSoup
import requests


def main():
    response = requests.get('https://news.ycombinator.com/news')

    yc_web_page = response.text

    soup = BeautifulSoup(yc_web_page, "html.parser")

    articles_texts = []
    articles_links = []

    tags_title = soup.find_all(class_="titleline")
    for tag in tags_title:
            a_tag = tag.find("a")
            articles_texts.append(a_tag.getText())
            articles_links.append(a_tag.get("href"))

    articles_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

    while articles_upvote:
        larger_number = max(articles_upvote)
        larger_number_index = articles_upvote.index(larger_number)
        print(articles_texts[larger_number_index],
              articles_links[larger_number_index],
              articles_upvote.pop(larger_number_index))


if __name__ == '__main__':
    print(buzzoid_scrap())
    print(movies_to_watch())
    main()

