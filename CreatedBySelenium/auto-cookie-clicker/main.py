from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

keep_click = True

cookie = driver.find_element(By.ID, value="cookie")


def inspect():
    inspection = driver.find_element(By.ID, value="store")
    products = inspection.find_elements(By.TAG_NAME, value="div")
    considerations = []
    for product in products:
        status = product.get_attribute("class")
        if status == "":
            considerations.append(product)
    return considerations


def shopping():
    considerations = inspect()
    for consideration in reversed(considerations):
        consideration.click()


while keep_click:
    cookie.click()
    time.sleep(5)  # 5초 대기
    shopping()  # 5초마다 shopping() 함수 호출
