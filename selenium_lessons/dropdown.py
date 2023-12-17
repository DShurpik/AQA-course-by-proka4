import time

from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.support.select import Select

webdriver = webdriver.Chrome()
webdriver.implicitly_wait(10)

webdriver.get('https://the-internet.herokuapp.com/dropdown')

dropdown = Select(webdriver.find_element(By.ID, "dropdown"))
time.sleep(1)
dropdown.select_by_index(1)
time.sleep(1)
dropdown.select_by_value("2")
time.sleep(1)
dropdown.select_by_visible_text('Option 1')
time.sleep(1)
all_options = dropdown.options
print(all_options)