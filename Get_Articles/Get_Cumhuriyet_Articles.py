from newspaper import Article
from bs4 import BeautifulSoup
import requests
import re


def get_text_with_url(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def get_title_with_url(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.title

def get_cumhuriyet_article_links(total_page,author):
    links = []
    main_page= "https://www.cumhuriyet.com.tr"
    for i in range(6, int(total_page)):
        main = "https://www.cumhuriyet.com.tr/koseyazari/3/{}/{}.html".format(i,author)
        r = requests.get(main)
        soup = BeautifulSoup(r.text,"html.parser")
        for i in soup.find("ul",{"class":"yazilar"}).find_all("li"):
            p = i.find('a', href=re.compile(r'[/]([a-z]|[A-Z])\w+')).attrs['href']
            links.append(main_page + p)

    return links

links = get_cumhuriyet_article_links(total_page = 35, author = "adnan-dincer")
stop_signs = '/:*?"<>|\\'
i = 1
for item in links:
    text= get_text_with_url(item)
    title = get_title_with_url(item)

    for sign in stop_signs:
        title = title.replace(sign, "")

    column = open("C:/Users/vct_3/Desktop/Köşe Yazıları/" + "%s" % title + ".txt", "w")
    column.write(text)
    column.close()
    print("{}. haber basıldı..." .format(i))
    i += 1

