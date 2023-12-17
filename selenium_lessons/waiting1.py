import time

from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Exp_conditions

webdriver = webdriver.Chrome()
# webdriver.implicitly_wait(5) Явное ожидание

wait = WebDriverWait(webdriver, 15, poll_frequency=1)

webdriver.get('https://the-internet.herokuapp.com/dynamic_controls')
time.sleep(2)
webdriver.find_element(By.XPATH, "//button[text()='Remove']").click()
time.sleep(2)
wait.until(Exp_conditions.invisibility_of_element_located((By.LINK_TEXT, 'Remove')))

time.sleep(2)
