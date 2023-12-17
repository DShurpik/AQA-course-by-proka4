import time

from selenium import webdriver
from selenium.webdriver.common.by import *

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

driver.get('https://www.demoblaze.com/index.html')
time.sleep(2)
list = driver.find_elements(By.CLASS_NAME, 'card-block')
print(list[1].get_attribute('outerText'))

print(list[0].get_property('innerText'))

driver.quit()