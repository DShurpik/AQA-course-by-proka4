from selenium import webdriver
from selenium.webdriver.common.by import * # Import all values from By

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

driver.get('https://www.demoblaze.com/index.html')
driver.find_element(By.ID, 'cartur')