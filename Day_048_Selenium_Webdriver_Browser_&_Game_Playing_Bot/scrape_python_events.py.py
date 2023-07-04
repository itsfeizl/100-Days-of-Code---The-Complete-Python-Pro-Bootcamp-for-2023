from selenium import webdriver
from selenium.webdriver.common.by import By

my_dict = {}

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title

event_time_elem = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_name_elem = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

for num in range(len(event_name_elem)):
    my_dict[num] = {
        "event_time": event_time_elem[num].text,
        "event_name": event_name_elem[num].text
    }

for key, value in my_dict.items():
    print(f"{key}: {value}")


driver.close()