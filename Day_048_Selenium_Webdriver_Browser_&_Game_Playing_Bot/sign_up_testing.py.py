from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://fill.dev/form/registration-email")

f_name = driver.find_element(By.NAME, "email")
f_name.clear()
f_name.send_keys("feizl@email.com")

l_name = driver.find_element(By.NAME, "password")
l_name.clear()
l_name.send_keys("Marani_is_the_Bomb")

email = driver.find_element(By.NAME, "password_confirmation")
email.clear()
email.send_keys("Marani_is_the_Bomb")

btn = driver.find_element(By.CLASS_NAME, "btn")
btn.click()

input("Input a text...")