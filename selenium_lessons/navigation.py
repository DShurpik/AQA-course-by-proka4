import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.demoblaze.com/index.html')
time.sleep(5)
driver.find_element(by=By.ID, value='cartur').click()
time.sleep(5)

# Back navigation
driver.back()

time.sleep(3)
# Refresh browser page
driver.refresh()
time.sleep(3)

driver.close()
driver.quit()