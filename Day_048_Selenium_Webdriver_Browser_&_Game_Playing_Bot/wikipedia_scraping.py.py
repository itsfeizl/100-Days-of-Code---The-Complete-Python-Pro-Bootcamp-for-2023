from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# meta_wiki = driver.find_element(By.LINK_TEXT, "Meta-Wiki")
# meta_wiki.click()

# search = driver.find_element(By.NAME, "search")
# search.clear()
# search.send_keys("python")
# search.send_keys(Keys.RETURN)

# Keep the browser open with these methods:
time.sleep(10)  # Browser will stay open for 10 seconds after executing the code
# input("Press Enter to continue...")  # Browser will wait for a user input, thus infinitely until there's an input or until user closes the browser


driver.quit()
