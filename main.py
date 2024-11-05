from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")


yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")
article = soup.find_all(name="span", class_="titleline")
article_texts= []
article_links=[]

for article_tag in article:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find("a").get("href")
    article_links.append(link)




article_upvote= [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


print(article_texts)
print(article_links)
print(article_upvote)


largest_numb = max(article_upvote)
largest_index = article_upvote.index(largest_numb)

print(article_texts[largest_index])
print(article_links[largest_index])

