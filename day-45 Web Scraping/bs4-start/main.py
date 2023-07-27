from bs4 import BeautifulSoup
import requests

# find the most upvoted entry

response = requests.get("https://news.ycombinator.com")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", rel="noreferrer")


article_link = []
article_text = []

for article_tag in articles:
    article_link.append(article_tag.get("href"))
    article_text.append(article_tag.getText())

upvote =[score.getText() for score in soup.find_all(name="span", class_="score")]
article_upvote = [int(score.split()[0]) for score in upvote]

# print(article_text)
# print(article_link)
# print(article_upvote)


index_of_max = article_upvote.index(max(article_upvote))
print(index_of_max+1)
print(article_text[index_of_max])
print(article_link[index_of_max])






















