import requests
import string
import os

from bs4 import BeautifulSoup


def get_soup(url, page_number=1):
    response = requests.get(url, {"page": page_number})
    return BeautifulSoup(response.content, 'html.parser')


def save_data(articles_type, page_number):
    main_soup = get_soup("https://www.nature.com/nature/articles?sort=PubDate&year=2020", page_number)
    os.mkdir("Page_" + page_number)
    os.chdir("Page_" + page_number)
    for i in main_soup.find_all("article"):
        if i.find("span", {"data-test": "article.type"}).text.strip() == articles_type:
            title = "".join([x for x in i.find("a").text if x not in string.punctuation]).replace(" ", "_") + ".txt"
            url = i.find("a", {"data-track-action": "view article"}).get("href")
            article_soup = get_soup("https://www.nature.com" + url)
            content = article_soup.find("div", {"class": "c-article-body u-clearfix"}).find_all(("p", "h2"))
            article = "\n".join([x.text for x in content if not x.text.startswith("\n")])
            with open(title, "wb") as article_file:
                article_file.write(article.encode())
    os.chdir(os.path.dirname(os.getcwd()))


def main():
    pages_number = int(input())
    articles_type = input()
    for page_number in range(1, pages_number + 1):
        save_data(articles_type, str(page_number))
    print("Saved all articles.")


if __name__ == "__main__":
    main()
