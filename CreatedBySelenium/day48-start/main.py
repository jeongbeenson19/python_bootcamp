from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.coupang.com/vp/products/5071892418?itemId=18226192789&vendorItemId=86532415890&q=%EC%A0%9C%EB"
           "%A1%9C%EC%BD%9C%EB%9D%BC&itemsCount=36&searchId=4fcf19dd9f3c47c191d41acc0b6cf40f&rank=6&isAddedCart=")

price = driver.find_element(By.CLASS_NAME, value="unit-price")
print(price.text)

driver.quit()
