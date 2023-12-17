import time

from selenium import webdriver
from selenium.webdriver.common.by import *

webdriver = webdriver.Chrome()
webdriver.implicitly_wait(10)

webdriver.get('https://the-internet.herokuapp.com/windows')

webdriver.find_element(By.LINK_TEXT, 'Click Here').click()
time.sleep(2)

tabs = webdriver.window_handles

webdriver.switch_to.window(tabs[1])

text = webdriver.find_element(By.XPATH, '//h3').get_attribute('innerText')
print(text)