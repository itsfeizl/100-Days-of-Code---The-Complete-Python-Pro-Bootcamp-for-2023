import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

ACCOUNT_EMAIL = "faisal.alhassan61@gmail.com"
ACCOUNT_PASSWORD = "Myname=Faisal+Alhassan"

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_in_btn = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_btn.click()

email = driver.find_element(By.NAME, "session_key")
email.clear()
email.send_keys(ACCOUNT_EMAIL)

password = driver.find_element(By.NAME, "session_password")
password.clear()
password.send_keys(ACCOUNT_PASSWORD)

sign_in_btn = driver.find_element(By.CLASS_NAME, "btn__primary--large")
sign_in_btn.click()

time.sleep(30)

drop_btn = driver.find_element(By.ID, "ember116")
drop_btn.click()
#
apply_btn = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
apply_btn.click()


input("Input: ")
