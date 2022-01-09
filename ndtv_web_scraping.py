from bs4 import BeautifulSoup
import requests
import urllib
import urllib.request,sys,time
# requests library, requests for information
from newspaper import Article
import nltk
nltk.download('punkt')

html_text = requests.get("https://www.ndtv.com/search?searchtext=road-accidents-in-hyderabad").text

# now to beautify this,
#create a soup variable for bs4
# print(html_text)
soup = BeautifulSoup(html_text , 'lxml')

articles = soup.find_all('li' , class_ = 'src_lst-li')
n = 0
for article in articles:

    # article = soup.find_all('li' , class_ = 'src_lst-li')
    n = n+1

    article_title = article.find('div' , class_ = 'src_itm-ttl').text
    article_info = article.find('span' , class_ = 'src_itm-stx').text
    # Link=st.find('a')['href'].strip()
    article_link = article.find('a')['href'].strip()
    # article_publish_date = article.find()
    # article_source =

    # print(f'Entire Article -> {article.text}')
    print(f'Article_number{n}')
    print(f'Article_title -> {article_title}')
    other_info = article_info.split("|")
    # del other_info[-1]
    print(other_info)
    # print(article_link)
    article_1 = Article(article_link)
    article_1.download()
    article_1.html
    article_1.parse()
    article_1.nlp()
    entire_article = article_1.text
    article_summary = article_1.summary
    article_keywords = article_1.keywords
    article_pub_date = article_1.publish_date
    # print(entire_article)
    print(f'Summary of the article {article_summary}')
    print(f'Keywords: {article_keywords}')
    print(f' Publish Date{article_pub_date}')

    # entire_article = requests.get(article_link).text
    # soup2 = B



    print('----------------------------------------------------')

