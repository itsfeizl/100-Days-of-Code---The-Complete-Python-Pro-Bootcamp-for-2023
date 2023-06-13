from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_website = response.text

web_soup = BeautifulSoup(yc_website, "html.parser")
# print(web_soup)
titles_list = []
title_anchor_list = []

title_span_tag_list = web_soup.find_all(name="span", class_="titleline")
for title in title_span_tag_list:
    titles_list.append(title.a.getText())
    title_anchor_list.append(title.a.get("href"))

upvotes_list = []
article_upvotes = web_soup.find_all(name="span", class_="score")
for votes in article_upvotes:
    upvotes_list.append(int(votes.getText().split()[0]))


top_vote = min(upvotes_list)
print(titles_list[upvotes_list.index(top_vote)])
print(title_anchor_list[upvotes_list.index(top_vote)])
