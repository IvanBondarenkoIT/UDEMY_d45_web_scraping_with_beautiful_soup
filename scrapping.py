from bs4 import BeautifulSoup
import requests

PREFIX_ACTIVE = "Active "
QTY_COMMON_USERS_GROUPS = 8


def buzzoid_scrap():
    response = requests.get('https://buzzoid.com/buy-instagram-followers/')

    web_page = response.text

    soup = BeautifulSoup(web_page, "html.parser")

    articles_dollars = []
    articles_cents = []

    tags_title = soup.find_all(class_="fragment__price")
    for tag in tags_title:
            p_tag = tag.find("p")
            articles_dollars.append(p_tag.find('strong').getText())
            articles_cents.append(p_tag.find_all('span')[1].getText())

    articles_followers = [followers.find("strong").getText() for followers in soup.find_all(name="div", class_="fragment__head")]

    result = {}
    prem = ""
    for ind in range(len(articles_followers)):
        if ind >= QTY_COMMON_USERS_GROUPS:
            prem = PREFIX_ACTIVE
        result[f'{prem}{articles_followers[ind]}'] = f'{articles_dollars[ind]}.{articles_cents[ind]}'

    return result




