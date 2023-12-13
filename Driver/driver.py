from selenium import webdriver

driver = webdriver.Chrome()

#firefox_driver = webdriver.Firefox()

driver.implicitly_wait(3)

driver.close()
driver.quit()
