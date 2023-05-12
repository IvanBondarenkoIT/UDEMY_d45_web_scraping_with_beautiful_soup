from bs4 import BeautifulSoup
import requests


def main():
    # website
    response = requests.get('https://news.ycombinator.com/news')

    yc_web_page = response.text

    soup = BeautifulSoup(yc_web_page, "html.parser")
    print(soup)

    articles_texts = []
    articles_links = []

    tags_title = soup.find_all(class_="titleline")
    for tag in tags_title:
            a_tag = tag.find("a")
            articles_texts.append(a_tag.getText())
            articles_links.append(a_tag.get("href"))

    articles_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

    print(articles_texts)
    print(articles_links)
    print(articles_upvote)

    while articles_upvote:
        larger_number = max(articles_upvote)
        larger_number_index = articles_upvote.index(larger_number)
        print(articles_texts[larger_number_index],
              articles_links[larger_number_index],
              articles_upvote.pop(larger_number_index))







    # with open('website.html', 'r') as file:
    #     content = file.read()
    #     soup = BeautifulSoup(content, 'html.parser')
    #     # print(soup.title)
    #
    #
    #     objects = soup.find(name='h1', id='name')
    #     print(objects)
    #
    #     all_tags = soup.find_all('a')
    #     for i in all_tags:
    #         print(i)
    #
    #     company_url = soup.select_one(selector='p a')
    #     print(company_url)
    #
    #     name = soup.select_one(selector='#name')
    #     print(name)
    #
    #     heading = soup.select_one(selector='.heading')
    #     print(heading)




if __name__ == '__main__':
    main()


