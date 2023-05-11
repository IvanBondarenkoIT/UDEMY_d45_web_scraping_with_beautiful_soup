from bs4 import BeautifulSoup


def main():
    with open('website.html', 'r') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        print(soup.title)


if __name__ == '__main__':
    main()


