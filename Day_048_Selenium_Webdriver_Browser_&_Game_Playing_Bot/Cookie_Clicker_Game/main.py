import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")


big_cookie = driver.find_element(By.ID, "cookie")

click_big_cookie = True
while click_big_cookie:
    big_cookie.click()

    # if stop_clicking == "yes":
    #     click_big_cookie = False

input("input: ")