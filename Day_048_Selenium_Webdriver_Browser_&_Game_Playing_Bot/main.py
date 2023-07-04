from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# links_list = ["one", "two", "three", "four", "five"]
# for num in range(len(links_list)):
#     print(num)
#     print(links_list[num])

driver = webdriver.Chrome()
driver.get("https://www.ghanaweb.com/GhanaHomePage/NewsArchive/")

titles_list = []
links_list = []
news_list = []
text_list = []

elems = driver.find_elements(By.ID, "inner-left-col")
for elem in elems:
    for title in elem.find_elements(By.CLASS_NAME, "info"):
        headline = title.text
        titles_list.append(headline)

    for link_elem in elem.find_elements(By.TAG_NAME, "a"):
        link = link_elem.get_attribute(name="href")
        links_list.append(link)

for num in range(len(titles_list)):
    news_list.append({"headline": titles_list[num], "link": links_list[num], "text": text_list[num]})

for item in news_list:
    print(item["headline"], item["link"], item["text"])

