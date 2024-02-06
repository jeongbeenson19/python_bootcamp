from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_dict = {}
event_list = []
target = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
date = target.find_elements(By.TAG_NAME, value='time')
event = target.find_elements(By.TAG_NAME, value='a')

for date, event in zip(date, event):
    plan = {'time': date.text, 'event': event.text}
    event_list.append(plan)

for idx, event in enumerate(event_list):
    event_dict[idx] = event


print(event_dict)
driver.quit()
