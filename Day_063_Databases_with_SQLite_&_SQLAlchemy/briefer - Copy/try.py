from bs4 import BeautifulSoup
import requests

CHATGPT_API_NAME = "Myname=Faisal+Alhassan"
CHATGPT_API_KEY = "Bearer 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"
chatgpt_ai_endpoint = "https://api.openai.com/v1/chat/completions"

news_link = input("Paste link: ")

response = requests.get(news_link)
soup = BeautifulSoup(response.text, "html.parser")

article = soup.select_one(selector=".article-details")
title = article.select_one(selector="h1").getText()
content = ""
paragraph_list = article.select(selector="p")
for p in paragraph_list[:-2]:
    content += p.getText()


params = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": f"Summarize this text in 50 words: {content}"}]
}

headers = {
    "Authorization": CHATGPT_API_KEY
}

response = requests.post(url=chatgpt_ai_endpoint, stream=True, json=params, headers=headers)
content_summary = response.json()["choices"][0]["message"]["content"]

print(content_summary)
