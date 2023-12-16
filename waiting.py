from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Exp_conditions

webdriver = webdriver.Chrome()
# webdriver.implicitly_wait(5) Явное ожидание

wait = WebDriverWait(webdriver, 15, poll_frequency=1)

webdriver.get('https://demoqa.com/dynamic-properties')

element = wait.until(Exp_conditions.element_to_be_clickable((By.ID, 'enableAfter')))

wait.until(Exp_conditions.visibility_of_element_located((By.ID, 'visibleAfter')))
