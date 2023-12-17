import time

from selenium import webdriver
from selenium.webdriver.common.by import *

webdriver = webdriver.Chrome()
webdriver.implicitly_wait(10)

webdriver.get('https://the-internet.herokuapp.com/checkboxes')

print(webdriver.find_element(By.XPATH, '//input[@type="checkbox"][1]').get_attribute('checked'))
print(webdriver.find_element(By.XPATH, '//input[@type="checkbox"][1]').is_selected())
webdriver.find_element(By.XPATH, '//input[@type="checkbox"][1]').click()

print(webdriver.find_element(By.XPATH, '//input[@type="checkbox"][1]').get_attribute('checked'))
print(webdriver.find_element(By.XPATH, '//input[@type="checkbox"][1]').is_selected())
time.sleep(2)